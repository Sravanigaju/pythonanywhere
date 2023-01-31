from flask import Flask, render_template
import git

app = Flask(__name__)

@app.route ('/update_server', methods=['POST'])
def update_server():
  repo = git.Repo('./pythonanywhere')  
  origin = repo.remotes.origin
  repo.create_head('main',
  origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return '', 200

@app.route ("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host='0.0.0.0',port=6464)
    