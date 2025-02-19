from flask import Flask, render_template, redirect, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    statement = request.args.get("textToAnalyze")
    if statement :
        emotions = emotion_detector(statement)
        print("aa\n")
        print(request)
        print("aa\n")

        if emotions["dominant_emotion"] is None:
            return "Invalid text! Please try again!"
        else:
            return f"""For the given statement, the system response is 'anger': {emotions['anger']},
            'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} and
            'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."""
    else:
        emotions = emotion_detector(statement)
        print("aa\n")
        print(request)
        print("aa\n")

        if emotions[0]["dominant_emotion"] is None:
            return "Invalid text! Please try again!"
        else:
            return f"""For the given statement, the system response is 'anger': {emotions['anger']},
            'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} and
            'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."""
    return {'error':404,'message':'You have to express a statement'}, 404

@app.route("/")
def open_index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)