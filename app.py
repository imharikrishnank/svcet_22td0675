from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Contact Model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Home Route - Show Contacts
@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

# Add Contact Route
@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    
    new_contact = Contact(name=name, email=email, phone=phone)
    db.session.add(new_contact)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_contact(id):
    contact = Contact.query.get(id)
    if contact:
        contact.name = request.form['name']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete<int:id>', methods=['POST'])
def delete_contact(id):
    contact = Contact.query.get(id)
    if contact:
        db.session.delete(contact)
        db.session.commit()
    return redirect(url_for('index'))
 
if __name__ == '__main__':
    app.run(debug=True)
