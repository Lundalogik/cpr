import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:

	def __init__(self,email_server_address, email_server_user, email_server_password, to_email_address, from_email_address, articles):
		self.email_server = email_server_address
		self.email_server_user = email_server_user
		self.email_server_password = email_server_password
		self.to_email_address = to_email_address
		self.from_email_address = from_email_address
		self.selected_articles = articles
		self.send_mail()

	def send_mail(self):
		msg = MIMEMultipart()
		msg['From'] = self.from_email_address
		msg['To'] = self.to_email_address
		msg['Subject'] = 'Hello from Python!'
		message = 'here is the email'
		msg.attach(MIMEText(message))
		mailserver = smtplib.SMTP(self.email_server, 587)
		# identify ourselves to smtp client
		mailserver.ehlo()
		# secure our email with tls encryption
		mailserver.starttls()
		# re-identify ourselves as an encrypted connection
		mailserver.ehlo()
		mailserver.login(self.email_server_user, self.email_server_password)

		mailserver.sendmail(self.to_email_address,self.from_email_address,msg.as_string())

		mailserver.quit()