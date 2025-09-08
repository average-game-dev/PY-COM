# PY-COM, The stupid Python "OS"
###### *not really an OS*

**Welcome** to the PY-COM documentation, whether you're a developer wanting to expand on the framework and make your own OS, or a user wanting to try the OS created by AOSP Group PY-COM is the stupid OS for *you*.

The PY-COM OS framework (and included PY-DOS OS) are fully open source, meaning **you** can share, modify, and redistribute as much as you want. (*but you need to credit me*)
###### the official license is the CC-BY Creative Commons license (found in the LICENSE.txt or [on their website](https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt))

## Usage
With PY-COM we, the AOSP Group aim to make your experience and opinion matter. Head over to the GitHub repo and start a pull request, or shoot us an Email at `average_fps_not_a_second_acount@proton.me` 
### Developers
Usually a developer will want to learn the codebase side of PY-COM.
The files for that are in the `/docs/developers/` directory of the GitHub repo.

Developers might find the "OS" made by AOSP Group to be a nice starting point and point of reference
### Users
Usually the user will want to learn how to get any custom PY-COM OS running, head on over to the `/docs/general/` directory in order to learn about that

There is another directory (`/docs/PY-DOS`) that contains documentation specific to the AOSP Group made PY-COM OS PY-DOS (or Py-Dos)
## Overview
PY-COM offers the bare essentials for making a Python "OS" without coding the entire kernel. You have a specific script for display, input events, errors, file system, and more in the `/source/useful.py`.

**However**, if you don't want to use any of these then you can just simply choose not to import them.

Also, I hate Docker and will not use it ever, I've made this specifically to run with only a Python Venv and the dependencies.
Here's a quick start up guide:


***
###### <u>*Make sure you run these from the repo's root.*</u>
### Windows
> 1. Download the repo
> 2. Make a Python Venv with `py -V:3.10 -m venv <environment name>` (I like using "env")
> 3. Run `.\<environment name>\scripts\activate`
> 4. Run `pip install -r requirements.txt`
> 5. Run `cd OSs` to enter the OSs folder
> 6. Run the OS of your choice (like PY-DOS)
### Linux
> 1. Download the repo
> 2. Make a Python Venv with `python3.10 -m venv <environment name>` (I like using "env")
> 3. Run `source ./<environment name>/bin/activate`
> 4. Run `pip install -r requirements.txt`
> 5. Run `cd OSs` to enter the OSs folder
> 6. Run the OS of your choice (like PY-DOS)
## ***TODO***
> - [ ] Finish documentation
> - [ ] Add multithreading support (maybe)
> - [x] Add Linux support
> - [ ] Improve memory efficiency
> - [ ] Improve disk speed
> - [ ] Improve display responsiveness and speed
> 
>  *(basic housekeeping stuff)*

## Notes
Some of the "kernel" python scripts might have Jupyter Notebooks with examples and other useful info along with the Markdown file.