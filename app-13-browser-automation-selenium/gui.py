import tkinter as tk


class Application:
    def __init__(self, root):
        self.root = root
        self.root.title('Web Automation GUI')
        self.root.geometry('350x220')
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        # Create the login frame
        tk.Label(self.login_frame, text='Username').grid(row=0, column=0, sticky='w')
        self.username_entry = tk.Entry(self.login_frame, width=20)
        self.username_entry.grid(row=0, column=1, sticky='ew')

        tk.Label(self.login_frame, text='Password').grid(row=1, column=0, sticky='w')
        self.password_entry = tk.Entry(self.login_frame, show='*', width=20)
        self.password_entry.grid(row=1, column=1, sticky='ew')

        # Form submission frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=20, pady=10)

        tk.Label(self.form_frame, text='Full Name').grid(row=0, column=0, sticky='w')
        self.full_name_entry = tk.Entry(self.form_frame, width=30)
        self.full_name_entry.grid(row=0, column=1, sticky='ew')

        tk.Label(self.form_frame, text='Email Address').grid(row=1, column=0, sticky='w')
        self.email_address_entry = tk.Entry(self.form_frame, width=30)
        self.email_address_entry.grid(row=1, column=1, sticky='ew')

        tk.Label(self.form_frame, text='Current Address').grid(row=2, column=0, sticky='w')
        self.current_address_entry = tk.Entry(self.form_frame, width=30)
        self.current_address_entry.grid(row=2, column=1, sticky='ew')

        tk.Label(self.form_frame, text='Permanent Address').grid(row=3, column=0, sticky='w')
        self.permanent_address_entry = tk.Entry(self.form_frame, width=30)
        self.permanent_address_entry.grid(row=3, column=1, sticky='ew')

        # Buttons frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=20, pady=10)

        tk.Button(self.button_frame, text='Submit', command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text='Close browser', command=self.close_window).grid(row=0, column=1, padx=5)

    def submit_data(self):
        pass

    def close_window(self):
        self.root.destroy()


root = tk.Tk()
app = Application(root)
root.mainloop()
