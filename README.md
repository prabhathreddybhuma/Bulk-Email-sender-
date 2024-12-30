# Bulk Email Sender Pro 📧

A powerful and secure web application for sending personalized bulk emails with advanced features like template management, email tracking, and analytics. Perfect for marketing campaigns, newsletters, event notifications, and any scenario requiring sophisticated mass email distribution.

## Features ✨

### Core Features 🚀
- **Bulk Email Distribution**: Send emails to multiple recipients simultaneously 📤
- **Smart Personalization**: Dynamic content insertion using recipient data 👤
- **Template Management**: Save, edit, and reuse email templates 📑
- **CSV Integration**: Upload recipient lists via CSV with custom field mapping 📋
- **HTML Support**: Rich text editor for creating beautiful HTML emails 🎨
- **Email Preview**: Preview emails before sending ✉️

### Advanced Features 🔥
- **Background Processing**: Asynchronous email sending using Celery ⚡
- **Email Tracking**: Monitor delivery status, opens, and clicks 📊
- **Scheduling**: Schedule emails for future delivery 🕒
- **Rate Limiting**: Prevent abuse and ensure delivery 🛡️
- **Multiple SMTP Support**: Configure multiple SMTP servers 🔌
- **User Management**: Multi-user support with role-based access 👥

### Security Features 🔒
- **Secure Authentication**: User authentication with password hashing 🔑
- **CSRF Protection**: Built-in protection against cross-site request forgery 🛡️
- **Rate Limiting**: Prevent abuse and ensure reliable delivery 🚦
- **Input Validation**: Comprehensive validation for all user inputs ✅
- **Error Handling**: Robust error handling and user feedback ⚠️

## Technical Requirements ⚙️

### Core Requirements
- Python 3.8+ 🐍
- Flask 2.0+ 🌶️
- PostgreSQL 13+ 🐘

### Python Dependencies
```bash
flask==2.0.1
flask-sqlalchemy==2.5.1
flask-login==0.5.0
flask-mail==0.9.1
flask-wtf==0.15.1
celery==5.1.2
redis==3.5.3
psycopg2-binary==2.9.1
python-dotenv==0.19.0
```

## Installation 🛠️

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/bulk-email-sender-pro.git
cd bulk-email-sender-pro
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Setup**
```bash
# Create .env file
cp .env.example .env

# Update .env with your configurations
nano .env
```

5. **Database Setup**
```bash
flask db upgrade
```

6. **Start Redis Server** (Required for Celery)
```bash
redis-server
```

7. **Start Celery Worker**
```bash
celery -A app.celery worker --loglevel=info
```

## Configuration ⚙️

### Environment Variables
```env
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost/dbname
REDIS_URL=redis://localhost:6379
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### SMTP Configuration
1. Enable 2-Step Verification in your Google Account
2. Generate an App Password
3. Use the App Password in your `.env` file

## Usage 🚀

### Starting the Application
```bash
# Start the Flask application
flask run

# In a separate terminal, start Celery worker
celery -A app.celery worker --loglevel=info
```

### Sending Bulk Emails
1. Log in to the application
2. Upload your CSV file or enter emails manually
3. Create or select an email template
4. Preview your email
5. Send or schedule your campaign

### CSV Format
Your CSV file should include these columns:
```csv
name,email,custom_field1,custom_field2
John Doe,john@example.com,value1,value2
Jane Smith,jane@example.com,value3,value4
```



### Running Tests
```bash
pytest
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄



## Support 💬

For support, email bulkemail@gmail.com or create an issue in the GitHub repository.

---
