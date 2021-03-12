import tkinter as tk
from tkinter import ttk


class Scrollbar():
    def __init__(self, parent = None):
        self.main_frame = tk.Frame(parent)
        self.main_frame.pack(fill = 'both', expand = True)

        self.canvas = tk.Canvas(self.main_frame, width = 530)

        self.canvas.pack(side = 'left', fill = 'both', expand = True)
        self.scrollbar = ttk.Scrollbar(self.main_frame,
                                       orient = 'vertical',
                                       command = self.canvas.yview)
        self.scrollbar.pack(side = 'right', fill = 'y')

        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.canvas.bind('<Configure>',
                         lambda e: self.canvas.configure(
                             scrollregion = self.canvas.bbox("all"))
                         )

        self.sub_frame = tk.Frame(self.main_frame)

        self.canvas.create_window((0,0),
                                   window = self.sub_frame,
                                   anchor='nw')
        self.values = []



class Top():
    def __init__(self, parent = None):
        self.top = tk.Toplevel(parent)

class Menu():
    def __init__(self, parent = None):
        self.menu = tk.Menu(parent)
        parent.configure(menu = self.menu)
        self.menu_b_file = tk.Menu(self.menu, tearoff = 0)
        self.menu_b_help = tk.Menu(self.menu, tearoff = 0)
        self.menu_b_pref = tk.Menu(self.menu, tearoff = 0)

        self.menu_b_file.add_command(label = 'Exit', command = parent.quit)

        self.menu_b_pref.add_command(label = 'Settings', command = self.top_preference)

        self.menu_b_help.add_command(label = 'Help', command = '')
        self.menu_b_help.add_command(label = 'About', command = self.top_about)


        self.menu.add_cascade(label = 'File',
                              menu = self.menu_b_file)


        self.menu.add_cascade(label = 'Preferences',
                              menu = self.menu_b_pref)


        self.menu.add_cascade(label = 'Help',
                              menu = self.menu_b_help)

    def top_preference(self,):
        """
        window = Top()
        window.top.title('System Monitor Settings')
        main_frame = tk.Frame(window.top)
        main_frame.grid(row = 0, column = 0)

        label_title = tk.Label(main_frame,
                               text = 'Visual Settings')
        label_title.grid(row = 0, column = 0)
        label_size = tk.Label(main_frame, text='Set Height: ')
        label_size.grid(row = 1, column = 0)

        entry_size = tk.Entry(main_frame)
        entry_size.grid(row = 1, column = 1, padx = 5)

        button = tk.Button(main_frame, text = 'Resize',
                           command = lambda: print('a'))
        button.grid(row = 1, column = 2)
        """

        raise NotImplemented

        return None

    def top_about(self,):
        window = Top()
        window.top.title('About (?)')
        text = tk.Label(window.top)
        text.configure(text = 'System Monitor\n Ver. 0.0.1\n Author: A. Berlot\n email: alexisgberlot@gmail.com', font = ('Roboto', 12))
        text.grid(row = 0, column = 0, sticky = 'w')
        return



if __name__ == '__main__':
    master = tk.Tk()
    sc = Scrollbar(master)
    for i in range(60):
        tk.Label(sc.sub_frame, text = i).grid(row=i, column = 0)
    menu = Menu(master)

    tk.mainloop()

