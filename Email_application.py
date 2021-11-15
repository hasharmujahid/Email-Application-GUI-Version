"""WRITE YOUR CODE HERE! """
""""Import SMTPLIB Libraray"""

import smtplib
from tkinter import *

"""create gloabal variables for email and passwords"""
global email_adress
global password


class Email_strcure:
    pass


if __name__ == '__main__':
    """MAIN SCREEN"""
    root = Tk()
    root.geometry("600x400")
    root.title("Email")
    root.iconbitmap("icon.ico")
    root.configure(background='grey')
    """placing buttons"""

    """FUNCTIONS"""


    def sign_up():
        import webbrowser
        webbrowser.open(
            "https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp")


    def sign_in():
        signin.destroy()
        signup.destroy()
        Label_account_name = Label(root, text='Email Adress')
        Label_account_name.place(relx=0.38, rely=0.2, anchor=CENTER)
        Account_name = Entry(root, width=35, borderwidth=4)
        Account_name.place(relx=0.5, rely=0.28, anchor=CENTER)
        Label_account_password = Label(root, text='Password')
        Label_account_password.place(relx=0.37, rely=0.37, anchor=CENTER)
        Account_password = Entry(root, width=35, borderwidth=4)
        Account_password.place(relx=0.5, rely=0.46, anchor=CENTER)

        def proceed():
            global password
            global email_adress
            password=str(Account_password.get())
            email_adress=str(Account_name.get())
            print(email_adress)

        Enter = Button(text="Proceed", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                       command=proceed)
        Enter.place(relx=0.6, rely=0.6, anchor=CENTER)
        cancle.place(relx=0.4, rely=0.6, anchor=CENTER)
    """BUTTONS"""
    signin = Button(text="Sign in", padx=40, pady=20, fg='black', bg="grey", font=("Consolas 12 bold"), command=sign_in)
    signup = Button(text="Sign up", padx=40, pady=20, fg='black', bg="grey", font=("Consolas 12 bold"), command=sign_up)
    cancle = Button(text="Exit", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"), command=exit)


    signup.place(relx=0.3, rely=0.5, anchor=CENTER)
    signin.place(relx=0.6, rely=0.5, anchor=CENTER)
    root.mainloop()
