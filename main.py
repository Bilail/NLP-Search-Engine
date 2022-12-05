import sys
import Parsing
import Vocab
#from Parsing import *

titles_all, abstracts_all = Parsing.parseAll("./CISI.ALL")
abstract_query = Parsing.parseQueries("./CISI.QRY")

#print(abstract_query)
#print(len(abstract_query))

#print("title:", len(titles_all))
#print("abstract:", len(abstracts_all))

vocab = Vocab.get_vocab(abstracts_all)

#TF_ALL, IDF_ALL = Vocab.Tf_idf(abstracts_all, vocab)
#TF_query, IDF_query = Vocab.tf_idf(abstract_query, vocab)


