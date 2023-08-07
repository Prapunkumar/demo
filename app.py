from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = 'onlineclassroom_database'

# db = SQLAlchemy(app)

# class ContactForm (db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(50), nullable=False)
#     message = db.Column(db.String(500), nullable=False)


@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # contact_form = ContactForm(name=name, email=email, message=message)
    # db.session.add(contact_form)
    # db.session.commit()

    return 'Thank you for your submission!'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # contact = ContactForm(name=name, email=email, message=message)
        # db.session.add(contact)
        # db.session.commit()
        # messages = ContactForm.query.all()
        # for message in messages:
        #     print(message.name,message.email,message.message)
        print('Message Sent Successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('contactus.html')
@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/css_desc')
def css_desc():
    return render_template('css_desc.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/html_desc')
def html_desc():
    return render_template('html_desc.html')

@app.route('/javascript_desc')
def javascript_desc():
    return render_template('javascript_desc.html')


if __name__ == '__main__':
    # with app.app_context():
        # db.create_all()
    app.run(debug=True)
