from flask import Flask, render_template, request
from datetime import datetime
import threading
import time

app = Flask(__name__)

# Store reminders in memory
reminders = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        medicine = request.form['medicine']
        time_str = request.form['time']
        reminders.append({"name": name, "medicine": medicine, "time": time_str})
    return render_template('index.html', reminders=reminders)

if __name__ == '__main__':
    app.run(debug=True)