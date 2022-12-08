import sys
import Parsing
import Vocab
import Prepocessing
import time
import numpy as np


documents = Parsing.parseAll("./CISI.ALL")
queries = Parsing.parseQueries("./CISI.QRY")

print("\nProcessing documents ...")
documents_processed = Prepocessing.clean(documents)
print("\nComputing the vocab ...")
start_time = time.time()
vocab, reverse_vocab = Vocab.get_vocab(documents_processed)
print("--> processed in %.2fs seconds" % (time.time() - start_time))

#print(vocab)
print(f"--> size of the vocabulary : {len(vocab)}")

print("\nComputing TF/IDF for each term ...")
start_time = time.time()
tf_idf_term_scores, TF_ALL, IDF_ALL, dic_TF, dic_IDF = Vocab.tf_idf_for_terms(documents_processed, vocab)
print("--> processed in %.2fs seconds" % (time.time() - start_time))

print("\nProcessing queries ...")
queries_processed = Prepocessing.process_queries(queries, vocab)

print("\nComputing TF/IDF scores for queries ...")
start_time = time.time()
tf_idf_query_scores = Vocab.tf_idf_for_queries(tf_idf_term_scores, reverse_vocab, queries_processed)
print("--> processed in %.2fs seconds" % (time.time() - start_time))

print("\nComputing BM25 scores ...")
start_time = time.time()
bm25_scores = Vocab.bm25(dic_TF, dic_IDF, documents_processed, queries_processed)
print("--> processed in %.2fs seconds" % (time.time() - start_time))

print("\n Testing scores for TF/IDF algorithm :")
for i in range(0, 3):
    print(f"\n########### Query n°{i+1} ###########")
    print(f"Query : \"{queries[i]}\" :")
    print(f"Query processed : \"{queries_processed[i]}\" :")
    arr = np.array(tf_idf_query_scores[i])
    res = arr.argsort()[-3:][::-1]
    print(f"--> sorted : {sorted(tf_idf_query_scores[i], reverse=True)}")
    for idx, r in enumerate(res):
        print(f"--> Result n°{idx+1} (doc_id = [{r+1}], score = {arr[r]}) : {documents[r].strip()}")
        print(f"--> Result processed : {documents_processed[r]}")


print(tf_idf_term_scores[reverse_vocab["definition"]][1132])

print("\n Testing scores for BM25 algorithm :")
for i in range(0, 3):
    print(f"\n########### Query n°{i+1} ###########")
    print(f"Query : \"{queries[i]}\" :")
    arr = np.array(bm25_scores[i])
    res = arr.argsort()[-3:][::-1]
    for idx, r in enumerate(res):
        print(f"--> Result n°{idx+1} (doc_id = [{r+1}]) : {documents[r].strip()}")
