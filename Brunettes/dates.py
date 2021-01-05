from datetime import date
import datetime
import usersDB
user1 = "hassan"

def deFollowUsers():
    following = usersDB.loadState('following.pickle')
    # run once at the end of a day
    # today = datetime.date.today()
    today = date(2021, 1, 12)
    weekBefore = today - datetime.timedelta(days=7)
    print(weekBefore)
    try:
        print('access week ago', following[str(weekBefore)])
        for elem in following[str(weekBefore)]: 
            print('deFollow', elem)
        following[str(weekBefore)].append('defollowed')
        usersDB.saveState(following, 'following.pickle')
    except:
        print('one week has not passed yet')

def followUser(user): 
    print('click Follow button of user')
    

    # load userList 
    following = usersDB.loadState('following.pickle')

    # following is false and empty object in first iteration
    today = datetime.date.today() 

    # check the object wether elements for this date exist 
    try:
        print('accessing date and show length', len(following[str(today)]))
        following[str(today)].append(user)
    except: 
        # if not existent, init empty array for that day
        print('first user of today. Init new array and save user')
        following[str(today)] = []
        following[str(today)].append(user)
    print('saving new followers...')
    usersDB.saveState(following, 'following.pickle')
    

# check for private by checking first post of user 
# follow user 
# like and comment 


deFollowUsers()




