from flask import Flask, render_template, flash, request
from email.message import EmailMessage
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('gebruiker-request.html')

@app.route('/imail', methods=['POST'])
def imail():
    result = request.form
    
    #Gmail usage reccomended!
    sender = ""
    
    recipient = request.form['Email']
    subject = request.form['Subject']
    message = request.form['Message']
    
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(message)
    
    #Google is the easiest
    #https://pythonassets.com/posts/send-email-via-gmail-and-smtp/
    #https://support.google.com/accounts/answer/185833?hl=en
    
    smtp = smtplib.SMTP("smtp.gmail.com", port=587)
    smtp.starttls()
    smtp.login(sender, "")
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()
    
    return render_template('./gebruiker-response.html', result=result)

if __name__ == '__main__':
    app.run()