files = {
    # filename : [properties, [start, end], [used_start, used_end]]
}
global_debug = True
global_debug_level = 10  # 0=silent, 10=all debug

def debug(text, level):
    if global_debug and level <= global_debug_level:
        print(f"[DEBUG_{level}] {text}")

def load_partition_table():
    debug("Loading partition table metadata", 10)
    try:
        with open("partition_table.txt", "r") as table:
            lines = table.readlines()
            for idx, line in enumerate(lines):
                line = line.strip()
                debug(f"Line {idx}: '{line}'", 10)
                if line:
                    parts = line.split()
                    name = parts[0]
                    if len(parts) == 6:
                        properties = parts[1]
                        start = int(parts[2])
                        end = int(parts[3])
                        used_start = int(parts[4])
                        used_end = int(parts[5])
                    elif len(parts) == 5:
                        # If no properties but with used range
                        properties = ""
                        start = int(parts[1])
                        end = int(parts[2])
                        used_start = int(parts[3])
                        used_end = int(parts[4])
                    elif len(parts) == 4:
                        # Old format: no used range
                        properties = parts[1]
                        start = int(parts[2])
                        end = int(parts[3])
                        used_start = start
                        used_end = end
                    else:
                        # Minimal: filename start end
                        properties = ""
                        start = int(parts[1])
                        end = int(parts[2])
                        used_start = start
                        used_end = end

                    debug(f"Parsed file '{name}': props='{properties}', start={start}, end={end}, used_start={used_start}, used_end={used_end}", 5)
                    files[name] = [properties, [start, end], [used_start, used_end]]
        debug(f"Loaded files dict: {files}", 5)
    except FileNotFoundError:
        debug("partition_table.txt not found. Starting with empty files dict.", 5)

def save_partition_table():
    debug("Saving partition table metadata", 10)
    with open("partition_table.txt", "w") as table:
        for fname, (props, (start, end), (used_start, used_end)) in files.items():
            if props:
                line = f"{fname} {props} {start} {end} {used_start} {used_end}\n"
            else:
                line = f"{fname} {start} {end} {used_start} {used_end}\n"
            debug(f"Writing line: {line.strip()}", 10)
            table.write(line)
    debug("Partition table saved.", 5)

def create_file(filename, start, end, properties="", used_start=None, used_end=None):
    debug(f"Creating file '{filename}' with start={start}, end={end}, props='{properties}'", 5)
    if start < end:
        if filename not in files:
            if used_start is None:
                used_start = start
            if used_end is None:
                used_end = end
            files[filename] = [properties, [start, end], [used_start, used_end]]
            with open("disk.img", "r+b") as disk:
                disk.seek(start)
                disk.write(b'\x00' * (end - start))
            debug(f"File '{filename}' added to files dict.", 5)
            save_partition_table()
        else:
            debug(f"File '{filename}' already exists. Skipping creation.", 5)
    else:
        debug(f"Invalid range: start {start} >= end {end}. File not created.", 5)

def delete_file(filename):
    debug(f"Deleting file '{filename}'", 5)
    if filename not in files:
        debug(f"File '{filename}' does not exist.", 5)
        return
    if 'r' in files[filename][0]:
        debug(f"File '{filename}' is read-only. Cannot delete.", 5)
        return
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
        debug(f"File '{filename}' not found for forced delete.", 5)

def is_read_only(filename):
    ro = 'r' in files.get(filename, [""])[0]
    debug(f"Checked read-only status of '{filename}': {ro}", 10)
    return ro

def is_bytes_like(data):
    result = isinstance(data, (bytes, bytearray, memoryview))
    debug(f"is_bytes_like check: {result} for data type {type(data)}", 10)
    return result

def bytes_in_input(data):
    length = len(data)
    debug(f"bytes_in_input: {length} bytes", 10)
    return length

def slice_every_n_chars(s, n):
    slices = [s[i:i+n] for i in range(0, len(s), n)]
    debug(f"sliced string into {len(slices)} chunks of {n} chars", 10)
    return slices

def to_binary_string(data):
    debug(f"Converting data of type {type(data)} to binary string", 10)
    if isinstance(data, int):
        bin_str = f"{data:08b}"
    elif isinstance(data, (bytes, bytearray)):
        bin_str = ''.join(f"{b:08b}" for b in data)
    elif isinstance(data, str):
        bin_str = ''.join(f"{ord(c):08b}" for c in data)
    elif isinstance(data, list) and all(isinstance(x, int) for x in data):
        bin_str = ''.join(f"{x:08b}" for x in data)
    else:
        raise TypeError("Unsupported data type for binary conversion")
    debug(f"Binary string length: {len(bin_str)}", 10)
    return bin_str

def binary_string_to_bytes(bitstring):
    if len(bitstring) % 8 != 0:
        raise ValueError("Bit string length must be a multiple of 8")
    byte_list = [int(bitstring[i:i+8], 2) for i in range(0, len(bitstring), 8)]
    return bytes(byte_list)

def write_byte(contents, seek):
    debug(f"write_byte called with contents={contents}, seek={seek}", 5)
    if is_bytes_like(contents) and bytes_in_input(contents) == 1:
        with open('disk.img', 'r+b') as disk:
            debug(f"Seeking to position {seek - 1}", 10)
            disk.seek(seek - 1)
            disk.write(contents)
            debug(f"Wrote byte {contents} at position {seek - 1}", 5)
    else:
        debug("Invalid input to write_byte, either not bytes-like or length != 1", 5)

def write_bytes(contents, seek, end_seek=0):
    debug(f"write_bytes called with contents length={bytes_in_input(contents) if is_bytes_like(contents) else 'N/A'}, seek={seek}, end_seek={end_seek}", 5)
    if not is_bytes_like(contents):
        debug("write_bytes received non-bytes-like input. Aborting.", 5)
        print("fuck off")
        return

    length = len(contents)
    if end_seek > 0 and end_seek > seek:
        max_len = end_seek - seek
        write_data = contents[:max_len]
        debug(f"Truncated write_data to max length {max_len}", 10)
    else:
        write_data = contents
        debug(f"Writing full contents of length {length}", 10)

    with open('disk.img', 'r+b') as disk:
        disk.seek(seek)
        debug(f"Seeking to position {seek} before writing", 10)
        disk.write(write_data)
        debug(f"Wrote {len(write_data)} bytes starting at position {seek}", 5)

def write_to_file(filename, contents, local_seek=0):
    if filename not in files:
        print("fucktard")
        debug(f"Attempted to write to non-existent file '{filename}'", 5)
        return

    seek = files[filename][1][0] + local_seek
    end_seek = files[filename][1][1]
    contents_bytes = binary_string_to_bytes(to_binary_string(contents))

    write_bytes(contents_bytes, seek, end_seek)

# Load partition table at script start
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
                    # create <filename> <start> <end> [properties]
                    if len(cmds) >= 4:
                        filename = cmds[1]
                        start = int(cmds[2])
                        end = int(cmds[3])
                        properties = cmds[4] if len(cmds) > 4 else ""
                        create_file(filename, start, end, properties)
                    else:
                        print("Usage: create <filename> <start> <end> [properties]")

                elif cmd == "delete":
                    # delete <filename> [ro]
                    if len(cmds) >= 2:
                        filename = cmds[1]
                        if len(cmds) > 2 and cmds[2].lower() == "ro":
                            delete_read_only_file(filename)
                        else:
                            delete_file(filename)
                    else:
                        print("Usage: delete <filename> [ro]")

                elif cmd == "write":
                    # write <filename> <contents> [local_seek]
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
            except Exception as e:
                print(f"Error processing command '{cmd}': {e}")

    except KeyboardInterrupt:
        print("\nExiting.")
        exit(0)
