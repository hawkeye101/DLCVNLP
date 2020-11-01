# Assignment 4

# Problem 1
class Triangle(object):
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
            
    @classmethod
    def from_input(cls):
        return cls(
            input("Enter a: "),
            input("Enter b: "),
            input("Enter c: "),
        )
class Area(Triangle):
    def area_compute(self):
        a = self.a
        b = self.b
        c = self.c
        if a + b < c or b + c < a or c + a < b:
            raise Exception('invalid triangle')
        s = (a+b+c)/2
        area_val = (s*(s-a)*(s-b)*(s-c))**0.5
        print(area_val)

tri_data = Triangle.from_input()
tri_area = Area(**tri_data.__dict__)
tri_area.area_compute()

# Problem 2
def filter_long_words(list_of_words, n):
    output = []
    for index in range(len(list_of_words)):
        if len(list_of_words[index]) > n:
            output.append(list_of_words[index])    
    return output

input = ['apple','orange','mango','banana']
print(filter_long_words(input, 5))

# Problem 3
def len_of_words(list_of_words):
    output = [len(list_of_words[index]) for index in range(len(list_of_words))]
    return output

input = ['ab','ce','erty']
print(len_of_words(input))

# Problem 4
def is_vowel(input_char):
    if input_char in ['a','e','i','o','u']:
        return 1
    else:
        return 0
    
print(is_vowel('e'))
print(is_vowel('b'))