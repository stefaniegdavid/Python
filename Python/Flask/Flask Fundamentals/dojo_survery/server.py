from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

app.secret_key="Gucci"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    print (session)
    return render_template("result.html")


if __name__=="__main__":
    app.run(debug=True)