# Lecture 11--Spherical/Cylindrical Coordinates

This repository exists for personal use and serves to host the variable files, particularly those associated with Manim.

Though the animations and images themselves currently in use are located at `/renders/`, you may produce them yourself via `master.py`, after downloading and installing the necessary system requirements, namely [MikTeX](https://miktex.org/download), [Python 3.7](https://www.python.org/downloads/), [FFmpeg](https://ffmpeg.org/download.html), [Sox](https://sourceforge.net/projects/sox/), and, of course, [Manim](https://github.com/3b1b/manim).

In a terminal window:
```sh
$ cd "C:\path\to\lecture11"
$ python -m manim master.py <scene_class_name> <args>
```

Alternatively, you can render via the `manim` command, provided you've installed `manimlib` previously:
```sh
$ pip3 install manimlib
$ manim master.py <scene_class_name> <args>
```

`args` may take any of the following forms:
* `-i` for a .gif output
* `-p` to preview the content upon completion (auto-popup)
* `-l` for low-quality rendering
* `-m` for medium-quality rendering
* `-r <resolution>` to render in the specified resolution

Note: The above arguments can be combined, for instance
```sh
$ manim master.py SphereSThenT -mi
```
will yield a medium-quality rendering (720p, 30fps) of the scene with declaration
```python
class SphereSThenT(ThreeDScene):
    def construct(self):
        ...
```

Happy animating!
