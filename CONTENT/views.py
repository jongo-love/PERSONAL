#This files has a bunch of url's
from flask import Blueprint ,render_template,url_for, request,redirect,flash
from flask_mail import Message, Mail
views = Blueprint('views', __name__)
mail=Mail()

@views.route('/')
def HOME():
    return render_template('home.html')

@views.route('/about')
def ABOUT():
    return render_template('about.html')

@views.route('/contact',methods=['GET', 'POST'])
def CONTACT():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate form data (e.g., ensure email is in the correct format, fields are not empty, etc.)
        if not name or not email or not message:
            flash("All fields are required.", "error")
            return redirect(url_for('views.CONTACT'))
        
        # Create and send email
        msg = Message(subject=f"New Contact Form Submission from {name}",
                      sender=email,
                      recipients=['sammochache01@gmail.com'],  # Replace with your email
                      body=f"Message from {name} ({email}):\n\n{message}")

        mail.send(msg)

        flash("Your message has been sent successfully!", "success")
        return redirect(url_for('views.HOME'))

    return render_template('contact.html')

@views.route('/visualsnack')
def SNACK():
    return render_template('snack.html')

