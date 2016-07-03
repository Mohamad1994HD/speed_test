import Tkconstants
import Tkinter
import tkFileDialog
from tkinter import StringVar, Entry, Label
import main

MINUTE = 60


class App(Tkinter.Frame):
    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 15, 'pady': 15}

        # time interval label + entry
        Label(self, text='Time interval between tests in mins (at least >= 1)').pack(**button_opt)

        self.t_val = StringVar(root)
        self.t_val.set(10)
        self.t_interval = Entry(textvariable=self.t_val).pack(**button_opt)

        # define buttons
        Tkinter.Button(self, text='Save At', command=self.asksaveasfilename).pack(**button_opt)

        Tkinter.Button(self, text='Start', command=self.start).pack(**button_opt)
        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root
        options['title'] = 'SpeedTester 1.0'

        self.filename = ''

    def asksaveasfilename(self):
        """Returns an opened file in write mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """
        # get filename
        self.filename = tkFileDialog.asksaveasfilename(**self.file_opt)

        if self.filename:
            return open(self.filename, 'w')

    def start(self):
        # set configurations
        main.CONFIG.FILE_PATH = str(self.filename)
        main.CONFIG.REQUEST_DELAY = int(self.t_val.get()) * MINUTE

        print(main.CONFIG.FILE_PATH)
        print main.CONFIG.REQUEST_DELAY

        main.start_tests()
        # from thread import start_new_thread
        # start_new_thread(main.start_tests, ())
        # try:
        #     # launch it
        #     start_tests()
        # except IOError as i:
        #     print(i)


if __name__ == '__main__':
    root = Tkinter.Tk()
    root.geometry('400x200')
    App(root).pack()
    root.mainloop()
