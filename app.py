from flask import Flask

# Create a new Flask instance calld app
app = Flask(__name__)

# Define the root
@app.route('/')
def hello_world():
    return 'Hello world'
