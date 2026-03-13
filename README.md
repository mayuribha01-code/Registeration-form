# Flask Registration Form 
## Project Description

This is a simple web application that allows users to register with their name, email, and password.  
It includes:
- A registration form with proper input validation  
- Real-time error messages (empty fields, invalid email, passwords don't match, etc.)  
- Password hashing for security  
- Data saved in a SQLite database (`users.db`)  
- Success page after successful registration  

## Technologies Used
- Python  
- Flask  
- Flask-WTF (for forms and validation)  
- Flask-SQLAlchemy (for database)  
- WTForms validators  
- Werkzeug (for password hashing)  
- email-validator (for proper email checking)  
- SQLite (lightweight database – no installation needed)

## How to Run the Project

### Requirements
- Python 3.8 or higher installed on your computer

### Step-by-step instructions

1. **Open the project folder**  
   Example: `C:\Users\LIBRARY\Documents\Mayuri_assignment8`

2. **Open Command Prompt (cmd) in this folder**  
   - Easiest way: In File Explorer, type `cmd` in the address bar and press Enter

3. **Install required packages** (only needed the first time)  
   Copy and paste this command → press Enter:pip install flask flask-wtf flask-sqlalchemy werkzeug email-validator

4. **Start the application**  
Run this command:python app.py

You will see messages like:  
`* Running on http://127.0.0.1:5000`  
(keep this window open)

5. **Open the form in your browser**  
Go to this address:  
http://127.0.0.1:5000  
or  
http://127.0.0.1:5000/register

6. **Test the form**
- Try submitting with empty fields → you should see error messages  
- Try wrong email format → error  
- Try different passwords → error  
- Fill correct data → you should see "Registration Successful!" page

7. **Stop the application**  
Go back to the command prompt window and press:  
`Ctrl + C`


**THANK YOU**
