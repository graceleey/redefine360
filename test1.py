import pip._vendor.requests
import hgtk

apikey = '3D7B3083C9AC9663D8FB66AD207A44E0'

#returning list of items 
#value: text
#s: start
#e: end
def returnList(value, s, e):
    
    if s in value:
        temp = value.split(s)
        value = []
        for i in range(0, len(temp)):
            if e in temp[i]: value.append(temp[i][:temp[i].find(e)])
    else:
        value = []
    return value

#returns just the item 
def returnItem(value, s, e):
    if s in value:
        value = value[value.find(s)+len(s):]
        if e in value: value = value[:value.find(e)]
    return value

#returns the translated definitions/items in a list 
def returnTranslation(value):
    for i in range(len(value)):
        if "CDATA" in value[i]:
            value[i] = value[i][value[i].find("CDATA")+len("CDATA")+1:]
            if "]" in value[i]: value[i] = value[i][:value[i].find("]")]
    return value

#checks if the word entered exists in the API dictionary; returns the data in XML 
def checkexists(query):
    # print("getting checkexists" + query)
    url = 'https://krdict.korean.go.kr/api/search?key=' + apikey + '&translated=y&trans_lang=1&part=word&sort=popular&num=100&pos=1&q=' + query
    response = pip._vendor.requests.get(url)
    ans = ''

    words = returnList(response.text,'<item>','</item>')
    # print(words)
    for w in words:
        word = returnItem(w,'<word>','</word>')
        pos = returnItem(w,'<pos>','</pos>')
        if len(word) >= 1 and pos == '명사' and word == query: ans += w
        # print("printing ans: " + ans)
    # print("getting ans??" + ans)
    if len(ans)>0:
        return ans
    else:
        return ''

def findword(word): 
    url = 'https://krdict.korean.go.kr/api/search?key=' + apikey + '&translated=y&trans_lang=1&part=word&pos=1&q=' + word
    response = pip._vendor.requests.get(url)
    ans = []
    words = returnList(response.text,'<item>','</item>')

    for w in words:
        word = returnItem(w,'<word>','</word>')
        print(word)
        pos = returnItem(w,'<pos>','</pos>')
        if len(word) > 1 and pos == '명사':
            ans.append(w)
        # print(ans) 
    print(returnItem(word, '<definition>', '</definition>'))


#returning the items in the list 
def listreturn(list):
    templist = [] 
    for i in range(len(list)):
        templist.append(list[i])
    return templist

def main(query):
    print("running kr.main()")
    # query = input('input a word: ')
    ans = checkexists(query)
    # print("printing answer:" +ans)

    #returns the list with multiple definitions in Korean
    kordeflist = returnList(ans, '<definition>', '</definition>')
    #returns the list with multiple words translated in English
    transwordlist = returnTranslation(returnList(ans, '<trans_word>', '</trans_word>'))
    #returns the list with multiple definitions in English
    transdfnlist = returnTranslation(returnList(ans, '<trans_dfn>', '</trans_dfn>'))
    a = listreturn(kordeflist)
    b = listreturn(transwordlist)
    c = listreturn(transdfnlist)
    print(a)
    print(b)
    print(c)
    return (a,b,c)




