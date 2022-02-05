import smtplib

my_email = "your_email"
my_password = "your_password"
my_smtp = "your.smtp.com"
my_port = 0
receiver = "receiving_email_address"
subject = "today's weather information"


def send_mail(message, subject_add=""):
    """Connects to and sends E-Mail"""
    with smtplib.SMTP(my_smtp, port=my_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver,
                            msg=f"Subject:{subject} {subject_add}\n\n{message}")
