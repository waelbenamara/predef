from git import Repo

git_url = "https://github.com/pallets/flask-website"
repo_dir = "p2"
Repo.clone_from(git_url, repo_dir)