from googletrans import Translator

def googleTranslate(query):

    translator = Translator()
    if translator.detect(query).lang == "en": 
        return (translator.translate(query, dest="ko").text)
    elif translator.detect(query).lang == "ko": 
        return (translator.translate(query, dest="en").text)
    else:
        return ValueError
    
