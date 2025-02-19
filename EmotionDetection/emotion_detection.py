import requests
import json
def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = body, headers=header)
    # Parse json
    formatted_response = json.loads(response.text)
    # Access the emotions in dict
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    # Initialize a dictionary to determine dominant emotion
    dominant_emotion = {"emotion":"", "value":0}
    # Reach each emotion to determine dominant one.
    for emotion in (emotions):
        # Compare the current emotion's score with assigned emotion's.
        if float(emotions[emotion]) > float(dominant_emotion["value"]):
            # If the current one more dominant then update 'dominant_emotion' with current values
            dominant_emotion.update({"emotion": emotion, "value":emotions[emotion]})
    # After checking complete, update the respond 'emotions'
    emotions.update({'dominant_emotion' :dominant_emotion["emotion"] })
    return emotions