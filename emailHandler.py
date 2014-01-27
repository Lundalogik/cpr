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
		msg['From'] = 'filip.persson@lundalogik.se'
		msg['To'] = 'filip.persson@me.com'
		msg['Subject'] = 'simple email in python'
		message = 'here is the email'
		msg.attach(MIMEText(message))
		mailserver = smtplib.SMTP('lundalogik.se', 587)
		print("hepp!")
		# identify ourselves to smtp gmail client
		mailserver.ehlo()
		# secure our email with tls encryption
		mailserver.starttls()
		# re-identify ourselves as an encrypted connection
		mailserver.ehlo()
		mailserver.login('fpe', '3LimePaj?')

		mailserver.sendmail('filip.persson@lundalogik.se','filip.persson@me.com',msg.as_string())

		mailserver.quit()