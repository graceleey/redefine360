from flask import Flask, render_template, request, jsonify, json
# import os
# os.system("python test1.py")
import test1 as kr
import test2 as edict 

# app = Flask(__name__, static_url_path='static', static_folder='capstone/static')
app = Flask(__name__, static_url_path='/static/')
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/capstone')
def about():
    return process()

# @app.route('/search-link/')
@app.route('/process', methods=["POST"])
    
def process():
    #run the api and return it here? 
    print("hello world")
#always run through flask - port 5000. don't use the port 5500
    #request.values.get ? 

    t = request.values.get('search')
    #printing the input
    print(t)
    ans = kr.main(t)
    # print("hello world2")
    print(ans)
    ans1 = edict.engdict(t)
    
    #string 
    combstr = ""
    for item in ans: 
        for subitem in item:
            combstr+=subitem + "\n"
    print(combstr)
    combstr2 = ""
    # combstr2 += list(ans1.keys())[0] + "\n"
    
    # for item in ans1[list(ans1.keys())[0]]: 
    #     for subitem in item:
    #         combstr2+=subitem + "\n"
    # if len(ans1.keys())>1:
    #     combstr2+= list(ans1.keys())[1]
    #     for item in ans1[list(ans1.keys())[1]]: 
    #         for subitem in item:
    #             combstr2+=subitem + "\n"
    print(ans1)

    return render_template('capstone.html', x=combstr, y=ans1)
