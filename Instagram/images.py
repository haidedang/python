import pickle
import os
import random

def loadState():
    print('LOADING')
    print(os.getcwd())
    with open(os.getcwd() + '/images.pickle', 'rb') as handle:
        try:
            obj = pickle.load(handle)
        except:
            obj = {}
        return obj

def saveState(obj):
    with open(os.getcwd()+ '/images.pickle', 'wb') as handle:
        pickle.dump(obj, handle, protocol= pickle.HIGHEST_PROTOCOL)

def init():
    obj = {} 
    folderPath = os.getcwd()+ '/images' 
    print(folderPath)
    i=0
    for fileName in os.listdir(folderPath):
        i +=1
        obj[fileName] = False
        print(fileName)
        # img = cv2.imread(os.path.join(folderPath,filename))
        # if img is not None:
            # print(filename)
            # dest = /posting or /finished
            # shutil.move(os.path.join(folderPath,filename), os.getcwd() + '/' + dest)
            #print(os.path.join(folderPath,filename), os.getcwd() + '/' + dest)
            #break
      
        #rename file 
    #save that file to pickle 
    saveState(obj)
    """ fileName = random.choice(list(obj.keys()))
    print('old name ', fileName)
    newFileName= '0'+fileName
    print('new Name', newFileName)
    os.rename(os.path.join(folderPath,fileName), os.path.join(folderPath,newFileName))
    'FINISHED POSTING IT, RENAME IT BACK.' """
           
""" init()
test = loadState()
print(test) """