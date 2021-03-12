from flask import Flask, render_template  
app = Flask(__name__)    
@app.route('/')          
def welcom():
    print('Welcome to Choose Your Own Adventure')
    return render_template('name.html',phrase= "Welcome", )
@app.route('/left')
def left():
    return render_template('death.html')
@app.route('/right')
def right():
    return render_template('success.html')
@app.route('/hello/<name>') 
def hello(name):
    print(name)
    return render_template("name.html",some_name = name)