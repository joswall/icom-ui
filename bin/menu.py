
# https://learning.oreilly.com/library/view/python-gui-programming/9781788835886


import tkinter as tk
import sys


root = tk()

root.title("Radio Control")
root.geometry("800x600")


root()



"""
class MyRigApp(tk.Tk):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Rig Control")
        self.geometry("800x600")
        self.resizable(width=False, height=False)

    myRigApp(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
    self.columnconfigure(0, weight=1)
"""

"""
def set_menu(window, choices):
    menubar = tkinter.Menu(root)
    window.config(menu=menubar)

    def _set_choices(menu, choices):
        for label, command in choices.items():
            if isinstance(command, dict):
                # Submenu
                submenu = tkinter.Menu(menu)
                menu.add_cascade(label=label, menu=submenu)
                _set_choices(submenu, command)
            elif label == '-' and command == '-':
                # Separator
                menu.add_separator()
            else:
                # Simple choice
                menu.add_command(label=label, command=command)

    _set_choices(menubar, choices)
"""


"""
root.(root, {
    'File': OrderedDict([
        ('Open', lambda: print('Open!')),
        ('Save', lambda: print('Save')),
        ('-', '-'),
        ('Quit', lambda: sys.exit(0))
    ]),
    'Rig':,
    'Quit', lambda: sys.exit(0)
})
"""
"""
if __name__ == '__main__':
    app = MyRigApp()
    app.mainloop()
"""