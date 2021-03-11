from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately 
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":  
    # import statements, maybe some other routes
    @app.route('/success')
    def success():
        return "success"
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name
    
app.run(debug=True)    # Run the app in debug mode.

