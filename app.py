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
        'Days_worn': float(request.form['Days_worn']),
        'Days_left_out': float(request.form['Days_left_out']),
        'Activity': float(request.form['Activity']),
        'Stress': float(request.form['Stress']),
        'Temperature': float(request.form['Temperature']),
        'Hours': float(request.form['Hours'])
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
    
    answers = []
    if data['Classifier'] == 'naive':
        correct, total = Classifier.run_test()
        answers.append(str(correct) + ' / ' + str(total) + ' correct')
    else:
        correct, total = Fuzzy_simpful.run_tests()
        answers.append(str(correct) + ' / ' + str(total) + ' correct')
    
    return render_template('form.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)