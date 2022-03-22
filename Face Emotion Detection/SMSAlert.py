import smtplib
from email.message import EmailMessage


def email_alert(to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "smsalertpython@gmail.com"
    msg['from'] = user
    password = 'hbsaoiiukctvxbqc'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


# if __name__ == '__main__':
#     email_alert("YOUR_MAIL_ID", "Subject", "Message")
    # email_alert("918870218203@airtelap.com", "Hello man", "Its working")

    # email_alert("918870218203@airtelkk.com", "Hello man", "Now Its working")

    # email_alert("9198948870218203@airtelmobile.com", "Hello man",
    #             "Now Its working 919894number@airtelmobile.com")

    # email_alert("918870218203@airtelchennai.com", "Hello man",
    #             "Now Its working airtelchennai")
