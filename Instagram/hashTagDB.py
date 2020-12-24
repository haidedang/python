import pickle
import os
import random

# Initialization of the object 
hashtagDB = {
    "cottagecore" :{},
    "cottagecoreaesthetic": {},
     "cottage":{} ,
     "aesthetic": {},
     "moodboardaesthetic" :{},
     "vintageaesthetic" :{},
     "cottagecore": {},
     "cottagecoreaesthetic": {},
     "cottagecorefashion" : {},
     "cottagecorestyle" : {},
     "vintagedresses": {},
     "fairyfashion" : {},
     "princessdress": {},
     "princessdresses" : {},
     "praerigirl": {},
     "morikei": {},
     "morigirl" : {},
     "farmcoreaesthetic" : {},
     "farmcore": {}
}

def loadState():
    print('LOADING')
    print(os.getcwd())
    with open(os.getcwd() + '/hashTag.pickle', 'rb') as handle:
        try:
            obj = pickle.load(handle)
        except:
            obj = hashtagDB
        return obj

def saveState(obj):
    with open(os.getcwd()+ '/hashTag.pickle', 'wb') as handle:
        pickle.dump(obj, handle, protocol= pickle.HIGHEST_PROTOCOL)

