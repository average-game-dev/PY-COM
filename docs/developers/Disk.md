###### *An Average OS Productions (AOSP) project*
```
  ____            S T U P I D 
 / /\ \           T H R E A D 
/ /  \ \          S Y S T E M 
\ \ _ \ \         W I T H I N 
 \_(_) \_\        P Y T H O N
```

# Disk
###### "I'll be honest, this is dark magic even I don't understand." - Average, lead developer
The disk system is a kernel module that, like the display script, will be changing a lot within a future update.
The disk system is meant to give a slightly higher level access to the disk without restricting your access too much.  
## Overview
This kernel module is special because you can set `global_debug_level` from 0 through 10 to decrease or increase debug output to the python console.  
The script uses a `files` dictionary to store the partition table and changes to said partition table before writing to the `partition_table.txt` file.
The `files` dictionary uses the following format:
`<filename>: [<properties>, [start_byte, end_byte], [used_start_byte, used_end_byte]`  
*Note: The partition table file is saved after every filesystem operation, usually if an error occurs you will not corrupt or lose data.*
## Functions
There are many functions to use when reading and writing to the disk.
### `save_partition_table()`
This function is a procedure-style function, meaning it neither accepts arguments, nor returns anything.
This function is called after every filesystem operation to update the `partition_table.txt` file with the updated partition table.
### `create_file()`
The signature for this function is `create_file(filename: str, start: int, end: int, used_start: int=None, used_end: int=None)` (Phew, what a mouthful!).  
This function is used to enter a file into the partition table, you can set the name, start position, end position, as well ad used space but that doesn't matter as much.  
###### Note: *This function will raise a DiskError if you try to create a file with an already existing name.*
### `delete_file(filename: str)`  
This function is used to delete a file's entry in the partition table.
###### Note: *This function will raise a DiskError if you try to delete a read-only file or a file that doesn't exist.*
###  `delete_read_only_file(filename: str)`
Be careful with this function, it will delete **any** file.
###### "It's like giving a gun to a toddler, something's bound to go wrong." - Average, lead developer
###### Note: *This function will raise a DiskError if you try to delete a read-only file or a file that doesn't exist.*
### `is_read_only(filename: str) -> bool`  
This function will return `True` is the file in question is read only, `False` if otherwise.
###### Note: *This function will raise a DiskError if you try to check a file that doesn't exist.*
## Bytes Helpers
### `is_bytes_like(data: any) -> bool`
This function returns `True` if the given data is bytes-like, `False` if otherwise.
### `bytes_in_input(data: any) -> bool`
This function returns the amount of bytes in a string or bytes-like input.
### `write_bytes()`
The signature of this function is `write_bytes(contents: bytes-like, seek: int, end_seek: int)`
The `contents` are any bytes-like object, like `b'hello world!'`, `seek` is the start byte of writing relative to the disk. `end_seek` can be used to make sure variable contents doesn't go over a certain limit.
### `write_to_file()`
The signature of this function is `write_to_file(filename: str, contents: any, local_seek: int=0)`
This function is used to write to a specific file, meaning it won't overwrite any other file's contents, this function is preferred over `write_bytes()`.
###### Note: *This function will raise a DiskError if you try to write to a file that doesn't exist.*
