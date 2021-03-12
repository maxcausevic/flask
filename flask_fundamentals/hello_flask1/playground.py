from flask import Flask, render_template  
app = Flask(__name__)    
@app.route('/')
def hello_world():
    return "hello world!"          
@app.route('/hello/<name>') 
def hello(name):
    print(name)
    return render_template("name.html",some_name = name)
@app.route('/<int:times>/<color>')
def repeat(times,color):
    return render_template("name.html", times = times , color = color)
if __name__=="__main__":  

    app.run(debug=True)  