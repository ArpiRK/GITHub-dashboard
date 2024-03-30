from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Add this import

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///github_data.db'
db = SQLAlchemy(app)

# Add the following two lines to initialize Flask-Migrate
migrate = Migrate(app, db)

# ... (your existing code)

class Repository(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    repository_name = db.Column(db.String(255))
    commits_count = db.Column(db.Integer)
    contributors_count = db.Column(db.Integer)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        github_username = request.form['username']

        # Fetch commit data
        commits_url = f'{GITHUB_API_BASE_URL}{github_username}/repos'

        with app.app_context():
            commits_response = requests.get(commits_url)

            if commits_response.status_code == 200:
                commits_data = commits_response.json()

                # Fetch contributors data
                contributors_url = f'{GITHUB_API_BASE_URL}{github_username}/followers'
                contributors_response = requests.get(contributors_url)
                contributors_data = contributors_response.json()

                # Store data in the database
                for repo in commits_data:
                    repository = Repository(
                        username=github_username,
                        repository_name=repo['name'],
                        commits_count=len(commits_data) if commits_data else 0,  # Replace with the actual data you want
                        contributors_count=len(contributors_data)  # Assuming contributors_data is a list of contributors
                    )
                    db.session.add(repository)
                    db.session.commit()

                user_repositories_url = f'{GITHUB_API_BASE_URL}{github_username}/repos'
                user_repositories_response = requests.get(user_repositories_url)
                user_repositories_data = user_repositories_response.json() if user_repositories_response.status_code == 200 else []

                return render_template('dash_board.html', repository=repository, repositories=user_repositories_data)
            else:
                return render_template('dash_board.html', error_message="User not found")

    return render_template('dash_board.html', repository=None, repositories=None)

if __name__ == '__main__':
    # Create the database tables outside the request handling
    with app.app_context():
        db.create_all()

    app.run(debug=True)
