###### *An Average OS Productions (AOSP) project*
```
  ____            S T U P I D 
 / /\ \           T H R E A D 
/ /  \ \          S Y S T E M 
\ \ _ \ \         W I T H I N 
 \_(_) \_\        P Y T H O N
```
# Useful Stuff
This script is mostly for one thing and one thing only:
## Writing letters to the screen
This script contains a nice dictionary, `font`, which contains a nice handmade 11x15 font. This font is made up of numpy arrays

## Framebuffer
This script also contains a framebuffer class which is the same as the `display.VRAM` class but without flushing to the screen or reading pixels, you also get a `zero_frame()` function which replaces all of the frame with `(0,0,0)`.