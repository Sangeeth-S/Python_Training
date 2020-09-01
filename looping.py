import time

switch = 1
count = 0

while switch:
    print('ON')
    time.sleep(2)
    print('OFF')
    time.sleep(2)
    count += 1
    switch = input('Enter switch state in True or False :')
    if switch == 'True':
        switch = 1
    else:
        switch = 0

print(count)

