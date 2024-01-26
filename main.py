# Pyinstall GUI

from os import popen
import tkinter as tk
import tkinter.filedialog


VERSION = (0, 0, 1)
NAME = f"Pyinstaller GUI v{VERSION[0]}.{VERSION[1]}.{VERSION[2]}"
SIZE = WIDTH, HEIGHT = 500, 500


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
        # self.window.geometry(f"{WIDTH}x{HEIGHT}")

    def set_frame(self) -> None:
        """设置组件"""
        # 项目名称
        self.project_StringVar = tk.StringVar()

        project_Label = tk.Label(master=self.window, text="project name")
        project_Entry = tk.Entry(master=self.window, textvariable=self.project_StringVar)
   
        # .py 文件路径
        self.py_StringVar = tk.StringVar()

        py_Label = tk.Label(master=self.window, text=".py path")
        py_Entry = tk.Entry(master=self.window, textvariable=self.py_StringVar)
        py_Button = tk.Button(master=self.window, text="choose",
                                command=lambda:self.file_choose(("Python File", ".py")))
        
        # .ico 文件路径
        self.ico_StringVar = tk.StringVar()

        ico_Label = tk.Label(master=self.window, text=".ico path")
        ico_Entry = tk.Entry(master=self.window, textvariable=self.ico_StringVar)
        ico_Button = tk.Button(master=self.window, text="choose",
                                command=lambda:self.file_choose(("ICO File", ".ico")))

        # 运行及参数
        self.run_StringVar = tk.StringVar()

        run_Button = tk.Button(master=self.window, text="Run",
                               command=self.run_pyinstaller)
        run_Entry = tk.Entry(master=self.window, textvariable=self.run_StringVar)

        # 更改时刷新
        project_Entry.bind("<KeyRelease>", self.update_run_Entry)
        py_Entry.bind("<KeyRelease>", self.update_run_Entry)
        ico_Entry.bind("<KeyRelease>", self.update_run_Entry)

        # 布局
        project_Label.grid(row=0, column=0)
        project_Entry.grid(row=0, column=1, ipadx=10)

        py_Label.grid(row=1, column=0)
        py_Entry.grid(row=1, column=1, ipadx=10)
        py_Button.grid(row=1, column=2)

        ico_Label.grid(row=2, column=0)
        ico_Entry.grid(row=2, column=1, ipadx=10)
        ico_Button.grid(row=2, column=2)

        run_Button.grid(row=3, columnspan=3)
        run_Entry.grid(row=4, column=0, columnspan=3, padx=10, sticky=tk.N + tk.S + tk.W + tk.E)

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

        self.update_run_Entry()

    def update_run_Entry(self, event=None) -> None:
        """刷新run_Entry的内容"""
        project_name = self.project_StringVar.get()
        py_path = self.py_StringVar.get()
        ico_path = self.ico_StringVar.get()

        command = f"pyinstaller {py_path}"

        if project_name.strip(' ') != '':
            # 设置项目名称
            command += f" -n {project_name}"
        if ico_path.strip(' ') != '':
            # 设置图标
            command += f" -i {ico_path}"
        
        self.run_StringVar.set(value=command)

    def run_pyinstaller(self) -> None:
        """运行pyinstaller"""
        self.out_file = popen(cmd=self.run_StringVar.get(), mode="r", buffering=-1)


if __name__ == "__main__":
    GUI()