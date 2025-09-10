###### *An Average OS Productions (AOSP) project*
```
  ____            S T U P I D 
 / /\ \           T H R E A D 
/ /  \ \          S Y S T E M 
\ \ _ \ \         W I T H I N 
 \_(_) \_\        P Y T H O N
```
# Input
###### "Why use an operating system if the whole thing's a demo?" - Average, lead developer
This module provides various ways to allow for user input in a PY-COM OS.

## Overview
This script has three different versions, this document will cover all three.
In order to get one of the version classes you must call `input.Input(version: str)`. (replacing "version: str" with one of the versions)
## V1
This is a very basic version that you can assign a hook to a specific key-code or key-name and the script will call you function whenever the key is active.
### `assign_hook()`
The signature of this method is `assign_hook(key: str | int, func: function)`.
This function allows you to assign a function be called when a key is found to be active.  
###### Note: *`__on_key()` is name-mangled for a reason, please do not call it*
## V2
This function still allows you to set up hooks, however you can choose when to check for inputs.
### `assign_hook()`.
The signature of this method is `assign_hook(key: str | int, func: function)`
Call this function along with proper parameters to set up a hook
### `check_input()`
The signature of this method is `check_input(key: str | int)`.
This function allows you to check one key for activity and if active, call the hook.
### `check_inputs()`
This method doesn't accept parameters.
This function will check all currently hooked keys for activity, calling hooks when necessary.
## V3
Just like V2 but only allows a key press to activate a hook once, instead of repeatedly calling the hook.
### `assign_faulty_hook()`
The signature of this method is `assign_faulty_hook(key: str | int)`
This function is used to make the script check the key, not much else though.
### `return_pressed()`
This method doesn't accept parameters.
This function returns all currently pressed key-codes.
## Helpers
The script contains two helper dictionaries, one, `name_to_code`, converts key-names to key-codes and two, `code_to_name`, converts key-codes to key-names.