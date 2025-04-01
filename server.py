from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyze)
    if res["dominant_emotion"] == None:
        return "<strong>Invalid text! Please try again!.</strong>"
    s1 = "For the given statement, the system response is"
    s2 = " 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}.".format(res["anger"], res["disgust"], res["fear"], res["joy"], res["sadness"])
    s3 = " The dominant emotion is <strong>{}.</strong>".format(res["dominant_emotion"])
    return s1 + s2 + s3
    

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)