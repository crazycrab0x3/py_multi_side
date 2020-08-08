try:  # Python 3.x
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox

except (ImportError, ModuleNotFoundError):  # Python 2.x
    import ttk
    from Tkinter import *
    import tkMessageBox as messagebox


class Saving_Spending:
    def __init__(self):
        self.font1, self.font2 = ('Courier', 13), ('Courier', 30)
        self.saving_file, self.spent_file = 'saving.txt', 'spending.txt'

        self.master = Tk()
        self.master.withdraw()
        self.master.after(0, self.master.deiconify)
        self.master.title('Saving & Spending')
        self.master.iconbitmap('included files\\icon.ico')
        self.master.resizable(0, 0)

        self.pos_x, self.pos_y = self.master.winfo_screenwidth() // 2 - 900 // 2, self.master.winfo_screenheight() - 650
        self.master.geometry(f'900x500+{self.pos_x}+{self.pos_y}')

        self.home_frame = Frame(self.master, bg='white')
        self.edit_window_frame = Frame(self.master, bg='white')
        self.earned_spent_frame = Frame(self.master, bg='white')
        self.add_earned_spent_frame = Frame(self.master, bg='white')
        self.home_frame.pack(ipadx=900, ipady=500)

        self.title_frame = Frame(self.home_frame, bg='White')
        self.title_label_one = Label(self.title_frame, bg='White', fg='Black', text='SAVING\n&\nSPENDING', font=self.font2, takefocus=False)
        self.title_label_one.grid(row=0, column=0)
        self.title_frame.place(x=100, y=30)

        self.label_image_frame = Frame(self.home_frame, bd=0, width=237, height=280)
        self.file_image_file = PhotoImage(file='included files\\istock.png')
        self.label_image = Label(self.label_image_frame, image=self.file_image_file, bg='blue', borderwidth=0, takefocus=False)
        self.label_image.grid(row=0, column=0)
        self.label_image_frame.place(x=3, y=200)

        self.earned_button_frame = Frame(self.home_frame)
        self.earned_button = Button(self.earned_button_frame, bd=3, bg='Red', activebackground='Red', activeforeground='white', height=3, width=60, fg='White', borderwidth=2, text='MY EARNING', cursor='hand2', command=lambda: self.show_details_window('Earned details', 'MY\n EARNING', 'save.png', self.saving_file, 'Not Earned Yet'))
        self.earned_button.grid(row=0, column=0)
        self.earned_button_frame.place(x=425, y=200)

        self.spent_button_frame = Frame(self.home_frame)
        self.spent_button = Button(self.spent_button_frame, bd=3, height=3, width=60, fg='White', bg='#01912f', activebackground='#01912f', activeforeground='white', borderwidth=2, text='MY SPENDING', cursor='hand2', command=lambda: self.show_details_window('Spent details', 'MY\nSPENDING', 'spent.png', self.spent_file, 'Not Spent Yet'))
        self.spent_button.grid(row=0, column=0)
        self.spent_button_frame.place(x=425, y=260)

        self.add_button_frame = Frame(self.home_frame)
        self.add_button = Button(self.add_button_frame, bd=3, height=3, width=60, fg='White', bg='Purple', activebackground='Purple', activeforeground='white', borderwidth=2, text='ADD SOURCE OF EARNING | EXPENDITURE', cursor='hand2', command=self.add_saving_or_spending_window)
        self.add_button.grid(row=0, column=0)
        self.add_button_frame.place(x=425, y=320)

        self.back_button_frame = Frame(self.master, bg='white')
        self.back_button_image = PhotoImage(file='included files\\back_button.png')
        self.back_button_button = Button(self.back_button_frame, image=self.back_button_image, bg='white', activebackground='white', relief=GROOVE, bd=0, cursor='hand2', takefocus=False)
        self.back_button_button.grid(row=0, column=0)

        self.master.mainloop()

    def show_details_window(self, title, text, image, file_name, yet):
        '''Displays saving or spending details'''

        self.master.title(title)
        self.home_frame.pack_forget()
        self.back_button_frame.place(x=10, y=10)
        self.earned_spent_frame.pack(ipadx=900, ipady=500)
        self.back_button_button.config(command=lambda: self.back_button_command(self.home_frame, 'Saving & Spending'))

        self.text_area_frame = Frame(self.earned_spent_frame)
        self.text_area = Text(self.text_area_frame, width=47, height=27, highlightcolor='grey', highlightthickness=2, cursor='arrow')
        self.text_area.grid(row=0, column=0)
        self.text_area_frame.place(x=450, y=50)

        self.scrollbar = Scrollbar(self.text_area_frame, orient="vertical", command=self.text_area.yview)
        self.text_area['yscrollcommand'] = self.scrollbar.set

        self.title_frame = Frame(self.earned_spent_frame, bg='White')
        self.title_label = Label(self.title_frame, text=text, bg='White', fg='Black', font=self.font2, takefocus=False)
        self.title_label.grid(row=0, column=0)
        self.title_frame.place(x=100, y=30)

        self.spent_image_frame = Frame(self.earned_spent_frame, bd=0, bg='white')
        self.spent_image = PhotoImage(file=f'included files\\{image}')
        self.spent_label_image = Label(self.spent_image_frame, image=self.spent_image, bd=0, bg='white', takefocus=False)
        self.spent_label_image.grid(row=0, column=0)
        self.spent_image_frame.place(x=10, y=220)

        self.name_image_frame = Frame(self.earned_spent_frame, bd=0)
        self.name_image = PhotoImage(file='included files\\name.png')
        self.name_label_image = Label(self.name_image_frame, image=self.name_image, bd=0, takefocus=False)
        self.name_label_image.grid(row=0, column=0)
        self.name_image_frame.place(x=460, y=10)

        self.rupee_image_frame = Frame(self.earned_spent_frame, bd=0)
        self.rupee_image = PhotoImage(file='included files\\rupees.png')
        self.rupee_label_name = Label(self.rupee_image_frame, image=self.rupee_image, bd=0, takefocus=False)
        self.rupee_label_name.grid(row=0, column=0)
        self.rupee_image_frame.place(x=715, y=10)

        self.label_frame = Frame(self.earned_spent_frame, bg='White')
        self.label_frame.place(x=480, y=250)

        contents = self.read_details(file_name)

        if contents:
            sums = 0

            for content in contents:  # If found not empty then displaying each line
                split = content.strip('\n').split(' ')
                self.text_area.insert(END, f'{split[0].ljust(35)}{split[-1]}\n')

                sums += int(split[-1])

            self.text_area.insert(END, '{}{}{}'.format('\n' * 3, 'Total: '.rjust(20), sums))

        else:
            self.label = Label(self.label_frame, bg='White', font=self.font2, text=yet, takefocus=False)
            self.label.pack(anchor='center')

        self.text_area.config(state=DISABLED)
        self.master.after(0, lambda: self.show_scrollbar(self.text_area, self.scrollbar))

    def add_saving_or_spending_window(self):
        '''Create window to enter source of spending'''

        self.home_frame.pack_forget()
        self.master.title('Add Earning | Expenditure')
        self.add_earned_spent_frame.pack(ipadx=900, ipady=500)

        self.back_button_frame.place(x=10, y=10)
        self.back_button_button.config(command=lambda: self.back_button_command(self.home_frame, 'Saving & Spending'))

        self.var_one, self.var_two, self.var_three, self.var_four, self.var_five, self.var_six = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
        self._vars = [self.var_one, self.var_two, self.var_three, self.var_four, self.var_five, self.var_six]

        self.title_frame = Frame(self.add_earned_spent_frame, bg='White')
        self.title_label = Label(self.title_frame, bg='White', fg='Black', text='ADD\nSAVING\nOR\nSPENDING'.rjust(8), font=self.font2, takefocus=False)
        self.title_label.grid(row=1, column=0)
        self.title_frame.place(x=50, y=10)

        self.spent_image_frame = Frame(self.add_earned_spent_frame, bd=0)
        self.spent_image = PhotoImage(file='included files\\earning.png')
        self.spent_label_image = Label(self.spent_image_frame, image=self.spent_image, borderwidth=0, takefocus=False)
        self.spent_label_image.grid(row=0, column=0)
        self.spent_image_frame.place(x=70, y=200)

        self.earn_frame = Frame(self.add_earned_spent_frame, bg='white', height=250, highlightthickness=1, highlightbackground='silver')
        self.earn_label = Label(self.earn_frame, padx=20, pady=20, bg='White', font=self.font1, text='Source of Money', takefocus=False)
        self.source_of_money = Entry(self.earn_frame, width=50, bg='White', highlightthickness=2, highlightbackground='silver')
        self.earn_label.grid(row=0, column=0)
        self.source_of_money.grid(row=0, column=1)
        self.earn_frame.place(x=350, y=150)

        self.entry_label = Label(self.earn_frame, padx=20, pady=20, bg='White', text='Amount', font=self.font1, takefocus=False)
        self.money_entry_box = Entry(self.earn_frame, bg='White', width=50, highlightthickness=2, highlightbackground='silver')
        self.entry_label.grid(row=1, column=0)
        self.money_entry_box.grid(row=1, column=1, padx=10)

        self.check_button_frame = Frame(self.add_earned_spent_frame)
        self.add_check_button = Checkbutton(self.check_button_frame, bd=0, text='ADD', anchor='e', bg='White', variable=self.var_one, onvalue=1, activebackground='white')
        self.del_check_button = Checkbutton(self.check_button_frame, bd=0, bg='White', anchor='w', variable=self.var_two, text='DELETE', onvalue=1, offvalue=0, padx=20, activebackground='white')
        self.add_check_button.grid(row=2, column=0, padx=0, sticky='ewns')
        self.del_check_button.grid(row=2, column=1, padx=0, sticky='ewns')
        self.check_button_frame.place(x=548, y=290)

        self.check_button_frame_two = Frame(self.add_earned_spent_frame)
        self.earn_check_button = Checkbutton(self.check_button_frame_two, bd=0, text='INCOME', anchor='e', bg='White', variable=self.var_three, onvalue=1, activebackground='white')
        self.expenditure_check_button = Checkbutton(self.check_button_frame_two, bd=0, text='SPENT', anchor='w', bg='White', variable=self.var_four, onvalue=1, activebackground='white')
        self.earn_check_button.grid(row=0, column=0)
        self.expenditure_check_button.grid(row=0, column=1)
        self.check_button_frame_two.place(x=548, y=312)

        self.delete_check_button_frame = Frame(self.add_earned_spent_frame)
        self.delete_all_button = Checkbutton(self.delete_check_button_frame, text='DELETE ALL', bg='White', variable=self.var_five, onvalue=1, activebackground='white')
        self.delete_all_button.grid(row=0, column=0)
        self.delete_check_button_frame.place(x=548, y=334)

        self.edit_frame = Frame(self.add_earned_spent_frame)
        self.edit_check_box = Checkbutton(self.edit_frame, text='EDIT', bg='White', variable=self.var_six, onvalue=1, command=self.edit_window, activebackground='white')
        self.edit_check_box.grid(row=0, column=0)
        self.edit_frame.place(x=548, y=357)

        self.submit_button = Button(self.earn_frame, height=4, width=16, fg='white', bg='#01912f', activebackground='#01912f', activeforeground='white', text='SUBMIT', font=self.font1, cursor='hand2', command=lambda: self.add_details(self.source_of_money, self.money_entry_box, self._vars))
        self.submit_button.grid(row=3, column=1, pady=11, padx=5, sticky='e')

    def edit_window(self):
        '''Create window to enter source of spending'''

        for _var in self._vars:
            _var.set(0)

        self.master.title('Edit')
        self.add_earned_spent_frame.pack_forget()
        self.back_button_frame.place(x=10, y=10)
        self.edit_window_frame.pack(ipadx=900, ipady=500)
        self.back_button_button.config(command=lambda: self.back_button_command(self.add_earned_spent_frame, 'Add Earning | Expenditure'))

        self.edit_frame = Frame(self.edit_window_frame, bd=0)
        self.edit_image = PhotoImage(file='included files\\edit.png')
        self.edit_label_image = Label(self.edit_frame, image=self.edit_image, borderwidth=0, takefocus=False)
        self.edit_label_image.grid(row=0, column=0)
        self.edit_frame.place(x=80, y=120)

        self.m_frame = Frame(self.edit_window_frame, bg='white', height=250, highlightthickness=1, highlightbackground='silver')
        self.source_label = Label(self.m_frame, padx=20, pady=20, bg='White', font=self.font1, text='Source of Money', takefocus=False)
        self.source_entry_box = Entry(self.m_frame, width=50, bg='White', highlightthickness=2, highlightbackground='silver')
        self.source_label.grid(row=0, column=0)
        self.source_entry_box.grid(row=0, column=1)
        self.m_frame.place(x=300, y=80)

        self.new_source_label = Label(self.m_frame, padx=20, pady=20, bg='White', font=self.font1, text='New Source of Money', takefocus=False)
        self.new_source_entry_box = Entry(self.m_frame, width=50, bg='White', highlightthickness=2, highlightbackground='silver')
        self.new_source_label.grid(row=1, column=0)
        self.new_source_entry_box.grid(row=1, column=1)

        self.old_money_label = Label(self.m_frame, padx=20, pady=20, bg='White', text='Old Amount', font=self.font1, takefocus=False)
        self.old_money_entry = Entry(self.m_frame, bg='White', width=50, highlightthickness=2, highlightbackground='silver')
        self.old_money_label.grid(row=2, column=0)
        self.old_money_entry.grid(row=2, column=1, padx=10)

        self.new_money_label = Label(self.m_frame, padx=20, pady=20, bg='White', text='New Amount', font=self.font1, takefocus=False)
        self.new_money_entry = Entry(self.m_frame, bg='White', width=50, highlightthickness=2, highlightbackground='silver')
        self.new_money_label.grid(row=3, column=0)
        self.new_money_entry.grid(row=3, column=1, padx=10)

        self.var = IntVar()
        self.style = ttk.Style()
        self.style.configure('R.TRadiobutton', background='white', foreground='black')

        self.radio_button_frame = Frame(self.edit_window_frame, bg='white')
        self.save_radio_buttons = ttk.Radiobutton(self.radio_button_frame, text='Saving', value=1, variable=self.var, style='R.TRadiobutton')
        self.spend_radio_buttons = ttk.Radiobutton(self.radio_button_frame, text='Spending', value=2, variable=self.var, style='R.TRadiobutton')
        self.save_radio_buttons.grid(row=0, column=0)
        self.spend_radio_buttons.grid(row=0, column=1)
        self.radio_button_frame.place(x=720, y=320)

        self.append_button = Button(self.m_frame, height=3, width=16, fg='white', bg='#01912f', activebackground='#01912f', activeforeground='white', text='APPEND', font=self.font1, command=lambda: self.edit_command(self.source_entry_box, self.new_source_entry_box, self.old_money_entry, self.new_money_entry, self.var))
        self.append_button.grid(row=4, column=1, pady=11, padx=5, sticky='e')

    def show_scrollbar(self, _text_widget, _scrollbar):
        '''show scrollbar when text is more than the text area'''

        if _text_widget.cget('height') < int(_text_widget.index('end-1c').split('.')[0]):
            scrollbar.grid(column=1, row=0, sticky=N + S)
            _text_widget.config(yscrollcommand=_scrollbar.set)
            self.master.after(100, lambda: self.hide_scrollbar(_text_widget, _scrollbar))

        else:
            self.master.after(100, lambda: self.show_scrollbar(_text_widget, _scrollbar))

    def hide_scrollbar(self, _text_widget, _scrollbar):
        '''hide scrollbar when text is less than the text area'''

        if _text_widget.cget('height') >= int(_text_widget.index('end-1c').split('.')[0]):
            _scrollbar.grid_forget()
            _text_widget.config(yscrollcommand=None)
            self.master.after(100, lambda: self.show_scrollbar(_text_widget, _scrollbar))

        else:
            self.master.after(100, lambda: self.hide_scrollbar(_text_widget, _scrollbar))

    def back_button_command(self, add_frame, title):
        '''Command when user clicks back button'''

        self.master.title(title)
        frames = [self.home_frame, self.edit_window_frame, self.earned_spent_frame, self.add_earned_spent_frame]

        if add_frame == self.home_frame:
            self.back_button_frame.place_forget()

        if add_frame == self.add_earned_spent_frame:
            self.back_button_button.config(command=lambda: self.back_button_command(self.home_frame, 'Saving & Spending'))

        for frame in frames:
            if frame != add_frame:
                frame.pack_forget()

        add_frame.pack(ipadx=900, ipady=500)

    def read_details(self, file_name):
        '''Retrive data from the given file_name'''

        try:
            with open(file_name, 'r') as f:
                lines = [line.strip('\n') for line in f.readlines()]

        except FileNotFoundError:
            lines = []

        return lines

    def write_details(self, file_name, _contents):
        '''Store data to the given file_name'''

        _contents.sort()

        with open(file_name, 'w') as f:
            for _content in _contents:
                f.write(f'{_content}\n')

    def edit_command(self, source_entry, new_source_entry, old_entry, new_entry, var):
        '''save values of edit window'''

        var_get = var.get()

        if var_get == 1:
            contents = self.read_details(self.saving_file)

        else:
            contents = self.read_details(self.spent_file)

        get_old_amount = old_entry.get().strip()
        get_new_amount = new_entry.get().strip()
        new_source = new_source_entry.get().strip()
        get_source_of_earning = source_entry.get().strip()

        if not get_source_of_earning or not get_old_amount or (not new_source and not get_new_amount):
            messagebox.showerror('ERROR', 'Some fields are left empty')

        elif not get_old_amount.isdigit() or (not get_new_amount.isdigit() and not get_old_amount):
            messagebox.showerror('ERROR', 'Money must be in number')

        elif var_get not in [1, 2]:
            messagebox.showerror('ERROR', 'No Buttons\nwere selected')

        else:
            success = False
            content = f'{get_source_of_earning.ljust(50)}{get_old_amount}'

            if content in contents:
                success = True
                index = contents.index(content)

                if get_new_amount:
                    get_old_amount = get_new_amount

                if new_source:
                    get_source_of_earning = new_source

                if var_get == 1:
                    file_name = self.saving_file

                else:
                    file_name = self.spent_file

                contents[index] = f'{get_source_of_earning.ljust(50)}{get_old_amount}'

            if success:
                self.write_details(file_name, contents)

                var.set(0)

                for _entry in [old_entry, new_entry, source_entry, new_source_entry]:
                    _entry.delete(0, END)

                messagebox.showinfo('ADDED', 'Value Added to the file')
                self.master.focus()

            else:
                messagebox.showerror('NOT FOUND', 'Value not found in file')

    def add_details(self, source_entry, money_entry, _vars):
        '''Add details to the file'''

        success = False
        get_money_earned = money_entry.get().strip()
        get_source_of_earning = source_entry.get().title().strip()

        values = [var.get() for var in _vars]
        count_values = len([value for value in values if value == 1])
        content = f'{get_source_of_earning.ljust(50)}{get_money_earned}'

        if values[2] == 1:
            contents = self.read_details(self.saving_file)

        elif values[3] == 1:
            contents = self.read_details(self.spent_file)

        if not get_source_of_earning and values[-2] == 0:
            messagebox.showerror('Invalid Source', 'Source of money is not given')

        elif not get_money_earned and values[-2] == 0:
            messagebox.showerror('Invalid Money', 'Amount of money is not given')

        elif not get_money_earned.isdigit() and values[-2] == 0:
            messagebox.showerror('Invalid Money', 'Amount of money must be in numbers')

        elif not((values[0] == values[2] == 1) or (values[0] == values[3] == 1) or (values[1] == values[2] == 1) or (values[1] == values[3] == 1) or values[4] == 1) or count_values > 2:
            error = f'''You must select checkbutton in the following ORDER:
        EDIT                            = Opens Edit Window
        DELETE ALL                 = Delete all values from both files
        ADD + SPENT             = Add data in {self.spent_file}
        ADD + INCOME         = Add data in {self.saving_file}
        DELETE + SPENT        = Delete a value from {self.spent_file}
        DELETE + INCOME     = Delete a value from {self.saving_file}'''

            messagebox.showerror('Invalid Combination', error)

        elif (values[0] == values[2] == 1) or (values[0] == values[3] == 1):  # When (Add and Income) or (Add and Spent) checkbutton is selected
            if content not in contents:
                if values[2] == 1:
                    file_name = self.saving_file

                elif values[3] == 1:
                    file_name = self.spent_file

                success = True
                contents.append(content)
                messagebox.showinfo('ADDED', 'Value added to the file.')
                self.write_details(file_name, contents)

            else:
                messagebox.showerror('Already Exists', 'Value already exists in the file.')

        elif (values[1] == values[2] == 1) or (values[1] == values[3] == 1):  # When (Delete and Income) or (Delete and Spend) checkbutton is selected
            if content in contents:
                if values[2] == 1:
                    file_name = self.saving_file

                elif values[3] == 1:
                    file_name = self.spent_file

                success = True
                contents.remove(content)
                messagebox.showinfo('REMOVED', 'Value removed from the file.')
                self.write_details(file_name, contents)

            else:
                messagebox.showerror('Not Found', 'Value not found in the file.')

        elif values[4] == 1:   # When delete all button is selected:
            success = True

            for file_name in [self.saving_file, self.spent_file]:
                self.write_details(file_name, '')

            messagebox.showinfo('DELETED ALL', 'All values are deleted.')

        if success:
            source_entry.delete(0, END)
            money_entry.delete(0, END)

            for _var in _vars:
                _var.set(0)

            self.master.focus()


if __name__ == '__main__':
    Saving_Spending()
