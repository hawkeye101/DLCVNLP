# Assignment 2
max = 5
no_of_rows = 2*max - 1
for i in range(no_of_rows):
    no_of_objects = no_of_rows-i if i>max-1 else i+1
    for j in range(no_of_objects):
        print('*', end = " ")
    print('\n')
    
# Assignment 3
word = input()[::-1]
print(word)