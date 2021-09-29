from flask import Flask, render_template, request, redirect, url_for
from question import Question

app = Flask(__name__)

tuples = [(0,'Does Flask framework is the Python part?',True),
          (1,"Does 'for loop' exist in Python?",True),
          (2,'Does 4/2 is equal 2 in Python?',False),
          (3,'Does Netflix use Flask?',True),
          (4,'Is print a function?',True),
          (5,'Is the current version of Python 2?',False)]

questions = []
for t in tuples:
    questions.append(Question(t[0], t[1], t[2]))
print(questions)

@app.route("/")
def index():
    return render_template('index.html', questions=questions)

@app.route("/result", methods = ["POST"])
def results():
    answers = request.form.items()
    points = 0
    for a in answers:
        print('question', a[0], 'answer', a[1])
        if a[1] == 'yes':
            is_true = True
        else:
            is_true = False

        question_index = int(a[0] )
        correct_answer = questions[question_index].is_correct
        if correct_answer == is_true:
            points += 1
    return render_template('result.html', points=points, questions=questions)

@app.route('/questionnumber', methods=['GET'])
def return_number():
    return {'number of questions' : 6}

@app.route('/answers', methods=['GET'])
def return_answers():
    dictionary = {}
    for t in tuples:
        dictionary[t[0]] = str(t)
    return dictionary

@app.route('/authentication', methods = ['POST'])
def authenticate():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'Bartosz' and password == 'Test':
        return {
            'Authenticate' : 'Accepted',
            'Token' : '1000'
        }
    else:
        return {'Authenticate' : 'Failed',}

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('return_answers', name = user))
    else:
        return render_template('login_page.html')