from flask import Flask
app = Flask (__name__)
@app.route('/')
def hello_world():
    return "hello world!"
if __name__=="__main__":
    @app.route('/dojo')
    def dojo():
        return "dojo"
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hi, " + name
@app.route('/repeat/<word>/<int:num>')
def repeat(word,num):
    return word * num

app.run(debug=True)
