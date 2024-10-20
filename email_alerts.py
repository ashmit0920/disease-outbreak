import smtplib
from email.message import EmailMessage
import os

def send_alert(email):
    EMAIL_ADDRESS = 'ashmitthawait2@gmail.com'
    EMAIL_PASSWORD = os.getenv("EMAIL_PWD")

    msg = EmailMessage()
    msg['Subject'] = 'Outbreak Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg.set_content('''
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style type="text/css">
            h1{font-size:56px}
            h2{font-size:32px; font-weight:900}
            p{font-size:28px; font-weight:400}
            td{vertical-align:top}
            #email{margin:auto;width:600px;background-color:#fff}
            </style>
        </head>
        <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
        <div id="email">
            <table role="presentation" width="100%">
                <tr>
                    <td bgcolor="#12086F" align="center" style="color: white;">
                        <h1> Epidemic Control Dept</h1>
                    </td>
            </table>
            <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
                <tr>
                    <td>
                        <h2>Outbreak alert</h2>
                        <p>
                            Our system has detected high chances of a <b>Malaria Outbreak</b> in your region. Kindly take appropriate precautions to stay safe!
                        </p>
                    </td>
                </tr>
            </table>
        </div>
        </body>
        </html>
    ''', subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
