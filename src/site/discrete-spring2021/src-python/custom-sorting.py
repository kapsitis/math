# https://betterprogramming.pub/advanced-sorting-in-python-using-lambdas-and-custom-functions-410b5780fb07

def custom_compare1(x1, x2):
    if (len(x1['activity']) < len(x2['activity'])):
        return -1
    elif (len(x1['activity']) > len(x2['activity'])):
        return 1
    elif x1['activity'] < x2['activity']:
        return -1
    elif x1['activity'] > x2['activity']:
        return 1
    else:
        return 0
        


def main(): 
    mylist = ['aaaa','bbb','cc']
    activities = [
    {'order': 0, 'day': 'Mon', 'activity': 'Baseball'},
    {'order': 1, 'day': 'Tue', 'activity': 'Swim'}, 
    {'order': 2, 'day': 'Wed', 'activity': 'Alpinism'}, 
    {'order': 3, 'day': 'Thu', 'activity': 'Alpinism'}, 
    {'order': 4, 'day': 'Thu', 'activity': 'Dance'}, 
    {'order': 5, 'day': 'Thu', 'activity': 'Football'}
    ]
    sorted_activities = sorted(activities, key=lambda x: (x['activity'], x['day']), reverse=False)
    for activ in sorted_activities: 
        print(activ)
        


    


if __name__=='__main__':
    main()
