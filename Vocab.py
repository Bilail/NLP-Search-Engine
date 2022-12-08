import operator
import re
import math

def get_vocab(docs):
    # creer le vocabulaire (liste)
    voc = []
    dic_vocab = {}
    for doc in docs:
        text = doc
        text = text.split()
        voc = voc + text
        #dic_vocab[text] = 0

    # supprimer les char spéciaux
    """index = 0
    for word in voc:
        if (not word.isapha()):
            wordN = re.sub('[^A-Za-z0-9]+', '', word)
            voc[index] = wordN
        index = index + 1"""

    # supprimer les doublons
    voc = list(dict.fromkeys(voc))
    rev_voc = {}
    for idx, word in enumerate(voc):
        rev_voc[word] = idx
    return voc, rev_voc


def tf_idf_for_terms(docs, voc):

    nbDocs = len(docs)

    # calculer tfidf de chaque mot de chaque doc.
    TF = []
    IDF = []
    dic_TF = {}
    dic_IDF = {}
    term_scores = []

    docs_length = []
    docs_splitted = []
    for doc in docs:
        docs_splitted.append(doc.split())
        docs_length.append(len(docs_splitted[-1]))

    for word in voc:
        nbDocsWordOccured = 0
        word_tf = []
        for idx, doc in enumerate(docs):
            nbWords = docs_length[idx]
            nbOcc = docs_splitted[idx].count(word)
            if nbOcc > 0:
                nbDocsWordOccured += 1
            if nbWords > 0:
                word_tf.append(nbOcc / nbWords)
            else:
                word_tf.append(0)
        TF.append(word_tf)
        if nbDocsWordOccured > 0:
            IDF.append(math.log(nbDocs / nbDocsWordOccured))
        else:
            IDF.append(0)
        dic_TF[word] = TF[-1]
        dic_IDF[word] = IDF[-1]

    for word in voc:
        word_scores = []
        for doc_idx, doc in enumerate(docs):
            word_scores.append(dic_TF[word][doc_idx] * dic_IDF[word])
        term_scores.append(word_scores)

    return term_scores, TF, IDF, dic_TF, dic_IDF


def tf_idf_for_queries(term_scores, rev_voc, queries):
    query_scores = []
    for query in queries:
        local_scores = [0] * len(term_scores[0])
        words = query.split()
        for word in words:
            local_scores = list(map(operator.add, local_scores, term_scores[rev_voc[word]]))
        query_scores.append(local_scores)
    return query_scores


def bm25(dic_TF, dic_IDF, docs, queries):
    scores = []
    k1 = 1.2  # doit etre compris entre 1.2 et 2
    b = 0.75  # doit etre compris entre 0 et 1
    docs_length = []
    for doc in docs:
        docs_length.append(len(doc.split()))
    avgdl = sum(docs_length) / len(docs_length)

    for query in queries:
        query_scores = []
        words = query.split()
        for doc_idx, doc in enumerate(docs):
            sum_scores = 0
            for word in words:
                sum_scores += (dic_TF[word][doc_idx] * (k1+1)) / (dic_TF[word][doc_idx] + k1 * (1-b+b*(docs_length[doc_idx]/avgdl)))
            query_scores.append(sum_scores)
        scores.append(query_scores)
    return scores
