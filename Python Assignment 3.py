# DLCVNLP - Assignment 3

# Problem 1
def myreduce(user_fn, lis):
    length = len(lis)
    if length < 2:
        raise Exception("List must contain at least two elements")
    else:
        output = user_fn(lis[0], lis[1])
        for index in range(2, length):
            output = user_fn(lis[index], output)
    return output

# Problem 2
def myfilter(filte, lis):
    output = []
    for index in range(len(lis)):
        if filte(lis[index]):
            output.append(lis[index])
    return output

# Problem 3
[letter*length for letter in 'xyz' for length in range(1,5)]
[letter*length for length in range(1,5) for letter in 'xyz']
[[x] for y in range(2, 5) for x in range(y,y+3)]
[[x for x in range(y,y+4)] for y in range(2, 6)]
[(y,x) for x in range(1,4) for y in range(1,4)]