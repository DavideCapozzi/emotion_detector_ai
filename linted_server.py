"""
Flask web application for emotion detection analysis.
Provides endpoints for emotion detection and serving the index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """Handle emotion detection analysis request and return formatted results."""
    text_to_analyze = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyze)

    if res["dominant_emotion"] is None:
        return "<strong>Invalid text! Please try again!.</strong>"

    response_parts = [
        "For the given statement, the system response is",
        f"'anger': {res['anger']}, 'disgust': {res['disgust']}, ",
        f"'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': {res['sadness']}.",
        f" The dominant emotion is <strong>{res['dominant_emotion']}.</strong>"
    ]

    return " ".join(response_parts)

@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
