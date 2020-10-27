# Problem 1
def division(a,b):
    try:
        print(a/b)
    except:
        print("Exception occurred")
        
division(5,0)

# Problem 2
subjects = ['Americans','Indians']
verbs = ['play','watch']
objects = ['Baseball','Cricket']

res = [i + ' ' + j + ' ' + k + '.' for i in subjects for j in verbs for k in objects]

for index in range(len(res)):
    print(res[index])
