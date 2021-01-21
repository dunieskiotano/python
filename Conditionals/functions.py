
# a file that contains a function

def conditional_decided(currentStatus, lowGallonQt):
    if(currentStatus >= 12 and currentStatus <= 15):
        print("You are good, and I would probably say that you're perfect")
    elif (currentStatus >= 3 and currentStatus <= 11):
        print('We think you should be thinking about some replenishmenrt')
    elif (currentStatus > lowGallonQt and currentStatus < 3):
        print('My friend, you are about to start running on fumes')
    elif (currentStatus == lowGallonQt):
        print('Low fuel warning has been turned on')
    else:
        print('Oh my God, my car just stopped in the middle of the highway')

    
def printHello(text):
    print('Your text is {}'.format(text))