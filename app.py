from flask import Flask, render_template, request, session
import Fuzzy_simpful
import Classifier

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def form():
    # Retrieve answers from the session if available
    answers = session.pop('answers', None)
    return render_template('form.html', answers=answers)

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'Classifier': request.form['Classifier'],
        'Days_worn': int(request.form['Days_worn']),
        'Days_left_out': int(request.form['Days_left_out']),
        'Activity': int(request.form['Activity']),
        'Stress': int(request.form['Stress']),
        'Temperature': int(request.form['Temperature']),
        'Hours': int(request.form['Hours'])
    }
    
    answers = []
    if data['Classifier'] == 'naive':
        answers.append(Classifier.calculate_score(data))
    else:
        answers.append(Fuzzy_simpful.calculate_score(data))
    
    return render_template('form.html', answers=answers)

@app.route('/run_tests', methods=['POST'])
def run_tests():
    data = {
        'Classifier': request.form['Classifier']
    }
    
    answers = None
    if data['Classifier'] == 'naive':
        Classifier.run_test()
    else:
        Fuzzy_simpful.run_tests()
    
    return render_template('form.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)