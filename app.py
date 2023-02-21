from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'New York',
    'salary': '1000$'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Los Angeles',
    'salary': '2000$'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '3000$'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Rome, Italy'
  }
]

# creating a route, a part of the url after the domain name
@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)