import sys
import Parsing
import Vocab
import Prepocessing
import Helper
import time
import numpy as np


documents = Parsing.parseAll("./CISI.ALL")
queries = Parsing.parseQueries("./CISI.QRY")
results = Parsing.parseResults("./CISI.REL")
print(results)
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
Helper.print_queries_results(documents, documents_processed, queries, queries_processed, tf_idf_query_scores)

print("\n Testing scores for BM25 algorithm :")
Helper.print_queries_results(documents, documents_processed, queries, queries_processed, bm25_scores)

print("\n Computing success rate for the results for TF/IDF algorithm :")
Helper.print_success_rate(queries, results, tf_idf_query_scores)

print("\nComputing success rate for the results for BM25 algorithm :")
Helper.print_success_rate(queries, results, bm25_scores)
