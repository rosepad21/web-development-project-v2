from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

# creating a route, a part of the url after the domain name
@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@app.route('/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)