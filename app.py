from flask import Flask

app = Flask(__name__)

# creating a route, a part of the url after the domain name
@app.route('/')
def hello_world():
  return "Hello, world!"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)