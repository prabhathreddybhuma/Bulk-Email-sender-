from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bulkemail19@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'gucg bfip fkng hnhj'  # Replace with your App Password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the user uploaded a CSV file or entered emails manually
        if 'csv_file' in request.files and request.files['csv_file'].filename != '':
            csv_file = request.files['csv_file']
            csv_path = os.path.join(UPLOAD_FOLDER, csv_file.filename)
            csv_file.save(csv_path)

            try:
                # Process the CSV file
                with open(csv_path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        recipient_email = row['email']
                        recipient_name = row['name']
                        subject = request.form['subject']
                        message_body = request.form['message'].replace('{name}', recipient_name)

                        # Send the email
                        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient_email])
                        msg.body = message_body
                        mail.send(msg)

                flash('Emails sent successfully!', 'success')

            except Exception as e:
                flash(f'Error processing CSV file: {str(e)}', 'error')

        elif 'emails' in request.form and request.form['emails']:
            # If emails were entered manually
            recipient_emails = request.form['emails']  # Comma-separated emails
            subject = request.form['subject']
            message_body = request.form['message']

            try:
                # Convert the email string to a list
                recipients_list = [email.strip() for email in recipient_emails.split(',') if email.strip()]
                
                # Send the email
                for email in recipients_list:
                    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[email])
                    msg.body = message_body
                    mail.send(msg)

                flash('Emails sent successfully!', 'success')

            except Exception as e:
                flash(f'Error: {str(e)}', 'error')

        else:
            flash('Please provide either a CSV file or manual emails!', 'error')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
