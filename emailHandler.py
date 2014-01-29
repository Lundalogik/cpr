import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:
    def __init__(self,email, articles):
        print(email)
        self.email = email
        self.selected_articles = articles
        self.send_mail()

    def send_mail(self):
        msg = MIMEMultipart()
        msg['From'] = self.email['from_address']
        msg['To'] = self.email['to_address']
        msg['Subject'] = 'All din info'
       
        part1 = MIMEText(self.build_text_body(), 'plain')
        part2 = MIMEText(self.build_html_body(), 'html')

        msg.attach(part1)
        msg.attach(part2)

        mailserver = smtplib.SMTP(self.email['server'], 587)
        # identify ourselves to smtp client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login(self.email['user'], self.email['password'])

        mailserver.sendmail(self.email['from_address'],self.email['to_address'], msg.as_string())

        mailserver.quit()

    def build_html_body(self):
        html= """\
            <html>
              <head></head>
              <body>
        """
        for idx, article in enumerate(self.selected_articles['articles']):           
            html += "<div style='background-color:" + article['link'] +"'>"
            html += "<h1>" + article['title']+ "</h1>"
            html += "<p>" + article['body'] + "</p>"
            html += "<a href='" + article['link'] + "'>Läs mer!</a>"
            html += "</div>"
        html += """\
              </body>
            </html>
        """
        print(html)
        return html

    def build_text_body(self):
        return "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
