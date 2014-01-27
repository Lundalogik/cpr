import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:

	def __init__(self, email_address, articles):
		self.email_address = email_address
		self.selected_articles = articles
		self.send_mail()

	def send_mail(self):
		msg = MIMEMultipart()
		msg['From'] = 'filip.persson@.se'
		msg['To'] = 'filip.persson@.com'
		msg['Subject'] = 'simple email in python'
		message = 'here is the email'
		msg.attach(MIMEText(message))
		mailserver = smtplib.SMTP('', 587)
		print("hepp!")
		# identify ourselves to smtp gmail client
		mailserver.ehlo()
		# secure our email with tls encryption
		mailserver.starttls()
		# re-identify ourselves as an encrypted connection
		mailserver.ehlo()
		mailserver.login('', '')

		mailserver.sendmail('filip.persson@.se','filip.persson@.com',msg.as_string())

		mailserver.quit()