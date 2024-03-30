from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GITHUB_API_BASE_URL = "https://api.github.com/"

@app.route('/repos/<username>')

def get_repo_details(username):
    # Make a request to the GitHub API to get repository details
    response = requests.get(GITHUB_API_BASE_URL + "users/" + username + '/repos')
  
    if response.status_code == 200:
        repositories = response.json()
        repository_names = [repository.get('name') for repository in repositories if repository.get('name')]
        return render_template('repos.html', username=username, repositories=repository_names)
    else:
        return f"Error: Unable to fetch repositories. Status code: {response.status_code}"

@app.route('/repos/<username>/repo_name/forks')
def get_fork_details(username, repo_name):
    # Make a request to the GitHub API to get fork details for all repositories
    
    response = requests.get(GITHUB_API_BASE_URL + '/repos/' + username + repo_name + '/forks')
  
    if response.status_code == 200:
        forks = response.json()
        fork_count = sum([repository.get('forks_count', 0) for repository in forks])
        return render_template('forks.html', username=username, fork_count=fork_count)
    else:
        return f"Error: Unable to fetch repositories. Status code: {response.status_code}"
    
if __name__ == '__main__':
    app.run(debug=True)

	
	