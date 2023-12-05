from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    columns = result.keys()
    result_dicts = []
    for row in result.fetchall():
        result_dicts.append(dict(zip(columns, row))) 
  return result_dicts

@app.route("/")
def hello_jovian():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)



if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
  