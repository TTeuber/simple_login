from tkinter import *

info = dict()


def register_window():
    root = Tk()
    root.title("Register")
    root.geometry("300x400")
    root.resizable(FALSE, FALSE)

    frame_1 = Frame(root, width=300, height=150)
    frame_1.pack()
    frame_2 = Frame(root, width=300, height=150)
    frame_2.pack()
    frame_3 = Frame(root, width=300, height=100)
    frame_3.pack()

    register_label = Label(frame_1, text="Register",
                           font=("futura", 50), pady=40, anchor=N)
    register_label.grid(row=0, column=1, columnspan=2)

    email_label = Label(frame_2, text="Email", font=("futura", 20))
    email_label.pack()
    email_entry = Entry(frame_2)
    email_entry.pack()

    username_label = Label(frame_2, text="Username", font=("futura", 20))
    username_label.pack()
    username_entry = Entry(frame_2)
    username_entry.pack()

    password_label = Label(frame_2, text="Password", font=("futura", 20))
    password_label.pack()
    password_entry = Entry(frame_2)
    password_entry.pack()

    def get_submit():
        global info
        if username_entry.get() not in info:
            info.update({username_entry.get(): (
                email_entry.get(), password_entry.get())})
            username_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
        else:
            username_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            username_entry.insert(0, "username taken")

    submit_button = Button(frame_3, text="Submit", command=get_submit)
    submit_button.grid(row=0, column=0)

    def login_switch():
        root.destroy()
        login_window()

    login_button = Button(frame_3, text="Login", command=login_switch)
    login_button.grid(row=0, column=1)

    root.mainloop()


def login_window():
    root = Tk()
    root.geometry("300x400")
    root.title('Login')
    root.resizable(FALSE, FALSE)

    frame_1 = Frame(root, width=300, height=150)
    frame_1.pack()
    frame_2 = Frame(root, width=300, height=150)
    frame_2.pack()
    frame_3 = Frame(root, width=300, height=100)
    frame_3.pack()

    login_label = Label(frame_1, text="Login", font=(
        "futura", 50), pady=40, anchor=N)
    login_label.grid(row=0, column=1, columnspan=2)

    username_label = Label(frame_2, text="Username", font=("futura", 20))
    username_label.pack()
    username_entry = Entry(frame_2)
    username_entry.pack()

    password_label = Label(frame_2, text="Password", font=("futura", 20))
    password_label.pack()
    password_entry = Entry(frame_2)
    password_entry.pack()

    def register_switch():
        root.destroy()
        register_window()

    register_button = Button(frame_3, text="Register", command=register_switch)
    register_button.grid(column=0)

    def log_in():
        global info
        if username_entry.get() in info:
            if info[username_entry.get()][1] == password_entry.get():
                root.destroy()
                logged_in_window()
            else:
                password_entry.delete(0, END)
                password_entry.insert(0, "invalid password")
        else:
            username_entry.delete(0, END)
            username_entry.insert(0, "Username not found")
            password_entry.delete(0, END)

    login_button = Button(frame_3, text="Login", command=log_in)
    login_button.grid(row=0, column=1)

    root.mainloop()


def logged_in_window():
    root = Tk()
    root.geometry("300x400")
    root.title('Logged In')
    root.resizable(FALSE, FALSE)

    frame_1 = Frame(root, width=300, height=150)
    frame_1.pack()
    frame_2 = Frame(root, width=300, height=150)
    frame_2.pack()
    frame_3 = Frame(root, width=300, height=100)
    frame_3.pack()

    login_label = Label(frame_1, text="Logged In",
                        font=("futura", 50), pady=40, anchor=N)
    login_label.grid(row=0, column=1, columnspan=2)

    def logout():
        root.destroy()
        login_window()

    logout_button = Button(frame_3, text="Log Out", command=logout)
    logout_button.pack()

    root.mainloop()


register_window()
