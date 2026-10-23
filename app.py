from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

PROJECTS = [
    {
        "number": "01",
        "name": "AI Bottle Detection System",
        "description": "An AI-powered system for detecting bottles.",
        "image": "/ai_bottle_detection_only.png",
        "image_alt": "AI bottle detection system preview",
        "url": "https://ai-bottle-detection-system.onrender.com/",
    },
    {
        "number": "02",
        "name": "CFD Data-Driven Machine Learning Surrogate Model for Stirred Tank Bioreactor",
        "description": "In progress",
        "image": "/bioreactor_cfd_ml_surrogate_logo_icon.png",
        "image_alt": "Stirred tank bioreactor and machine learning logo",
        "url": "",
    },
    {
        "number": "03",
        "name": "AI-Based Beverage Quality Prediction Using Theoretical and Machine Learning Models",
        "description": "In progress",
        "image": "/beverage_quality_prediction_logo.png",
        "image_alt": "Beverage quality prediction and analysis logo",
        "url": "",
    },
]


@app.get("/")
def dashboard():
    return render_template("index.html", projects=PROJECTS)


@app.get("/logo1.png")
def logo():
    return send_from_directory(app.root_path, "logo1.png")


@app.get("/ai_bottle_detection_only.png")
def bottle_detection_logo():
    return send_from_directory(app.root_path, "ai_bottle_detection_only.png")


@app.get("/bioreactor_cfd_ml_surrogate_logo_icon.png")
def bioreactor_logo():
    return send_from_directory(app.root_path, "bioreactor_cfd_ml_surrogate_logo_icon.png")


@app.get("/beverage_quality_prediction_logo.png")
def beverage_quality_logo():
    return send_from_directory(app.root_path, "beverage_quality_prediction_logo.png")


if __name__ == "__main__":
    app.run(debug=True)
