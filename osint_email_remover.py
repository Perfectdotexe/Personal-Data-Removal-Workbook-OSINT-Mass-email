import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# SMTP Configuration for Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "your_email@gmail.com"
smtp_password = "your_app_password"  # Use an App Password if you have 2FA enabled

# Personal Information (to be filled by the programmer)
full_name = "John Doe"
physical_address = "1234 Main St, Anytown, USA"
telephone_number = "(555) 123-4567"
email_address = "john.doe@example.com"

# Email Template
subject = "Request for Data Removal"
body_template = """
Dear {service_name},

I have been unsuccessful in removing my personal information from your website. Per the information provided from 
your legal privacy policy, please remove the following details from your service.

Full Name: {full_name}
Physical Address: {physical_address}
Telephone Number: {telephone_number}
Email Address: {email_address}

Thank you for your attention to this matter.

Sincerely,
{full_name}
"""

# List of services and their email addresses
email_list = [
    {"service_name": "411.com", "email": "support@whitepages.com"},
    {"service_name": "411.info", "email": "support@411.info"},
    {"service_name": "411.info", "email": "admin@411.info"},
    {"service_name": "Absolute People Search", "email": "support@absolutepeoplesearch.com"},
    {"service_name": "Addresses", "email": "support@addresses.com"},
    {"service_name": "Addresses", "email": "support@mailer.intelius.com"},
    {"service_name": "Address Search", "email": "support@addresssearch.com"},
    {"service_name": "Advanced Background Checks", "email": "support@advancedbackgroundchecks.com"},
    {"service_name": "Advanced People Search", "email": "support@advanced-people-search.com"},
    {"service_name": "All Area Codes", "email": "support@allareacodes.com"},
    {"service_name": "All People", "email": "webmaster@allpeople.com"},
    {"service_name": "America Phonebook", "email": "lookupuk@gmail.com"},
    {"service_name": "Anywho", "email": "ypcsupport@yp.com"},
    {"service_name": "Anywho", "email": "press@yp.com"},
    {"service_name": "Ancestry", "email": "support@ancestry.com"},
    {"service_name": "Ancestry", "email": "customersolutions@ancestry.com"},
    {"service_name": "Archives", "email": "privacy@archives.com"},
    {"service_name": "Apollo", "email": "support@apollo.io"},
    {"service_name": "Arivify", "email": "hello@arivify.com"},
    {"service_name": "Arrest Facts", "email": "support@arrestfacts.com"},
    {"service_name": "Azerch", "email": "support@azerch.com"},
    {"service_name": "Background Alert", "email": "customerservice@backgroundalert.com"},
    {"service_name": "Background Check", "email": "support@backgroundcheck.run"},
    {"service_name": "Background Checkers", "email": "support@backgroundcheckers.net"},
    {"service_name": "BatchSkipTracing", "email": "support@batchskiptracing.com"},
    {"service_name": "BatchLeads", "email": "support@batchleads.io"},
    {"service_name": "BatchDialer", "email": "support@batchdialer.com"},
    {"service_name": "BatchDriven", "email": "support@batchdriven.com"},
    {"service_name": "Been Verified", "email": "privacy@beenverified.com"},
    {"service_name": "BlockShopper", "email": "scarlett@blockshopper.com"},
    {"service_name": "Buzzfile", "email": "info@buzzfile.com"},
    {"service_name": "Call Revealer", "email": "support@callrevealer.com"},
    {"service_name": "Call Truth", "email": "support@calltruth.com"},
    {"service_name": "Caller Smart", "email": "support@callersmart.com"},
    {"service_name": "Callyo", "email": "callyo.support@motorolasolutions.com"},
    {"service_name": "Cars Owners", "email": "lookupuk@gmail.com"},
    {"service_name": "Catalog Choice", "email": "support@catalogchoice.org"},
    {"service_name": "Centeda", "email": "support@centeda.com"},
    {"service_name": "Check People", "email": "support@checkpeople.com"},
    {"service_name": "Check Secrets", "email": "support@checksecrets.com"},
    {"service_name": "Checkr", "email": "support@checkr.com"},
    {"service_name": "City-Data", "email": "others@city-data.com"},
    {"service_name": "City-Data", "email": "legal@city-data.com"},
    {"service_name": "ClickSearch", "email": "support@clicksearch.us"}
]

# Function to send email
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())

# Loop through the email list and send emails
for entry in email_list:
    service_name = entry['service_name']
    to_email = entry['email']
    body = body_template.format(
        service_name=service_name,
        full_name=full_name,
        physical_address=physical_address,
        telephone_number=telephone_number,
        email_address=email_address
    )
    
    send_email(to_email, subject, body)
    print(f"Email sent to {service_name} ({to_email})")
    time.sleep(60)  # Wait for 60 seconds before sending the next email

print("All emails have been sent.")