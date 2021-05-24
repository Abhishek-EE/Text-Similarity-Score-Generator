# Text-Similarity-Score-Generator
This is a Text Similarity Score Generator. It takes in two different texts and compares how similar they are. 
To calculate the similarity score I am using Vector Space Model. This model creates a vector Space where each dimension represents a single word.
Words are taken from all the texts that are considered. One document is a single vector space. Each dimension of a single document vector represents 
how often this word appears in the text.To compare two documents a cosine similarity is used. This generates a value between 0 and 1, 0 meaning no 
similarity and 1 meaning perfect match.
