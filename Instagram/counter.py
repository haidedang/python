import pickle

class counter:
    counterSlogan = 0 

def loadState(path):
    with open(path, 'rb') as handle:
        obj = pickle.load(handle)
        return obj


def saveState(obj):
    if obj.counterSlogan == 5:
        obj.counterSlogan = 0

    with open('counter.pickle', 'wb') as handle:
        pickle.dump(obj, handle, protocol= pickle.HIGHEST_PROTOCOL)


