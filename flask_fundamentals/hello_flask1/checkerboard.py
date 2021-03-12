from flask import Flask, render_template  
app = Flask(__name__)    
@app.route('/')
def home():
    return render_template('checkerboard.html', x=4, y=4) 
@app.route('/<x>/<y>')
def down(x,y):
    return render_template('checkerboard.html', x=int(x), y=int(y))   
if __name__=="__main__":   
    app.run(debug=True)  