import pickle
import os

def loadState():
    print('LOADING')
    print(os.getcwd())
    with open(os.getcwd() + '/users.pickle', 'rb') as handle:
        try:
            obj = pickle.load(handle)
        except:
            obj = {}
        return obj

def saveState(obj):
    with open(os.getcwd()+ '/users.pickle', 'wb') as handle:
        pickle.dump(obj, handle, protocol= pickle.HIGHEST_PROTOCOL)
