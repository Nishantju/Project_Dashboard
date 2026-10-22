from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

PROJECTS = [
    {
        "number": "01",
        "name": "AI Bottle Detection System",
        "description": "An AI-powered system for detecting bottles.",
        "url": "https://ai-bottle-detection-system.onrender.com/",
    },
    {
        "number": "02",
        "name": "CFD Data-Driven Machine Learning Surrogate Model for Stirred Tank Bioreactor",
        "description": "In progress",
        "url": "",
    },
    {
        "number": "03",
        "name": "AI-Based Beverage Quality Prediction Using Theoretical and Machine Learning Models",
        "description": "In progress",
        "url": "",
    },
]


@app.get("/")
def dashboard():
    return render_template("index.html", projects=PROJECTS)


@app.get("/logo1.png")
def logo():
    return send_from_directory(app.root_path, "logo1.png")


if __name__ == "__main__":
    app.run(debug=True)
