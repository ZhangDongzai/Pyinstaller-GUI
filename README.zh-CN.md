# Pyinstaller GUI
[English](README.md)  
一个提供[pyinstaller](https://pyinstaller.org)的GUI版本的项目。  
  
这个项目使用了[tkinter](https://docs.python.org/3/library/tkinter.html)和[pyinstaller](https://pyinstaller.org)。

## 背景
使用[pyinstaller](https://pyinstaller.org)有些麻烦，参数也容易遗忘，所以萌生了制作GUI版本的想法。

## 安装
[Go to Releases](https://github.com/ZhangDongzai/Pyinstaller-GUI/releases)  
  
或者编译二进制文件，请确保你拥有[pyinstaller](https://pyinstaller.org)。  
首先，下载项目。
```sh
git clone https://github.com/ZhangDongzai/Pyinstaller-GUI.git
```
然后，使用[pyinstaller](https://pyinstaller.org)编译。
```sh
pyinstaller -w -D main.py
```
最后，`./dict`下就有可执行文件了。

## 开源许可证
[MIT](LICENSE) © Richard Littauer