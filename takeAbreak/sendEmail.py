import smtplib, ssl

# SSL port
port = 465

# Your credentials
yourEmail = input("Please enter your email: ")
pwd = input('Enter password: ')
message = input('Enter your message')
targetEMail = input("Please enter target email")
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login(yourEmail, pwd)
    server.sendmail(yourEmail, targetEMail, message)