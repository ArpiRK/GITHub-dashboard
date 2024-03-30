from flask import Flask, render_template, request, flash, session, redirect, url_for

import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# GitHub API base URL
GITHUB_API_BASE_URL = 'https://api.github.com/repos/'

def get_repo_details(repo_name):
    # Make a request to the GitHub API to get repository details
    response = requests.get(GITHUB_API_BASE_URL + repo_name, headers=get_auth_headers())
    
    if response.status_code == 200:
        # Parse the JSON response
        repo_data = response.json()
        return repo_data
    else:
        return None

def get_auth_headers():
    # Get GitHub username and password from session (you should use a secure storage mechanism)
    username = session.get('github_username')
    password = session.get('github_password')

    # Create authentication headers
    headers = {}
    if username and password:
        headers['Authorization'] = f'Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}'
    
    return headers

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the username and password are correct (replace this with your authentication logic)
    if username == "your_valid_username" and password == "your_valid_password":
        # Store username and password in session (you should use a secure storage mechanism)
        session['github_username'] = username
        session['github_password'] = password

        flash("Login successful", "success")
        return redirect(url_for('repo_details'))
    else:
        flash("Invalid username or password", "error")
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Clear stored credentials from the session
    session.pop('github_username', None)
    session.pop('github_password', None)
    
    flash("Logout successful", "success")
    return redirect(url_for('index'))

@app.route('/repo_details', methods=['GET', 'POST'])
def repo_details():
    if 'github_username' not in session or 'github_password' not in session:
        flash("Please log in to view repository details", "error")
        return redirect(url_for('index'))

    if request.method == 'POST':
        repo_name = request.form['repo_name']
        repo_details = get_repo_details(repo_name)

        if repo_details:
            return render_template('forks.html', repo_details=repo_details)
        else:
            flash("Failed to fetch repository details from GitHub API", "error")
            return render_template('forks.html', repo_details=None)

    return render_template('forks.html', repo_details=None)

if __name__ == '__main__':
    app.run(debug=True)
