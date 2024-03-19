# app.py (continuation)
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy to use SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary notifications

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define SQLAlchemy model for medicine injection
class MedicineInjection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spot = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(100), nullable=False)
    patient_name = db.Column(db.String(100), nullable=False)
    patient_surname = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"MedicineInjection(spot={self.spot}, date={self.date}, serial_number={self.serial_number}, " \
               f"patient_name={self.patient_name}, patient_surname={self.patient_surname})"

# Route for handling form submission
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        spot = request.form['spot']
        date = request.form['date']
        serial_number = request.form['serial_number']
        patient_name = request.form['patient_name']
        patient_surname = request.form['patient_surname']
        
        # Save form data to database
        injection = MedicineInjection(spot=spot, date=date, serial_number=serial_number,
                                      patient_name=patient_name, patient_surname=patient_surname)
        db.session.add(injection)
        db.session.commit()
        
        # Query database for previous data for the specific name and surname
        previous_data = MedicineInjection.query.filter_by(patient_name=patient_name, 
                                                           patient_surname=patient_surname).all()
        
        return render_template('form.html', previous_data=previous_data)  # Pass previous data to template
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
