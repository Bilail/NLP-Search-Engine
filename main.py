import sys
import Parsing
import Vocab
import Prepocessing
#from Parsing import *
import time
import numpy as np


titles_all, abstracts_all = Parsing.parseAll("./CISI.ALL")
abstract_query = Parsing.parseQueries("./CISI.QRY")

#print(abstract_query)
#print(len(abstract_query))

#print("title:", len(titles_all))
#print("abstract:", len(abstracts_all))

print("Computing the vocab ...")
start_time = time.time()
vocab = Vocab.get_vocab(abstracts_all)
print("--- processed in %.2fs seconds ---" % (time.time() - start_time))

print("Computing the TF / IDF ...")
start_time = time.time()
TF_ALL, IDF_ALL, dic_IDF, dic_TF = Vocab.tf_idf(abstracts_all, vocab)
print("--- processed in %.2fs seconds ---" % (time.time() - start_time))
#TF_query, IDF_query = Vocab.tf_idf(abstract_query, vocab)

#print("dic de IDF : ", dic_IDF)

"""for i in range(0,10):
    print("IDF de :", vocab[i], " est de : ", IDF_ALL[i])
    #print("TF de :", vocab[i], " dans le doc 1 est de : ", IDF_ALL[1][i])
"""

# Suppression des mots des queries qui ne sont pas dans le vocabulaire
queries = []
for query in abstract_query:
    words = query.split()
    query = ""
    for word in words:
        if word in vocab:
            query += word + " "
    queries.append(query)

print("Computing BM25 scores ...")
start_time = time.time()
bm25_scores = Vocab.bm25(dic_TF, dic_IDF, abstracts_all, queries)
print("--- processed in %.2fs seconds ---" % (time.time() - start_time))

print("\n Testing scores for BM25 algorithm :")
for i in range(0, 3):
    print(f"\n########### Query n°{i+1} ###########")
    print(f"Query : \"{abstract_query[i]}\" :")
    arr = np.array(bm25_scores[i])
    print(bm25_scores[i])
    res = arr.argsort()[-3:][::-1]
    for idx, r in enumerate(res):
        print(f"Result n°{idx+1} (doc_id = [{r+1}]) : {abstracts_all[r].strip()}")

