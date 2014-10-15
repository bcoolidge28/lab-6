#first 25 points

print "How many items in your first list"

total = 0

userInput = raw_input()

for x in range(int(userInput)):
    print 'How much is each item'
    userInput2 = int(raw_input())
    total = total + userInput2

print total

#Second 25 points

print 'How many items in your second list'

totalList = []

userInput3 = raw_input()

for i in range(int(userInput3)):
    print 'Now how much was each item?'
    userInput4 = int(raw_input())
    totalList.append(userInput4)

print totalList
print sum(totalList)

#Third 25 points

userInput5 = raw_input()

total = 1

for e in range(1,int(userInput5) + 1,1):
    total = total * e
print int(total) 

#Fourth 25 points

total = 1

userInput6 = raw_input()

for m in range(1,int(userInput6),1):
    if int(userInput6) % m == 0:
        print m