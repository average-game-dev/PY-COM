# Errors in PY-COM
This Markdown file will go over the `/source/error.py` file and usage.

## Error handling
Usually errors should be passed to the "kernel" error handling script, this script contains many things to make you life easier, however you can make your own errors and not use the kernel error handling script.

## Why use the kernel error handling?
The kernel error handling is heavily documented and will provide an insight into what occurred to both the user and the developer.

## Classic kernel errors
###### _Errors that are mostly used by the other kernel scripts._

These errors can be used by your operating system, but refrain from using these kernel level errors too much as you might trigger an error that does something you don't want.

| Error Name   | Usage                                                                                     |  
|--------------|-------------------------------------------------------------------------------------------|
| DisplayError | For use whenever a general display error has occurred.                                    |
| DiskError    | For use whenever a general disk error has occurred.                                       |
| InputError   | For use whenever a general input error has occurred.                                      |
| Error        | For use whenever something inexplicable that doesn't fit any other error category occurs. |
| FuckYouError | For use when you really want to tell yourself or the user they fucked up bad.             |
| WTFError     | For use when something genuinely baffling has occurred.                                   |

## More in-depth on each error now
**_Note: whatever passed to the second argument will be converted to string by `f"{message} {args}"`. If nothing is passed to the exception it will give a generic error message._**

### DisplayError
A DisplayError should be raised whenever an error with anything related to the display occurs.
It's usage in code should be something like:
```python
from source import error

if monitor_too_bright:  
    do_something_intentional
else:
    raise error.DisplayError("<error message>", <any extra arguments>)
```
### DiskError
A DiskError should be raised whenever an error related to the disk or filesystem happens. 
It's usage in code should be something like:  
```python
from source import error

if disk_spinny:  
    do_something_intentional
else:
    raise error.DiskError("<error message>", <any extra arguments>)
```
### Error
The basic Error exception should usually not be used as it is undescriptive and vague, however it does exist for some circumstances.
It's usage in code should be something like:  
```python
from source import error

if condition:  
    do_something_intentional
else:
    raise error.Error("<error message>", <any extra arguments>)
```
### FuckYouError
The error used when you feel the need to insult you or the user, this feeling is entirely natural and this error should be used to express it.
It's usage in code should be something like:  
```python
from source import error

if user_did_not_do_something_dumb:  
    do_something_intentional
else:
    raise error.FuckYouError("<error message>", <any extra arguments>)
```
### WTFError
This error is used as "specialty" error, it doesn't really have a definition or use case but rather is used whenever you feel like it. This error is special in the fact that you can not give this error an error message because you use this error only in scenarios where you couldn't have an explanation. 
It's usage in code should be something like:  
```python
from source import error

if condition_that_really_should_be_true:  
    do_something_intentional
else:
    raise error.WTFError(<any arguments>)
```
## Custom Errors
You can raise any error you want, the kernel will not try to catch or do anything to it.
## ***Error Guidelines***
>- Make error messages clear.
>- If you have an error code associated with an error message or its args please fulfill your duty and properly document said error code.
>- If possible catch and recover from any errors