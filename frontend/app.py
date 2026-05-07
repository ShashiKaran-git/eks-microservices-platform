from flask import Flask, render_template, request, redirect
import requests
import os

app = Flask(__name__)

API_URL = os.environ.get("API_URL", "http://api-service:5000")


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        text = request.form.get("text")

        requests.post(
            f"{API_URL}/task",
            json={"text": text}
        )

        return redirect("/")

    response = requests.get(f"{API_URL}/tasks")

    tasks = response.json()

    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)