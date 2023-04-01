from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import datetime


class Emailer:
    def __init__(self, me='regentmarlin537@gmail.com', password='gmat34spicy', server_='smtp.gmail.com:587',
                 you='rakeenrouf@gmail.com'):
        self.me = me
        self.password = password
        self.server = server_
        self.you = you

    def send_email(self, data, custom, subject):
        text = """
        Hello, Friend.

        All stats as of: {now}:

        {custom}

        {table}

        Regards,

        Me"""

        html = """
        <html><head><style> 
          table, th, td {{ border: 1px solid black; border-collapse: collapse; }}
          th, td {{ padding: 5px; }}
        </style></head><body>
        <p>All stats as of: {now}:

        {custom}

        </p>
        {table}
        <p>Regards,</p>
        <p>Me</p>
        </body></html>
        """

        table_1 = tabulate(data, headers="firstrow", tablefmt="grid")
        table_2 = tabulate(data, headers="firstrow", tablefmt="html")
        akhon = datetime.now()
        text = text.format(table=table_1, now=akhon, custom=custom)
        html = html.format(table=table_2, now=akhon, custom=custom)

        message = MIMEMultipart(
            "alternative", None, [MIMEText(text), MIMEText(html, 'html')])

        message['Subject'] = f"{subject} {akhon}"
        message['From'] = self.me
        message['To'] = self.you
        server = smtplib.SMTP(self.server)
        server.ehlo()
        server.starttls()
        server.login(self.me, self.password)
        server.sendmail(self.me, self.you, message.as_string())
        server.quit()


if __name__ == '__main__':
    mailer = Emailer()
