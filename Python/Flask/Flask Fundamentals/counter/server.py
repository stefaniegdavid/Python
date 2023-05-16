from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Gucci'

@app.route('/')
def index():
    if "add_num" in session:
        session['add_num'] =+ 1
    else:
        session['add_num'] = 0
        return render_template("index.html")
    
@app.route('/count', methods=['POST'])
def click():
    session['add_num'] =+ int(request.form['add'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def destroy_session():
    session.clear()
    session["add_num"] = 0
    return redirect('/')

@app.route('/plus_two', methods=['POST'])
def plus_two():
    session['add_num'] += 1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
