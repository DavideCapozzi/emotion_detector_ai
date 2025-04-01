from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyze)
    return "For the given statement, the system response is" + 
    " 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}.".format(res["anger"], res["disgust"], res["fear"], res["joy"], res["sadness"]) +
    " The dominant emotion is {}.".format(res["dominant_emotion"])

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)