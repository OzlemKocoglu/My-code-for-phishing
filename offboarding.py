import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Account information
from_email = "okocoglu07@gmail.com"
app_password = "xoyikubfdzmeibmd"

# Recipient email
to_email = "ozlem.kocoglu@midiagnostics.com"

# Email text
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = "Offboarding"
body = "'Beste Özlem,\n\nWij willen je informeren dat je vanaf morgen niet langer bij ons bedrijf werkt. Gelieve alle bedrijfseigendommen terug te geven en eventuele openstaande taken af te ronden.\n\nBedankt voor je bijdrage aan ons bedrijf.\n\nMet vriendelijke groet,\nHR team'"
msg.attach(MIMEText(body, 'plain'))

# Send email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, app_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    print('Email sent successfully.')
except Exception as e:
    print('Something went wrong...', e)
finally:
    server.quit()
