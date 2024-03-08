from flask import Flask, render_template
import requests
import pandas as pd 

app = Flask(__name__)


# After the loop, df will contain the concatenated DataFrame


@app.route('/')
def index():
    # Render the template with DataFrame passed to it
    return render_template('home.html')


