import sys
import Parsing
import Vocab
#from Parsing import *

titles_all, abstracts_all = Parsing.parsing("./CISI.ALL")
asbtract_query = Parsing.parsing("./CISI.QRY")

#print("title:", titles[0])
#print("abstract:", abstracts)

vocab = Vocab.get_vocab(abstracts_all)

TF_ALL, IDF_ALL = Vocab.Tf_idf(abstracts_all, vocab)
TF_query, IDF_query = Vocab.tf_idf(vocab)


