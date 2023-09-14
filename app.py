from flask import Flask, render_template, jsonify 

app = Flask(__name__)

JOBS = (
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Lagos, Nigeria',
    'salary': '#250,000'
  },

  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Rivers, Nigeria',
    'salary': '#300,000'
  },

  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '#500,000'
  },

  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco ',
    'salary': '$750,000'
  } 
)

@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/jobs")
def list_jobs():
  return render_template('job.html', jobs=JOBS,
                        company_name='Techful')

@app.route("/about")
def about_us():
  return render_template('about.html')


if  __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)