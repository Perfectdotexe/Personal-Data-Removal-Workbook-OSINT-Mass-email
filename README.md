# Personal-Data-Removal-Workbook-OSINT-Mass-email
# Automated Data Removal Email Sender

This Python script automates the process of sending data removal requests to multiple services using a Gmail account. The script sends personalized emails to each service requesting the removal of personal information as specified in their privacy policies, following the guidelines from the book "Extreme Privacy" by Michael Bazzell.

## Features

-   **Automated Email Sending:** Sends emails to multiple services using Gmail's SMTP server.
-   **Personalized Requests:** Each email is customized with the service name and your personal information.
-   **Rate Limiting:** Includes a delay between sending emails to avoid exceeding Gmail's sending limits.
-   **Console Confirmation:** Provides real-time console output to confirm each email sent.

## Prerequisites

-   Python 3.x
-   `smtplib` and `email` libraries (install with `pip install smtplib email`)

## Setup

1.  **Enable IMAP in Gmail:**
    -   Go to Settings -> See all settings -> Forwarding and POP/IMAP.
    -   Ensure IMAP is enabled.

2.  **Allow Less Secure Apps (if needed):**
    -   Visit https://myaccount.google.com/lesssecureapps
    -   Toggle the option to allow less secure apps.

3.  **Set Up Two-Factor Authentication and Create an App Password:**
    -   Visit https://myaccount.google.com/security
    -   Enable 2-Step Verification.
    -   Create an App Password for "Mail" at https://myaccount.google.com/apppasswords

## Usage

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/yourusername/automated-data-removal-email-sender.git](https://github.com/yourusername/automated-data-removal-email-sender.git)
    cd automated-data-removal-email-sender
    ```

2.  **Configure Personal Information:**

    -   Open `email_sender.py` and replace placeholders with your information:

    ```python
    full_name = "John Doe"
    physical_address = "1234 Main St, Anytown, USA"
    telephone_number = "(555) 123-4567"
    email_address = "john.doe@example.com"
    smtp_user = "your_email@gmail.com"
    smtp_password = "your_app_password"
    ```

3.  **Run the script:**

    ```bash
    python email_sender.py
    ```

## Technical Details

-   **SMTP Configuration:** Uses Gmail's SMTP server (`smtp.gmail.com`) with port 587.
-   **Email Sending:** Utilizes `smtplib` and `email` libraries. Sends `MIMEMultipart` messages.
-   **Personalization:** Customizes email body for each service using Python string formatting.
-   **Rate Limiting:** Includes a 60-second delay between emails.
-   **Console Output:** Confirms each email sent in the console.
