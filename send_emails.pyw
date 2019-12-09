import smtplib
import config

def send_emails(subject, msg):

  try:
    # finds the server for email
    server = smtplib.SMTP('smtp.gmail.com:587')
    # print("1")
    server.ehlo()
    # print("2")
    server.starttls()
    # print("3")
    # logs into the gmail account
    server.login(config.ADDRESS, config.PASSWORD)
    print("I got to login")
    # types the message
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    # sends the email
    server.sendmail(config.ADDRESS, config.ADDRESS, message)
    # exits the server
    server.quit()
    print("Email successfully sent.")
  except:
    print("Email failed to send.")

# sbj = input("Enter the subjet of the email: ")
# msg = input("Enter the message of the email: ")
sbj = 't'
msg = 'falkjfla'
send_emails(sbj, msg)