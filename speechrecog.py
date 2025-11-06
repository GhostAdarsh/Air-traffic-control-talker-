'''print("hello world")
# nat lang processing? ?? 

import spacy 
import nltk 
nltk.download('punkt')
import speech_recognition as sr 
from nltk.tokenize import sent_tokenize, word_tokenize
r = sr.Recognizer() 
example_string = "Muad'Dib learned rapidly because his first training was in how to learn"

# tokenise string: 
sent_tokenize(example_string)

aims - find text to analyse (this will be voice input)
preprocess text for analysis 

analyse text 

and then come up with a solution (in game movements)


'''


from nltk.tokenize import sent_tokenize, word_tokenize 

example_string = "Muad'Dib learned rapidly because his first training was in how to learn."
sent_tokenize(example_string)