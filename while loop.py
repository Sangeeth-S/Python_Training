"""
import time

sets = 0 #5
count = 0 #20

while sets < 5:
    sets += 1
    print('sets {}' .format(sets))

    while count < 20:
        count += 1
        print('count {}' .format(count))
        
"""    


mark = int(input('Enter Mark : '))

if mark < 40:
    print('Fail')
elif mark >= 50 and mark <= 75:
    print('Average')
elif mark >= 75 and mark <= 99:
    print('Good')
elif mark == 100:
    print('Excelent')
else:
    print('Improper format')

    

x = 5
y = 10

if x > y:
    print ("True")
    
