# Text-Similarity-Score-Generator
This is a Text Similarity Score Generator. It takes in two different texts and compares how similar they are. 
To calculate the similarity score I am using Vector Space Model. This model creates a vector Space where each dimension represents a single word.
Words are taken from all the texts that are considered. One document is a single vector space. Each dimension of a single document vector represents 
how often this word appears in the text.To compare two documents a cosine similarity is used. This generates a value between 0 and 1, 0 meaning no 
similarity and 1 meaning perfect match.

#How to Use it?

### 1. Clone Code
```bash
git clone https://github.com/Abhishek-EE/Text-Similarity-Score-Generator.git
```

### 2. Install dependencies and Python Packages
It is recommended to use pip
```bash
pip install Flask numpy pandas
```
### 3. How to run the code

Open up the terminal and reach where runserver.py file is then run

```bash
python runserver.py
```
you should get a message like this
* Serving Flask app "Website" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 206-182-451
 * Running on http://localhost:5555/ (Press CTRL+C to quit)

clik on http:/localhost:5555/ to reach the server
Follow the instruction there to run the Text Similarity Algorithm
