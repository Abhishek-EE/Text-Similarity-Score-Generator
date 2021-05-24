import numpy as np
import pandas as pd
from numpy.linalg import norm
import copy

''' Steps involved to do text Matching 
1. Parse the document or get the text

2. Preprocessing the text ->
    Convert it to lower case
    use stemming to get important words working in your favor

3. create a list of all the words which are in the two documents

4. vectorize both the documents

5. calculate the dot product of both the vectors

6. return the dot product of both the vectors


'''

class SimiliariytScoreGenerator:
    
    def __init__(self,doc1,doc2):
        self.doc1 = doc1
        self.doc2 = doc2
        self.set_of_words = set()
        self.vec1 = []
        self.vec2 = []
        self.score = 0
        self.stop_words = ['I','You','are','a','an','the',',','.']

    def preprocess(self):
        self.doc1 = self.doc1.split(" ")
        self.doc2 = self.doc2.split(" ")
        # print(self.doc1)
        # print(self.doc2)

    
    def word_map(self):
        self.set_of_words.update(set(self.doc1))
        self.set_of_words.update(set(self.doc2))
        self.set_of_words = sorted(self.set_of_words)
        self.set_of_words = dict.fromkeys(self.set_of_words,0)
        # print(self.set_of_words)
    
    def vectorize(self,l):
        vec = copy.deepcopy(self.set_of_words)
        # print(vec)
        for i in l:
            vec[i] += 1
        df = pd.DataFrame(vec,index=[0])
        vec = df.to_numpy()
        return vec

        
        

    def dot_product(self):
        self.vec1 = self.vec1.flatten(order = 'C')
        self.vec2 = self.vec2.flatten(order = 'C')
        # print(self.vec1)
        # print(self.vec2)
        self.score = np.dot(self.vec1,self.vec2)/(norm(self.vec1)*norm(self.vec2))

    
    def calculate(self):
        self.preprocess()
        self.word_map()
        self.vec1 = self.vectorize(self.doc1)
        self.vec2 = self.vectorize(self.doc2)
        self.dot_product()
        return self.score
    
    
