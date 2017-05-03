import multiprocessing
import smtplib
import time
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

me = "your_email_address@gmail.com"
pwd = "your_password"
you = "receiver_address@gmail.com"

class send_email(multiprocessing.Process):

    def __init__(self, inputQ, outputQ, stopEvent):
        multiprocessing.Process.__init__(self)
        self.inputQ = inputQ
        self.outputQ = outputQ
        self.stopEvent = stopEvent

    def run(self):
        while not self.stopEvent.is_set():
            while not self.inputQ.empty():
                file = "videos/test_sample.mov"
                msg = MIMEMultipart('alternative')
                msg['From'] = me
                msg['To'] = you
                gmail_user = me
                gmail_pwd = pwd

                if inputQ["event_type"] == "fast_movement":
                    msg['Subject'] = 'Alarm from healthsensorsolutions! Someone looks like have a fast movement'
                elif inputQ["event_type"] == "breathing_stopped":
                    msg['Subject'] = 'Alarm from healthsensorsolutions! Someone looks like stopping breathing'
                html = """
                <html>
                <body>
                Hurry up. Please check the video attached in the email. Someone probably need your help!"
                </body>
                </html>
                """
                part1 = MIMEText(html, 'html')
                msg.attach(part1)
                with open(file, 'rb') as file:
                    part2 = MIMEApplication(file.read())
                    part2['Content-Disposition'] = 'attachment; filename="test_sample.mov"'
                    msg.attach(part2)
                try:
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.ehlo()
                    s.starttls()
                    s.login(gmail_user, gmail_pwd)
                    s.sendmail(me, [you], msg.as_string())
                    s.close()
                    endtime = time.time()
                    print 'Successfully sent the email at'
                except:
                    print 'Failed to send the email'
