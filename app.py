from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Ft Lauderdale, FL',
        'salary': 'usd 50,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Miami, FL',
        'salary': 'usd 100,000'
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location': 'West Palm Beach, FL',
        'salary': 'usd 80,000'
    },
]


@app.route("/")
def hello():
    return render_template("home.html", jobs=JOBS, company_name="DevCurt")


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
