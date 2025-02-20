""" server """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """ Function handles /emotionDetector routes."""
    statement = request.args.get("textToAnalyze")
    if statement :
        emotions = emotion_detector(statement)
        if emotions["dominant_emotion"] is None:
            return "Invalid text! Please try again!"
        return f"""For the given statement, the system response is 'anger':
            {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear':
            {emotions['fear']}, 'joy': {emotions['joy']} and 'sadness':
            {emotions['sadness']}. The dominant emotion is
            {emotions['dominant_emotion']}."""
    emotions = emotion_detector(statement)
    if emotions[0]["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return {'error':404,'message':'You have to express a statement'}, 404

@app.route("/")
def open_index():
    """ Function handles / routes."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
