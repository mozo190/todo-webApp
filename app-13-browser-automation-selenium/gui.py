import tkinter as tk


class Application:
    def __init__(self, root):
        self.root = root
        self.root.title('Web Automation GUI')
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text='Username').grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text='Password').grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1)

    def submit_data(self):
        pass

    def close_window(self):
        pass


root = tk.Tk()
app = Application(root)
root.mainloop()
