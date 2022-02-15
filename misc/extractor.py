import os, json

def list_attributes(file):
    if validate(file):
        with open(os.path.abspath(file), encoding='utf8') as f:
            data = json.load(f)
            for n in data[0].keys():
                print(n, '', type(n), '', data[0].get(n))

def extract_from_tweets(file, attribute):
    if validate(file):
        with open(os.path.abspath(file), encoding='utf8') as f:
            data = json.load(f) 
            for tweet in data:  
                try:
                    print(f"{tweet['id']}, {attribute}: {tweet[attribute]}")  
                except Exception as e:
                    raise e

def validate(file):
    if os.path.isfile(file):
        return True
    elif os.path.exists(file):
        print("Could not validate filetype. Please submit a .json file.") 
    else:
        print("File does not seem to exist. Please check that the path is correct.")  
    return False


#extract_from_tweets('data', 'mentions')
list_attributes('data')