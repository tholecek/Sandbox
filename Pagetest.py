import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+650+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.07, rely=0.18, relheight=0.48, relwidth=0.81)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=485)

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.06, rely=0.33, height=19, width=57)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Channel 0''')

        self.StartTest = Button(self.Frame1)
        self.StartTest.place(relx=0.06, rely=0.84, height=24, width=60)
        self.StartTest.configure(activebackground="#d9d9d9")
        self.StartTest.configure(activeforeground="#000000")
        self.StartTest.configure(background="#d9d9d9")
        self.StartTest.configure(disabledforeground="#a3a3a3")
        self.StartTest.configure(foreground="#000000")
        self.StartTest.configure(highlightbackground="#d9d9d9")
        self.StartTest.configure(highlightcolor="black")
        self.StartTest.configure(pady="0")
        self.StartTest.configure(text='''Start Test''')

        self.CH0Data = Text(self.Frame1)
        self.CH0Data.place(relx=0.06, rely=0.42, relheight=0.11, relwidth=0.11)
        self.CH0Data.configure(background="white")
        self.CH0Data.configure(font="TkTextFont")
        self.CH0Data.configure(foreground="black")
        self.CH0Data.configure(highlightbackground="#d9d9d9")
        self.CH0Data.configure(highlightcolor="black")
        self.CH0Data.configure(insertbackground="black")
        self.CH0Data.configure(relief=RIDGE)
        self.CH0Data.configure(selectbackground="#c4c4c4")
        self.CH0Data.configure(selectforeground="black")
        self.CH0Data.configure(width=54)
        self.CH0Data.configure(wrap=NONE)






if __name__ == '__main__':
    vp_start_gui()

#end
