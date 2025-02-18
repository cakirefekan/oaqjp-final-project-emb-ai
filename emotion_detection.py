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
    result = formatted_response['emotionPredictions'][0]['emotion']
    return result