# Pyinstall GUI

from os import popen
import tkinter as tk
import tkinter.filedialog


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
        # .py 文件路径
        self.py_StringVar = tk.StringVar()

        path_Label = tk.Label(master=self.window, text=".py path")
        path_Entry = tk.Entry(master=self.window, textvariable=self.py_StringVar)
        path_Button = tk.Button(master=self.window, text="choose",
                                command=lambda:self.file_choose(("Python File", ".py")))

        path_Label.grid(row=0, column=0)
        path_Entry.grid(row=0, column=1)
        path_Button.grid(row=0, column=2)
        
        # .ico 文件路径
        self.ico_StringVar = tk.StringVar()

        ico_Label = tk.Label(master=self.window, text=".ico path")
        ico_Entry = tk.Entry(master=self.window, textvariable=self.ico_StringVar)
        ico_Button = tk.Button(master=self.window, text="choose",
                                command=lambda:self.file_choose(("ICO File", ".ico")))

        ico_Label.grid(row=1, column=0)
        ico_Entry.grid(row=1, column=1)
        ico_Button.grid(row=1, column=2)

        # 运行
        run_Button = tk.Button(master=self.window, text="Run",
                               command=self.run_pyinstaller)
        
        run_Button.grid(row=2, columnspan=3)

        # 输出
        self.out_StringVar = tk.StringVar()

        out_Text = tk.Text(master=self.window)

    def loop_window(self) -> None:
        """窗口循环"""
        self.window.mainloop()

    def file_choose(self, filetype: tuple) -> None:
        """打开文件管理器选择文件"""
        path = tkinter.filedialog.askopenfilename(title="Open file",
                                                  filetypes=[filetype])
        
        try:
            eval(f"self.{filetype[-1][1:]}_StringVar.set('{path}')")
        except TypeError:
            # 没有选择文件
            pass

    def run_pyinstaller(self) -> None:
        """运行pyinstaller"""
        py_path = self.py_StringVar.get()
        ico_path = self.ico_StringVar.get()

        command = f"pyinstaller {py_path}"

        if ico_path != '':
            # 设置图标
            command += f" -i {ico_path}"

        print(command)


if __name__ == "__main__":
    GUI()