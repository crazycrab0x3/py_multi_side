import os
import sys
import string
import random
import pyperclip
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox


class PasswordGenerator:
    def __init__(self):
        self.ClearedDefault = False
        self.DEFAULT_TEXT = 'Number of Character'

        self.master = Tk()
        self.master.withdraw()
        self.master.resizable(0, 0)
        self.master.title('Password GENERATOR')
        self.master.iconbitmap(self.resource_path('icon.ico'))

        self.width, self.height = 310, 505
        self.master.geometry(f'{self.width}x{self.height}+{self.master.winfo_screenwidth() // 2 - self.width // 2}+{self.master.winfo_screenheight() // 2 - self.height // 2}')

        self.image = PhotoImage(file=self.resource_path('title_image.png'))
        self.image_label = Label(self.master, image=self.image)
        self.image_label.pack(pady=5)

        self.number_box_var = StringVar()
        self.number_box_style = ttk.Style()
        self.number_box_style.configure('N.TEntry', foreground='grey', font=('Calibri', 12))
        self.number_box = ttk.Entry(self.master, width=35, textvariable=self.number_box_var, style='N.TEntry', justify='center')
        self.number_box_var.set(self.DEFAULT_TEXT)
        self.number_box.pack(pady=5, ipady=3)

        self.check_box_frame = Frame(self.master)
        self.check_box_items = ['UPPERCASE', 'LOWERCASE', 'NUMBERS', 'SPECIAL CHARACTERS', 'ALL']  # Options for generating password

        self.upper_var, self.lower_var, self.num_var, self.special_var, self.all_var = IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
        self.vars = [self.upper_var, self.lower_var, self.num_var, self.special_var, self.all_var]

        self.check_box_style = ttk.Style()
        self.check_box_style.configure('C.TCheckbutton', font=('Calibri', 12))

        for index, value in enumerate(self.check_box_items):  # Creating Checkbuttons as per name in "self.check_box_items" and variables as per in self.vars
            self.check_box = ttk.Checkbutton(self.check_box_frame, text=value, variable=self.vars[index], cursor='hand2', style='C.TCheckbutton')
            self.check_box.grid(row=index, column=0, sticky='w')

        self.check_box_frame.pack(pady=10)

        self.generate_password_button = Button(self.master, text='Generate Password', bg='Green', fg='white', activeforeground='white', activebackground='Green', font=('Calibri', 12), relief=FLAT, cursor='hand2', command=self.generate_button)
        self.generate_password_button.pack(pady=10)

        self.password_label = Label(self.master, font=('Calibri', 20))
        self.copy_button = Button(self.master, text='Copy', width=6, bd=0, bg='Green', fg='white', activeforeground='white', activebackground='Green', font=('Calibri', 12), relief=FLAT, cursor='hand2', command=self.copy_to_clipboard)

        self.master.bind('<Button-1>', self.focus_here)
        self.number_box.bind('<FocusIn>', self.focus_in)
        self.number_box.bind('<FocusOut>', self.focus_out)
        self.number_box.bind('<KeyPress>', self.KeyPressed)
        self.number_box.bind('<Return>', self.generate_button)
        self.master.bind('<Control-c>', self.copy_to_clipboard)
        self.master.bind('<Control-C>', self.copy_to_clipboard)
        self.generate_password_button.bind('<Return>', self.generate_button)

        self.master.after(0, self.master.deiconify)
        self.master.mainloop()

    def focus_here(self, event=None):
        '''Focus to the clicked widget'''

        event.widget.focus_force()

    def focus_in(self, event=None):
        '''Remove default text when user clicks to entry widget'''

        get = self.number_box_var.get().strip()

        if self.ClearedDefault is False and get == self.DEFAULT_TEXT:
            self.number_box_var.set('')
            self.ClearedDefault = True

    def focus_out(self, event=None):
        '''Remove focus from Entry widget when already
           focused and still user presses TAB key'''

        get = self.number_box_var.get().strip()

        if not get:
            self.ClearedDefault = False
            self.number_box_var.set(self.DEFAULT_TEXT)

    def KeyPressed(self, event=None):
        '''Inserting user pressed key only if the key is digit only'''

        num = event.keysym

        if num.isdigit():
            text = self.number_box_var.get() + num
            self.number_box_var.set(text)

            self.number_box.icursor(END)

        return 'break'

    def generate_password(self, string_combination, lengths):
        '''Generating random generated password'''

        return ''.join([random.SystemRandom().choice(string_combination) for _ in range(lengths)])

    def copy_to_clipboard(self, event=None):
        '''Copy Generated Password to the clipboard'''

        text = self.password_label['text']

        if text:
            pyperclip.copy(text)
            self.copy_button['text'] = 'Copied!'
            self.master.after(1000, lambda: self.copy_button.config(text='Copy'))

        else:
            messagebox.showerror('ERROR', 'Not yet generated password')

    def generate_button(self, event=None):
        '''Command when user clicks generate button'''

        try:
            get_var = [var.get() for var in self.vars]

            if not any(get_var):
                get_var[-1] = 1
                self.all_var.set(1)

            lengths = int(self.number_box_var.get().strip())
            string_combo = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation, string.printable[:94]]

            string_combination = ''.join({string_combo[index] for index, value in enumerate(get_var) if value == 1})
            password = self.generate_password(string_combination, lengths)

            self.password_label.config(text=password)
            self.password_label.pack()

            self.master.geometry(f'{self.width}x{self.height + 15}')
            self.copy_button.pack(side=RIGHT)

        except ValueError:
            messagebox.showerror('Invalid Number', 'Input Valid Number')

    def resource_path(self, file_name):
        '''Get absolute path to resource from temporary directory

        In development:
            Gets path of files that are used in this script like icons, images or file of any extension from current directory

        After compiling to .exe with pyinstaller and using --add-data flag:
            Gets path of files that are used in this script like icons, images or file of any extension from temporary directory'''

        try:
            base_path = sys._MEIPASS  # PyInstaller creates a temporary directory and stores path of that directory in _MEIPASS

        except AttributeError:
            base_path = os.path.dirname(__file__)

        return os.path.join(base_path, 'assets', file_name)


if __name__ == '__main__':
    PasswordGenerator()
