import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:

<<<<<<< HEAD
	def __init__(self, email_address, articles):
		self.email_address = email_address
=======
	def __init__(self,email_server_address, email_server_user, email_server_password, to_email_address, from_email_address, articles):
		self.email_server = email_server_address
		self.email_server_user = email_server_user
		self.email_server_password = email_server_password
		self.to_email_address = to_email_address
		self.from_email_address = from_email_address
>>>>>>> 8112fb078934660adb1eb886dcbafc85ce7592c2
		self.selected_articles = articles
		self.send_mail()

	def send_mail(self):
		msg = MIMEMultipart()
<<<<<<< HEAD
		msg['From'] = 'filip.persson@.se'
		msg['To'] = 'filip.persson@.com'
		msg['Subject'] = 'simple email in python'
		message = 'here is the email'
		msg.attach(MIMEText(message))
		mailserver = smtplib.SMTP('', 587)
		print("hepp!")
		# identify ourselves to smtp gmail client
=======
		msg['From'] = self.from_email_address
		msg['To'] = self.to_email_address
		msg['Subject'] = 'Hello from Python!'
		message = 'here is the email'
		msg.attach(MIMEText(message))
		mailserver = smtplib.SMTP(self.email_server, 587)
		# identify ourselves to smtp client
>>>>>>> 8112fb078934660adb1eb886dcbafc85ce7592c2
		mailserver.ehlo()
		# secure our email with tls encryption
		mailserver.starttls()
		# re-identify ourselves as an encrypted connection
		mailserver.ehlo()
<<<<<<< HEAD
		mailserver.login('', '')

		mailserver.sendmail('filip.persson@.se','filip.persson@.com',msg.as_string())
=======
		mailserver.login(self.email_server_user, self.email_server_password)

		mailserver.sendmail(self.to_email_address,self.from_email_address,msg.as_string())
>>>>>>> 8112fb078934660adb1eb886dcbafc85ce7592c2

		mailserver.quit()