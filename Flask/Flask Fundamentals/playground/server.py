from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return "Welcome to the the main page!"


# ========= LEVEL 1 ========have it render three beautiful looking blue boxes. Please use a template to render this.
@app.route('/play')
def play():
    return render_template("index.html", num = 3, color = "#9acbf3")

# ==========LEVEL 2========= have it display the beautiful looking blue boxes x times. For example, localhost:5000/play/7 should display these blue boxes 7 times. 
# Calling localhost:5000/play/35 would display these blue boxes 35 times. Please remember that x originally is a string, and if you want to use it as an integer, you must first convert it to integer using int(). For example int("7") returns 7.

@app.route('/play/<int:num>')
def play_num(num):
    return render_template("index.html", num = num, color = "#9acbf3")


# ==========LEVEL 3===============have it display beautiful looking boxes x times, but this time where the boxes appear in (color). 
# For example, localhost:5000/play/5/green would display 5 beautiful green boxes. Calling localhost:5000/play/35/red would display 35 beautiful red boxes.

@app.route('/play/<int:num>/<string:color>')
def play_color(num, color):
    return render_template("index.html", num = num, color = color)



if __name__=="__main__":
    app.run(debug=True)