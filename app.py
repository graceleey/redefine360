from flask import Flask, render_template, request
import test1 as krdict
import test2 as edict 
import test3 as ekdict 
import test4 as googletransdict 
import re

app = Flask(__name__, static_url_path='/static/')
app.debug = True
@app.route("/")
def home():
    return "Hello!!!"

@app.route('/capstone')
def about():
    return render_template('capstone.html', krdef="", engdef="")


@app.route('/process', methods=["POST"])
def process():
    print("hello world")

    inputvalue = request.values.get('search')
    
    krdef =""
    engtokor=""
    engdef=""
    googletransdef=""
    koreanRegex = re.compile('[\uac00-\ud7a3]+')
    iskorean =  bool(koreanRegex.search(inputvalue))
    if (iskorean):
        krdef = krdict.main(inputvalue)
        
    else: 
        engtokor = ekdict.etok(inputvalue)
        engdef = edict.engdict(inputvalue)
    
    googletransdef= googletransdict.googleTranslate(inputvalue)
        
    return render_template('capstone.html', krdef=krdef, engdef=engdef, engtokor=engtokor, googletransdef=googletransdef, wordsearched = inputvalue)
