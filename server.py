"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection on user-provided text.

Author (Learner): [Vaishnavi Arthamwar]
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Analyze the user-provided text for emotions and return the result.

    This function takes input text from the user, sends it to the emotion detection function, 
    and returns a response based on the detected emotions.

    Returns:
        str: Formatted string with the emotion analysis results or an error message if input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    # Extract emotions from the response
    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion', None)

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main application page.

    This function initiates the rendering of the main application page over the Flask channel.

    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
