import deepl

def etok(query):
    auth_key = "ea435442-ecc9-4a54-a9a9-f2a71e76179b:fx"
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(query, target_lang="KO")
    return (result.text) 
 
