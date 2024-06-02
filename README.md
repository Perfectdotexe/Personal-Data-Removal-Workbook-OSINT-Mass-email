# Personal-Data-Removal-Workbook---OSINT-Mass-email
This Python script automates the process of sending data removal requests to multiple services using a Gmail account. The script sends personalized emails to each service requesting the removal of personal information as specified in their privacy policies, following the guidelines from the "Extreme Privacy" book by Michael Bazzell.

Features
Automated Email Sending: Sends emails to multiple services using Gmail's SMTP server.
Personalized Requests: Each email is customized with the service name and your personal information.
Rate Limiting: Includes a delay between sending emails to avoid exceeding Gmail's sending limits.
Console Confirmation: Provides real-time console output to confirm each email sent.
Prerequisites
Python 3.x: Ensure Python is installed on your system.
Required Libraries: Install the necessary Python libraries using the following command:
pip install smtplib email
Setup
Enable SMTP for Gmail:

Log in to your Gmail account.
Go to Settings -> See all settings -> Forwarding and POP/IMAP.
Ensure IMAP is enabled and save changes.
Allow Less Secure Apps (if needed):

Visit Allow less secure apps: https://myaccount.google.com/lesssecureapps
Toggle the option to allow less secure apps.
Set Up Two-Factor Authentication (recommended) and Create an App Password:

Visit Google Account Security: https://myaccount.google.com/security
Enable 2-Step Verification if not already enabled.
Create an App Password for "Mail" by visiting App Passwords: https://myaccount.google.com/apppasswords
Usage
Clone the Repository:
git clone https://github.com/yourusername/automated-data-removal-email-sender.git
cd automated-data-removal-email-sender

Configure Personal Information:
Open the script file email_sender.py and replace the placeholders with your actual information:
full_name = "John Doe"
physical_address = "1234 Main St, Anytown, USA"
telephone_number = "(555) 123-4567"
email_address = "john.doe@example.com"
smtp_user = "your_email@gmail.com"
smtp_password = "your_app_password"

Run the Script:
Execute the script to start sending emails:
python email_sender.py

Technical Details
SMTP Configuration: The script uses Gmail's SMTP server (smtp.gmail.com) with port 587 for sending emails.
Email Sending: The script uses the smtplib and email libraries to send emails. Each email is sent using a MIMEMultipart message to include both plain text and potentially HTML content.
Personalization: The email body is customized for each service using Python string formatting.
Rate Limiting: A time.sleep(60) delay is included between sending each email to ensure that the Gmail account's sending limits are not exceeded.
Console Output: Each email sent is confirmed with a print statement in the console, providing real-time feedback to the user.
