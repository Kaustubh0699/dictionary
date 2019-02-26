import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def search_meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0 :
        yn = input("Did you mean %s ? Type YES if true and NO if not: " %get_close_matches(word,data.keys())[0])
        if(yn == "YES" or yn =="yes" or yn =="Yes"):
            return data[get_close_matches(word,data.keys())[0]]
        elif(yn == "NO" or yn =="no" or yn =="No"):
            print("Please double check the input word")
        else:
            print("Irrelevant Entry")
    else:
        print("Word Not Found in Dictionary")

word = input("Enter a Word: ")
output = search_meaning(word) 
if(type(output)== list):
     for i in output:
         print(i)
else:
    print(output)
