import sys
import Parsing
import Vocab
import Prepocessing
#from Parsing import *

titles_all, abstracts_all = Parsing.parseAll("./CISI.ALL")
abstract_query = Parsing.parseQueries("./CISI.QRY")


#print(abstract_query)
#print(len(abstract_query))

#print("title:", len(titles_all))
#print("abstract:", len(abstracts_all))

vocab = Vocab.get_vocab(abstracts_all)

TF_ALL, IDF_ALL,dic_IDF, dic_TF= Vocab.Tf_idf(abstracts_all, vocab)
#TF_query, IDF_query = Vocab.tf_idf(abstract_query, vocab)

print("dic de IDF : ", dic_IDF);

for i in range(0,10):
    print("IDF de :", vocab[i], " est de : ", IDF_ALL[i])
    #print("TF de :", vocab[i], " dans le doc 1 est de : ", IDF_ALL[1][i])

