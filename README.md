# Pyinstaller GUI
[zh-CN](README.zh-CN.md)  
A project that provides a GUI version of [pyinstaller](https://pyinstaller.org).

This project uses the [tkinter](https://docs.python.org/3/library/tkinter.html) and [pyinstaller](https://pyinstaller.org).

## Background
Using [pyinstaller](https://pyinstaller.org) is a bit cumbersome and the parameters are easy to forget, so the idea of making a GUI version came up.

## Installation
[Go to Releases](https://github.com/ZhangDongzai/Pyinstaller-GUI/releases)

Or to compile binaries, make sure you have [pyinstaller](https://pyinstaller.org).  
First, download the project.
```sh
git clone https://github.com/ZhangDongzai/Pyinstaller-GUI.git
```
Then compile using [pyinstaller](https://pyinstaller.org).
```sh
pyinstaller -w -D main.py
```
Finally, you have the executable file under `./dict `.

## Open source license
[MIT](LICENSE) © Richard Littauer