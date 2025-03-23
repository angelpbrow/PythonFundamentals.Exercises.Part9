import json
import os
import pickle


#function to turn json file into python object -- json.load()
def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    print (data)
    return data

def read_all_json_files(file_path):
    #given a file_path. for the files in file_path, create a new path
    #read the new file path and place in a variable
    #append the results in a list
    result = []
    for file in os.listdir(file_path):
        new_file_path = "%s/%s" % (file_path, file)
        data = read_json(new_file_path)
        result.append(data)
    return result

def write_pickle(file_path, data):
    obj = pickle.dumps(data)
    with open('super_smash_characters.pickle', 'w') as w:
        w.write(obj)


def load_pickle(file_path):
    with open(file_path, 'r') as f:
        obj = (pickle.load(f))
        print(obj)




read_json('/Users/angel/Desktop/Projects/Exercise9_2025/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json')