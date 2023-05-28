from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Sudheer Rudraraju!"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/user/<username>')
def user_profile(username):
    return f"Welcome to your profile, {username}!"

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Process the form data (e.g., save to database, send an email)
        # ...
        return "Thanks for your message! We'll get back to you soon."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
