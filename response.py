from transformers import pipeline


classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

def clasify(sentence):
    
    model_outputs = classifier(sentence)

    for emotion in model_outputs[0]:
        if emotion['score'] > 0.5:
            return emotion['label']
