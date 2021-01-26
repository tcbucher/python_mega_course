from flask import Flask

# __name__ gets the name of your python script
# the main script being run is given the name __main__
# if your script is called by main, it gets the name script1
# etc.
app = Flask(__name__) 

@app.route('/') # Decorator that maps the given URL to the execution of the function it decorates
def home():
    return "Hello"

# This is checking if this is the main script being run
if __name__ == "__main__":
    app.run(debug=True)