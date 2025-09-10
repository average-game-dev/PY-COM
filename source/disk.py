from source import error

files = {
    # filename : [properties, [start, end], [used_start, used_end]]
}
global_debug = True
global_debug_level = 10  # 0=silent, 10=all debug

def debug(text, level):
    if global_debug and level <= global_debug_level:
        print(f"[DEBUG_{level}] {text}", flush=True)

# ---------------- Partition Table ----------------

def load_partition_table():
    debug("Loading partition table metadata", 10)
    try:
        with open("partition_table.txt", "r") as table:
            lines = table.readlines()
            for idx, line in enumerate(lines):
                line = line.strip()
                debug(f"Line {idx}: '{line}'", 10)
                if not line:
                    continue
                parts = line.split()
                name = parts[0]
                if len(parts) == 6:
                    properties = parts[1]
                    start, end, used_start, used_end = map(int, parts[2:])
                elif len(parts) == 5:
                    properties = ""
                    start, end, used_start, used_end = map(int, parts[1:])
                elif len(parts) == 4:
                    properties = parts[1]
                    start, end = map(int, parts[2:])
                    used_start, used_end = start, end
                elif len(parts) == 3:
                    properties = ""
                    start, end = map(int, parts[1:])
                    used_start, used_end = start, end
                else:
                    debug(f"Skipping invalid line: {line}", 5)
                    continue
                files[name] = [properties, [start, end], [used_start, used_end]]
                debug(f"Parsed file '{name}': {files[name]}", 5)
        debug(f"Loaded files dict: {files}", 5)
    except FileNotFoundError:
        debug("partition_table.txt not found. Starting with empty files dict.", 5)

def save_partition_table():
    debug("Saving partition table metadata", 10)
    try:
        with open("partition_table.txt", "w") as table:
            for fname, (props, (start, end), (used_start, used_end)) in files.items():
                if props:
                    line = f"{fname} {props} {start} {end} {used_start} {used_end}\n"
                else:
                    line = f"{fname} {start} {end} {used_start} {used_end}\n"
                debug(f"Writing line: {line.strip()}", 10)
                table.write(line)
        debug("Partition table saved.", 5)
    except Exception as e:
        raise error.DiskError("Failed to save partition table", e)

# ---------------- File Management ----------------

def create_file(filename: str, start: int, end: int, properties: str="", used_start: int=None, used_end: int=None):
    debug(f"Creating file '{filename}' with start={start}, end={end}, props='{properties}'", 5)
    if start >= end:
        raise error.DiskError(f"Invalid range: start {start} >= end {end}")
    if filename in files:
        raise error.DiskError(f"File '{filename}' already exists")
    used_start = used_start if used_start is not None else start
    used_end = used_end if used_end is not None else end
    files[filename] = [properties, [start, end], [used_start, used_end]]
    try:
        with open("disk.img", "r+b") as disk:
            disk.seek(start)
            disk.write(b'\x00' * (end - start))
    except Exception as e:
        raise error.DiskError(f"Failed to write file '{filename}' to disk", e)
    debug(f"File '{filename}' added to files dict.", 5)
    save_partition_table()

def delete_file(filename):
    debug(f"Deleting file '{filename}'", 5)
    if filename not in files:
        raise error.DiskError(f"File '{filename}' does not exist")
    if 'r' in files[filename][0]:
        raise error.DiskError(f"File '{filename}' is read-only")
    files.pop(filename)
    debug(f"File '{filename}' removed from files dict.", 5)
    save_partition_table()

def delete_read_only_file(filename):
    debug(f"Force deleting read-only file '{filename}'", 5)
    if filename in files:
        files.pop(filename)
        debug(f"File '{filename}' force-removed.", 5)
        save_partition_table()
    else:
        raise error.DiskError(f"File '{filename}' not found for forced delete")

def is_read_only(filename):
    ro = 'r' in files.get(filename, [""])[0]
    debug(f"Checked read-only status of '{filename}': {ro}", 10)
    return ro

# ---------------- Bytes Helpers ----------------

def is_bytes_like(data):
    result = isinstance(data, (bytes, bytearray, memoryview))
    debug(f"is_bytes_like check: {result} for data type {type(data)}", 10)
    return result

def bytes_in_input(data):
    length = len(data)
    debug(f"bytes_in_input: {length} bytes", 10)
    return length

def write_bytes(contents, seek, end_seek=0):
    debug(f"write_bytes called with length={len(contents) if is_bytes_like(contents) else 'N/A'}, seek={seek}, end_seek={end_seek}", 5)
    if not is_bytes_like(contents):
        raise error.DiskError("write_bytes received non-bytes-like input")
    max_len = len(contents)
    if end_seek > 0 and end_seek > seek:
        max_len = min(len(contents), end_seek - seek)
    try:
        with open('disk.img', 'r+b') as disk:
            disk.seek(seek)
            disk.write(contents[:max_len])
        debug(f"Wrote {max_len} bytes starting at position {seek}", 5)
    except Exception as e:
        raise error.DiskError(f"Failed to write bytes to disk at position {seek}", e)

def write_to_file(filename, contents, local_seek=0):
    if filename not in files:
        raise error.DiskError(f"Attempted to write to non-existent file '{filename}'")

    seek = files[filename][1][0] + local_seek
    end_seek = files[filename][1][1]

    if isinstance(contents, str):
        contents = contents.encode('utf-8')
    elif isinstance(contents, list):
        contents = bytes(contents)
    elif not is_bytes_like(contents):
        raise error.DiskError(f"Unsupported type for writing to file '{filename}'")

    write_bytes(contents, seek, end_seek)

# ---------------- CLI ----------------

load_partition_table()

if __name__ == "__main__":
    try:
        while True:
            user_input = input("|> ").strip()
            if not user_input:
                continue
            cmds = user_input.split()
            cmd = cmds[0].lower()

            try:
                if cmd == "create":
                    if len(cmds) >= 4:
                        filename = cmds[1]
                        start = int(cmds[2])
                        end = int(cmds[3])
                        properties = cmds[4] if len(cmds) > 4 else ""
                        create_file(filename, start, end, properties)
                    else:
                        print("Usage: create <filename> <start> <end> [properties]")

                elif cmd == "delete":
                    if len(cmds) >= 2:
                        filename = cmds[1]
                        if len(cmds) > 2 and cmds[2].lower() == "ro":
                            delete_read_only_file(filename)
                        else:
                            delete_file(filename)
                    else:
                        print("Usage: delete <filename> [ro]")

                elif cmd == "write":
                    if len(cmds) >= 3:
                        filename = cmds[1]
                        contents = cmds[2]
                        local_seek = int(cmds[3]) if len(cmds) > 3 else 0
                        write_to_file(filename, contents, local_seek)
                    else:
                        print("Usage: write <filename> <contents> [local_seek]")

                elif cmd == "print":
                    print(files)

                else:
                    print(f"Unknown command: {cmd}")
            except error.DiskError as e:
                print(f"DiskError: {e}")
            except Exception as e:
                print(f"Error processing command '{cmd}': {e}")

    except KeyboardInterrupt:
        print("\nExiting.")
        exit(0)
