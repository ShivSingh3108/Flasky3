from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/troll')
def troll():
    user_name= "RICKROLLED"
    return render_template('troll.html', user_name=user_name)

@app.route('/about')
def about():
    user_name= "SHIV"
    return render_template('about.html', user_name=user_name)
if __name__ == "__main__":
    app.run(port= 5000, debug=True)