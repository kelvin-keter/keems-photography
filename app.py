import os
from flask import Flask, render_template, request

app = Flask(__name__)

# -- Configuration --
# In production, it's safer to get the key from the environment, 
# but this fallback works fine for now.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'keems_secret_key_2026')

# -- Routes --

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="The Passion")

@app.route('/portfolio')
def portfolio():
    # We moved the image definitions directly into portfolio.html 
    # to handle the complex Masonry layout and filtering.
    return render_template('portfolio.html', title="Portfolio")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # In a real app, you would add email sending logic here.
        # For now, it just reloads the page showing the success message.
        return render_template('contact.html', title="Contact", success=True)
    return render_template('contact.html', title="Contact")

# -- Production Entry Point --
if __name__ == '__main__':
    # debug=False is CRITICAL for production security
    # host='0.0.0.0' allows the cloud server (Render) to access the app
    app.run(debug=False, host='0.0.0.0')