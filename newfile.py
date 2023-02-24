# incorporating a boolean that equates numbers#

your_score = int(input("what is your score "))
print("your score is " + str(your_score))

passing_score = 80
if your_score >= passing_score:
    studentPassed = True
else:
    studentPassed = False

if studentPassed:
    print("congratulations! you passed")
else:
    print('you failed you loser')
