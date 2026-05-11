from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = [
        request.form['First Name'],
        request.form['Last Name'],  # Capitalized 'Last Name'
        request.form['Email'],
        request.form['Password']    # Capitalized 'Password'
    ]

    file_exists = os.path.isfile('submissions.csv')
    with open('submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['First Name', 'Last Name', 'Email', 'Password'])  # Write headers
        writer.writerow(data)

    return "<h3>Data saved successfully! <a href='/'>Back to Form</a></h3>"

if __name__ == "__main__":  # Fixed this line
    app.run(debug=True, host='0.0.0.0', port=5001)
