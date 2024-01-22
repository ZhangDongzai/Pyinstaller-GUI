# Pyinstall GUI

from os import popen
import tkinter as tk


NAME = "Pyinstaller-GUI"
VERSION = (0, 0, 1)


class GUI:
    """图形界面"""

    def __init__(self) -> None:
        self.init_window()
        self.set_frame()
        self.loop_window()

    def init_window(self) -> None:
        """初始化窗口"""
        self.window = tk.Tk()

        # 参数设置
        self.window.title(NAME)

    def set_frame(self) -> None:
        """设置组件"""
        pass

    def loop_window(self) -> None:
        """窗口循环"""
        self.window.mainloop()

    def run_pyinstaller(self) -> None:
        """运行pyinstaller"""
        pass


if __name__ == "__main__":
    GUI()