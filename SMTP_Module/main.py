import smtplib

my_email = "xprasoulas@gmail.com"
my_email_password = "PASSWORD"
recipient = "ispanoss@yahoo.gr"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # Encrypt the connection
    connection.starttls()
    connection.login(user=my_email, password=my_email_password)
    connection.sendmail(from_addr=my_email, to_addrs=recipient,
                        msg="Subject:This is the Subject\n\nThe body of Python message")
    connection.close()