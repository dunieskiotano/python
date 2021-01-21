# nested loops
import os

os.system('clear')

counteri = 0
counterj = 0
counterx = 0
countery = 0

for i in range(1, 11): # OUTER LOOP => loops 10 times
    print(' ')
    print(f'\033[1;31;40mi.................... {i}')
    counteri += 1
    for j in range(1, 6): # INNER LOOP => loops 50 times in total
        print(f'\033[1;33;40mj................ {j}')
        counterj += 1
        for x in range(1, 4):
            print(f'\033[1;34;40mx............{x}')
            counterx += 1
            for y in range(1, 3):
                print(f'\033[1;35;40my.....{y}')
                countery+=1
# First iteration
    # i loops first time (1)
        # j loops the first time (1)
            # x loops the first time (1)
                # y loops 2 times
            # x loops for the second time (2)
                # y loops 2 times
            # x loops for the third time (3)
                # y loops 2 times
        # j loops for the second time (2)
            # x loops the first time (1)
                # y loops 2 times
            # x loops for the second time (2)
                # y loops 2 times
            # x loops for the third time (3)
                # y loops 2 times

print('Counter i => ', counteri)
print('Counter j => ', counterj)
print('Counter x => ', counterx)
print('Counter y => ', countery)


counterz = 0 
counterw = 0

for z in range(1,20):
    print(f'\033[1;34;40mz............{z}')
    counterz +=1 
    for w in range(1,10):
        print(f'\033[1;35;40mw..........{w}')
        counterw +=1 

print(f'Counter z: ', counterz)
print(f'Counter w: ', counterw)

# counterz = 1, counterw = 9