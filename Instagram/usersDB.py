import pickle
import os

def loadState(path):
    print('LOADING')
    print(os.getcwd())
    with open(os.getcwd() + '/'+ path, 'rb') as handle:
        try:
            obj = pickle.load(handle)
        except:
            obj = {}
        return obj

def saveState(obj, path):
    with open(os.getcwd()+ '/' + path, 'wb') as handle:
        pickle.dump(obj, handle, protocol= pickle.HIGHEST_PROTOCOL)
