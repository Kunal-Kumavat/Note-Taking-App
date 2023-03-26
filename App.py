from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

notes = dict()

@app.route('/index', methods=["GET","POST"])
def index():
    note_title = request.form.get('title')
    note_text = request.form.get('note')
    notes[note_title] = note_text
    return render_template('/home.html', data = notes)


@app.route('/deleteNote', methods=['DELETE','GET','POST'])
def deleteNote():
    notes = notes.pop()
    return render_template('home.html', data=notes)


if __name__ == '__main__':
    app.run(debug=True)
