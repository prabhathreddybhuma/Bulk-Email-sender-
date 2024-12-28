Bulk Email Sender 📧

A simple and efficient tool to send bulk emails using a pre-designed email template. This project is designed to help users send personalized emails in bulk, making it perfect for marketing campaigns, event notifications, newsletters, or any situation requiring mass email distribution.

Features ✨

Bulk Email Sending: Send emails to multiple recipients at once 📤
Personalization: Include personalized details (such as recipient names) in each email ✉️
Email Templates: Use a pre-designed email template for formatting the message 📑
SMTP Integration: Uses SMTP server to send emails securely 🔒
Email Status Tracking: Track the status of emails sent (success or failure) ✅❌
Error Handling: Provides error messages for failed email deliveries ⚠️
Requirements ⚙️

Python 3.x: Ensure Python is installed on your machine 🐍
Libraries: Install the required libraries using pip:
pip install smtplib email-validator
Installation 🛠️

Clone the repository:
git clone https://github.com/prabhathreddybhuma/Bulk-Email-sender.git
Navigate to the project directory:
cd Bulk-Email-sender
Install dependencies:
Ensure all dependencies are installed as listed above using pip 📥
Configuration ⚙️

SMTP Server Setup:
Update the SMTP server settings with your email provider's details:
SMTP Host (e.g., smtp.gmail.com for Gmail)
SMTP Port (typically 587 for TLS)
Sender Email and Password: Provide the credentials of the email account from which you will send emails 🔑
Recipient List:
Prepare a list of recipients in a CSV file (e.g., contacts.csv) with the following columns:
Name 👤
Email 📧
Email Template:
Customize the email template in the code or in a separate file to personalize the message for each recipient 📝
Usage 🚀

Prepare the Contact List:
Ensure the contact list CSV file is in the correct format and contains valid emails ✅
Run the Script:
Execute the bulk email sender script:
python bulk_email_sender.py
Monitor Progress:
The script will send emails to all recipients in the contact list and provide a status report for each email 📊
