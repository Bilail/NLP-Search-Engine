import sys
import Parsing
import Vocab
#from Parsing import *

titles, abstracts = Parsing.parsing("./CISI.ALL")

#print("title:", titles[0])
#print("abstract:", abstracts)

Vocab.Tf_idf(abstracts)

# TF et IDF
## TF pour chaque document

