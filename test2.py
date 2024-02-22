import requests

def engdict(query):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + query
    response = requests.get(url)
    # print(response)
    apidata = response.json()
    if len(apidata)==3 and apidata['title'] == 'No Definitions Found': 
        print("ERROR")
        return
    # print(apidata)
    
    # for key in apidata: 
    #     for i in key:
    #         print(i)
            
    ansdict = {}

    word = apidata[0]["word"]
    phonetic = apidata[0]["phonetic"]
    # print(apidata[0]["meanings"])
    meaningslist1 = apidata[0]["meanings"][0]
    partofspeech1 = meaningslist1['partOfSpeech']
    
    ansdict.setdefault(partofspeech1,[])
    # print(partofspeech1)

    definitionmasterlist1 = meaningslist1['definitions']

    # print(definitionmasterlist)
    definitionlist1 = []
    examplelist1= ['Examples']

    for i in definitionmasterlist1: 
        # print(i)
        definitionlist1.append(i['definition'])
        if 'example' in i:
            examplelist1.append(i['example'])  
    ansdict[partofspeech1].append(definitionlist1)
    ansdict[partofspeech1].append(examplelist1)
    # print(definitionlist1)
    # print(examplelist1)
    
    if len(apidata[0]["meanings"])>1: 
        meaningslist2 = apidata[0]["meanings"][1]
        partofspeech2 = meaningslist2['partOfSpeech']
        # print(partofspeech2)

        
        definitionmasterlist2 = meaningslist2['definitions']
        definitionlist2 = []
        examplelist2 = ['Examples']
        for i in definitionmasterlist2: 
        # print(i)
            definitionlist2.append(i['definition'])
            if 'example' in i:
                examplelist2.append(i['example'])  
        # print(definitionlist2)
        # print(examplelist2)
        ansdict.update({partofspeech2:[]})
        ansdict[partofspeech2].append(definitionlist2)
        ansdict[partofspeech2].append(examplelist2)

    print(ansdict)
    return ansdict
