from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "you will never walk alone"

@app.route('/')
def index():
    if 'computer' not in session:
        session['computer'] = 0
    computer_choice = int(random.randrange(0,101))
    session['computer'] = computer_choice
    print(computer_choice)
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def process_play():
    rGuess = request.form['guess']
    if int(rGuess) == session['computer']:
        return render_template('correct.html')
    if int(rGuess) > session['computer']:
        return render_template('high.html')
    if int(rGuess) < session['computer']:
        return render_template('low.html')

@app.route('/reset')
def reset():
    print('reset')
    session.pop('computer')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)