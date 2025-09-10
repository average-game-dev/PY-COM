###### *An Average OS Productions (AOSP) project*
```
  ____            S T U P I D 
 / /\ \           T H R E A D 
/ /  \ \          S Y S T E M 
\ \ _ \ \         W I T H I N 
 \_(_) \_\        P Y T H O N
```

# Display
###### "You wanna make this look good, kid?"
#### *Note: `/source/display.py` will be changing a **lot** with in a near-future update*

## Overview
To use the standard kernel display script you simply import `from source import display`, this file contains everything you need to write to the screen, read to it, and perform updates to said screen.  
## The Class
The main `VRAM` class has all the basic stuff for display, in fact, you can instantiate two in order to make two display windows!  
There are four methods in the `VRAM` class:

###### Note: *pygame will throw an error if you write a greater than 255 color value to the screen*
###### Note: *numpy will throw an error if you try to read or write to a pixel that doesn't exist*
### `write_pixel()`

This method takes two arguments: `color_tuple` and `position`, the `color_tuple` can be any iterable object like a list, set, or tuple containing 8-bit RGB values. `position` is any iterable object like a list, set, or tuple which contains two `x`,`y` coordinates.   
### `write_pixels()`
This method is largely the same as `write_pixel()`, however you can pass an array of 8-bit RGB color values to write along with a starting position. This method returns a numba Just-In-Time optimized function which does the writing and returns the next x-coordinate after the last pixel written.
### `read_pixel()`
This method returns the RGB color value of the given `position`.
### `update_screen()`
This method flushes all changes and current pixel values of the `VRAM.vram` attribute to the display.

###### Note: *You **can** modify the `VRAM.vram` numpy array manually and call `update_screen()` to flush the display.*

