# Text Processing Assignment

import re

# Problem 1
print("Problem 1")
sentences = ["xyz@gmail.com", "abc@yahoo.com", "xyz@hotmail.com",
             "abc@ineuron.ai", "xyz@outlook.com"]

for sentence in sentences:
    x = re.split("@", sentence)
    print(x[1])

# Problem 2
print("\nProblem 2")
sentence = "New Delhi is the capital of India"
print(re.sub(r'New', '', sentence))

# Problem 3
print("\nProblem 3")
sentence = "In India, 184 people got affected with Corona virus and 4 are died."
sentence = sentence.lower()

match = re.findall("\d+", sentence)
for str in match:
    sentence = re.sub(str, '', sentence)
    
print('Sentence after processing: ', sentence)

# Problem 4
print('\nProblem 4')
import spacy
sp = spacy.load('en_core_web_sm')
sentence = 'I hope that, when I have built up my savings, I will be able to travel to Hawai.'
print('Sentence: ', sentence)
sentence = sp(sentence)

print("\nTokenization")
for word in sentence:
    print(word.text)
    
print('\nStemming')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
for token in sentence:
    print(token.text + ' --> ' + stemmer.stem(token.text))
    
print('\nLemmatization')
for word in sentence:
    print(word.text + ' --> ' + word.lemma_)

# Problem 5
print('\nProblem 5')

sentence = 'I love NLP, not you'
print([s[0] for s in sentence.split()])
