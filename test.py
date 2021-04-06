from flask import Flask, request,jsonify
from Project import Project
from git import Repo
import uuid
import json
from Result import Result


app = Flask(__name__)



@app.route('/analyse')
def analyse():
	data = request.get_json()
	git_url = data['git_repo']
	project_id = str(uuid.uuid1())
	repo_dir = "./projects/"+ project_id
	Repo.clone_from(git_url, repo_dir)
	project = Project(repo_dir)
	project.analyse()
	result = Result(project)
	output = json.dumps(result.__dict__)


	return output






if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3030,debug = False)	