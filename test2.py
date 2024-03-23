import requests

def engdict(query):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + query
    response = requests.get(url)
    apidata = response.json()
    #If there is no definition, print error and return the program.
    print(apidata)
    if len(apidata) >1:
        if type(apidata) =="<class 'list'>": 
            if len(apidata)==3 and apidata[0] == 'No Definitions Found': 
                print("ERROR")
                return
        elif type(apidata) =="<class 'dict'>": 
            if len(apidata)==3 and apidata['title'] == 'No Definitions Found': 
                print("ERROR")
                return


    if type(apidata)=="<class 'list'>" and apidata['title'] == "No Definitions Found":
        exit()
    ansdict = {}
    # if type(apidata)=="<class 'list'>":
    word = apidata[0]["word"]
    # phonetic = apidata[0]["phonetic"]

    meaningslist1 = apidata[0]["meanings"][0]
    partofspeech1 = meaningslist1['partOfSpeech']
        
    ansdict.setdefault(partofspeech1,[])


    definitionmasterlist1 = meaningslist1['definitions']

    definitionlist1 = []
    examplelist1= ['Examples']

    for i in definitionmasterlist1: 

        definitionlist1.append(i['definition'])
        # if 'example' in i:
        #     examplelist1.append(i['example'])  
    ansdict[partofspeech1].append(definitionlist1)
    # ansdict[partofspeech1].append(examplelist1)

        
    if len(apidata[0]["meanings"])>1: 
        meaningslist2 = apidata[0]["meanings"][1]
        partofspeech2 = meaningslist2['partOfSpeech']
            
        definitionmasterlist2 = meaningslist2['definitions']
        definitionlist2 = []
        examplelist2 = ['Examples']

        for i in definitionmasterlist2: 
            definitionlist2.append(i['definition'])
            # if 'example' in i:
            #     examplelist2.append(i['example'])  
    
        ansdict.update({partofspeech2:[]})
        ansdict[partofspeech2].append(definitionlist2)
        # ansdict[partofspeech2].append(examplelist2)
    print(ansdict)
    return ansdict
