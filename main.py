import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_ya_mail(recipients_emails: list, msg_text: str):
    login = "&&&&&&&@yandex.ru"
    password = "*(^%$##9gsve"

    msg = MIMEText(f"{msg_text}", "plain", "utf-8")
    msg["Subject"] = Header("Важно!", "utf-8")
    msg["From"] = login
    msg["To"] = ", ".join(recipients_emails)

    s = smtplib.SMTP("smtp.yandex.ru", 587, timeout=10)

    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg["From"], recipients_emails, msg.as_string())
    except Exception as ex:
        print(ex)
    finally:
        s.quit()


def main():
    send_ya_mail(["******@mail.ru", "^^^^^^@gmail.com"], "Hi, it is great!")


if __name__ == "__main__":
    main()
