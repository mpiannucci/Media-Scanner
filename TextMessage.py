import smtplib

""" Quickly send a text message to a verizon phone"""

def SendText(sender, password, number, message):
    recipient = number + '@vtext.com'
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender, recipient, message)
    server.quit()

if __name__ == "__main__":
    sender = raw_input('Email: ')
    password = raw_input('Password: ')
    number = raw_input('Phone Number: ')
    message = raw_input('Message: ')
    SendText(sender, password, recipient, message)
