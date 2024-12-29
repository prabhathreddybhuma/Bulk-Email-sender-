from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Flask-Mail configuration (initially empty)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Save credentials in session (not recommended for production)
        session['email'] = email
        session['password'] = password

        # Configure Flask-Mail with user credentials
        app.config['MAIL_USERNAME'] = email
        app.config['MAIL_PASSWORD'] = password

        # Test SMTP login
        try:
            with mail.connect() as conn:
                pass  # If successful, redirect to email-sender page
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Login failed: {str(e)}', 'error')

    return render_template('login.html')  # Render login page


@app.route('/email-sender', methods=['GET', 'POST'])
def index():
    if 'email' not in session or 'password' not in session:
        flash("Please log in first.", "error")
        return redirect(url_for('login'))

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
                        msg = Message(subject, sender=session['email'], recipients=[recipient_email])
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
                    msg = Message(subject, sender=session['email'], recipients=[email])
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
