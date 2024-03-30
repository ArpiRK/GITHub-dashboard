from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from flask import render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# GitHub API base URL
GITHUB_API_BASE_URL = 'https://api.github.com/users/'
#GITHUB_API_BASE_URL = 'https://api.github.com/repos/'

def get_user_details(username):
    # Make a request to the GitHub API
    response = requests.get(GITHUB_API_BASE_URL + username)
    
    if response.status_code == 200:
        # Parse the JSON response
        user_data = response.json()

        # Fetch additional details like followers
        followers_data = get_followers_details(username)
        following_data = get_following_details(username)
        #repositories_data = get_user_repositories(username)

        user_data['followers'] = followers_data
        user_data['following'] = following_data
        #user_data['repositories'] = repositories_data

        return user_data
    else:
        return None

def get_followers_details(username):
    # Make a request to the GitHub API to get followers details
    response = requests.get(GITHUB_API_BASE_URL + username + '/followers')
    
    if response.status_code == 200:
        # Parse the JSON response
        followers_data = response.json()
        return followers_data
    else:
        return None


    
def get_following_details(username):
    # Make a request to the GitHub API to get following details
    response = requests.get(GITHUB_API_BASE_URL + username + '/following')
    
    if response.status_code == 200:
        # Parse the JSON response
        following_data = response.json()
        return following_data
    else:
        return None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    

    user_details = get_user_details(username)

    if user_details:
        # Pass user details to the template
        return render_template('user_details.html', user_details=user_details)
    else:
        flash("Failed to fetch user details from GitHub API", "error")
        return redirect(url_for('index'))
 

@app.route('/user_details', methods=['GET', 'POST'])
def user_details():
    if request.method == 'POST':
        username = request.form['username']
        user_details = get_user_details(username)
        return render_template('user_details.html', user_details=user_details)

    return render_template('user_details.html', user_details=None)


if __name__ == '__main__':
    app.run(debug=True)
