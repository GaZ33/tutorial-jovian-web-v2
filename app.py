from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
  {"id": 1, "title": "Data analyst", "Location": "SP, brasil", "salary": "Rs: 1,000.00"},
  {"id": 2, "title": "Data Scientist", "Location": "RJ, brasil", "salary": "Rs: 1,900.00"},
  {"id": 3, "title": "Front engineer", "Location": "REMOTE"},
  {"id": 4, "title": "back-end engineer", "Location": "PR, Brasil", "salary": "Rs: 1,500.00"}
]



@app.route("/")
def hello_world():
  return render_template("home.html", jobs=jobs)

@app.rout("/api/jobs")
def list_jobs():
  return jsonify(jobs)



if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
  