import pickle
import os
class counter:
    counterSlogan = 0 

def loadState(path):
    print('LOADING')
    print(os.getcwd())
    with open(os.getcwd() + '/' + path, 'rb') as handle:
        obj = pickle.load(handle)
        return obj

def saveState(obj):
    if obj.counterSlogan == 5:
        obj.counterSlogan = 0

    with open(os.getcwd() + '/counter.pickle', 'wb') as handle:
        pickle.dump(obj, handle, protocol= pickle.HIGHEST_PROTOCOL)
