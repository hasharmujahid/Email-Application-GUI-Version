"""WRITE YOUR CODE HERE! """
""""Import SMTPLIB Libraray"""

from tkinter import *

"""create gloabal variables for email and passwords"""



global email_adress
global password
global receptent
global Subject
global body

#
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
            password = str(Account_password.get())
            email_adress = str(Account_name.get())
            print(email_adress)
            Enter.destroy()
            next_button.place(relx=0.6, rely=0.6, anchor=CENTER)

        Enter = Button(text="Authorize", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                       command=proceed)
        Enter.place(relx=0.6, rely=0.6, anchor=CENTER)
        cancle.place(relx=0.4, rely=0.6, anchor=CENTER)

        def menu():
            next_button.destroy()
            Label_account_name.destroy()
            Label_account_password.destroy()
            Account_password.destroy()
            Account_name.destroy()
            root.title(str(email_adress))
            cancle.place(relx=0.25, rely=0.45, anchor=CENTER)
            Emails_recieved.place(relx=0.48, rely=0.45, anchor=CENTER)
            Send_email.place(relx=0.745, rely=0.45, anchor=CENTER)

        next_button = Button(text="Proceed", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                             command=menu)


    def recieved_mails():
        import webbrowser
        webbrowser.open("https://mail.google.com/")


    def Send_to():
        Emails_recieved.destroy()
        Send_email.destroy()
        cancle.place(relx=0.10, rely=0.85, anchor='n')
        Receptant_lable = Label(root, text="Enter receptent's Email Adress")
        Receptant_lable.place(relx=0.46, rely=0.2, anchor=CENTER)
        receptent_account = Entry(root, width=35, borderwidth=4)
        receptent_account.place(relx=0.5, rely=0.28, anchor=CENTER)

        def Authorize():
            global receptent
            receptent = str(receptent_account.get())
            Auth_button.destroy()
            Receptant_lable.destroy()
            receptent_account.destroy()
            print(receptent)
            send_message.place(relx=0.45, rely=0.45, anchor=CENTER)

        Auth_button = Button(text="Authorize", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                             command=Authorize)
        Auth_button.place(relx=0.45, rely=0.45, anchor=CENTER)


    def write_message():
        send_message.destroy()
        Subject_lable = Label(root, text="Enter Subject")
        Subject_lable.place(relx=0.38, rely=0.2, anchor=CENTER)
        Subject_write = Entry(root, width=35, borderwidth=4)
        Subject_write.place(relx=0.5, rely=0.28, anchor=CENTER)
        message_Lable = Label(root, text="Enter Message")
        message_Lable.place(relx=0.38, rely=0.37, anchor=CENTER)
        message_write = Entry(root, width=35, borderwidth=4)
        message_write.place(relx=0.5, rely=0.46, anchor=CENTER)

        def Authorize():
            global Subject
            Subject = str(Subject_write.get())
            print(Subject)
            global body
            body = str(message_write.get())
            print(body)
            message_write.destroy()
            message_Lable.destroy()
            Subject_write.destroy()
            Subject_lable.destroy()
            auth_button_for_write_msg.destroy()
            last_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        auth_button_for_write_msg = Button(text="Confirm Message", padx=30, pady=15, fg='black', bg="grey",
                                           font=("Consolas 10 bold"), command=Authorize)
        auth_button_for_write_msg.place(relx=0.49, rely=0.62, anchor=CENTER)


    def sending_email():
        import smtplib
        last_button.destroy()
        FROM = email_adress
        TO = receptent
        SUBJECT = Subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(email_adress, password)
            server.sendmail(FROM, TO, message)
            server.close()
            print('successfully sent the mail')
            conformation_lable = Label(root, text="Successfully Sent...",font=("Consolas 20 bold"))
            conformation_lable.place(relx=0.5, rely=0.5, anchor=CENTER)
        except:
            conformation_lable = Label(root, text="Failed...")
            conformation_lable.place(relx=0.5, rely=0.5, anchor=CENTER)


    """BUTTONS"""
    signin = Button(text="Sign in", padx=40, pady=20, fg='black', bg="grey", font=("Consolas 12 bold"), command=sign_in)
    signin.place(relx=0.6, rely=0.5, anchor=CENTER)
    signup = Button(text="Sign up", padx=40, pady=20, fg='black', bg="grey", font=("Consolas 12 bold"), command=sign_up)
    signup.place(relx=0.3, rely=0.5, anchor=CENTER)
    cancle = Button(text="Exit", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"), command=exit)

    """"MENU BUTTONS"""
    Emails_recieved = Button(text="Recieved Mails", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                             command=recieved_mails)
    Send_email = Button(text="Send Mails", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                        command=Send_to)
    send_message = Button(text="Write Message", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                          command=write_message)
    last_button = Button(text="SEND", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                         command=sending_email)
    root.mainloop()
