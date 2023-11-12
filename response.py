from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")


model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-es-en")


def translate(sentence):
    
    inputs = tokenizer(sentence, return_tensors="pt")
    print(inputs)

    outputs = model.generate(**inputs)
    print(outputs)

    translation = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    print(translation)
    return translation
