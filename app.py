# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

class MedicineInjection:
    def __init__(self, spot, date, serial_number, patient_name, patient_surname):
        self.spot = spot
        self.date = date
        self.serial_number = serial_number
        self.patient_name = patient_name
        self.patient_surname = patient_surname

    def __str__(self):
        return f"Spot: {self.spot}, Date: {self.date}, Serial Number: {self.serial_number}, Name: {self.patient_name}, Surname: {self.patient_surname}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        spot = request.form['spot']
        date = request.form['date']
        serial_number = request.form['serial_number']
        patient_name = request.form['patient_name']
        patient_surname = request.form['patient_surname']
        injection = MedicineInjection(spot, date, serial_number, patient_name, patient_surname)
        return render_template('result.html', injection=injection)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
