
# Bulk Email Sender 📧

A simple and efficient tool to send bulk emails using a pre-designed email template. This project is designed to help users send personalized emails in bulk, making it perfect for marketing campaigns, event notifications, newsletters, or any situation requiring mass email distribution.

## Features ✨

- **Bulk Email Sending**: Send emails to multiple recipients at once 📤
- **Personalization**: Include personalized details (such as recipient names) in each email ✉️
- **Email Templates**: Use a pre-designed email template for formatting the message 📑
- **SMTP Integration**: Uses SMTP server to send emails securely 🔒
- **Email Status Tracking**: Track the status of emails sent (success or failure) ✅❌
- **Error Handling**: Provides error messages for failed email deliveries ⚠️

## Requirements ⚙️

- **Python 3.x**: Ensure Python is installed on your machine 🐍
- **Libraries**: Install the required libraries using pip:
  ```bash
  pip install smtplib email-validator
  ```

## Installation 🛠️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/prabhathreddybhuma/Bulk-Email-sender.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Bulk-Email-sender
   ```

3. **Install dependencies**:
   - Ensure all dependencies are installed as listed above using `pip` 📥

## Configuration ⚙️

1. **SMTP Server Setup**:
   - Update the SMTP server settings with your email provider's details:
     - **SMTP Host** (e.g., `smtp.gmail.com` for Gmail)
     - **SMTP Port** (typically `587` for TLS)
     - **Sender Email** and **Password**: Provide the credentials of the email account from which you will send emails 🔑

2. **Recipient List**:
   - Prepare a list of recipients in a CSV file (e.g., `contacts.csv`) with the following columns:
     - `Name` 👤
     - `Email` 📧

3. **Email Template**:
   - Customize the email template in the code or in a separate file to personalize the message for each recipient 📝

## Usage 🚀

1. **Prepare the Contact List**:
   - Ensure the contact list CSV file is in the correct format and contains valid emails ✅

2. **Run the Script**:
   - Execute the bulk email sender script:
     ```bash
     python bulk_email_sender.py
     ```

3. **Monitor Progress**:
   - The script will send emails to all recipients in the contact list and provide a status report for each email 📊

## Example 🧑‍💻

Here's how the code might look to send a bulk email:

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Setup SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your_email@example.com"
sender_password = "your_email_password"

# Prepare the email content
subject = "Welcome to Our Event! 🎉"
body = "Hello {name},\n\nWe are excited to have you at our event!"

# Create the SMTP session
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)

# Send emails to all recipients in the contact list
for recipient in contacts:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient['email']
    msg['Subject'] = subject
    msg.attach(MIMEText(body.format(name=recipient['name']), 'plain'))
    server.sendmail(sender_email, recipient['email'], msg.as_string())

server.quit()
```

## Contributing 🤝

1. Fork the repository 🍴
2. Create a new branch (`git checkout -b feature-name`) 🌱
3. Commit your changes (`git commit -am 'Add feature'`) 💻
4. Push to the branch (`git push origin feature-name`) 🚀
5. Create a new pull request 🔄



---
