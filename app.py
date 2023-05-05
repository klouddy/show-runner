
from flask import Flask , redirect , url_for , request # Importing the class flask
# app is the object or instance of Flask
app = Flask(__name__)
# app.route informs Flask about the URL to be used by function
@app.route('/success/<name>')
# Creating a function named success
def success(name):
    return 'welcome %s' % name


  
if __name__ == '__main__':
   app.run(debug = True)