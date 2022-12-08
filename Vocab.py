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

    return voc


def tf_idf(docs, voc):

    nbDocs = len(docs)

    # calculer tfidf de chaque mot de chaque doc.
    TF = []
    IDF = []
    dic_TF = {}
    dic_IDF = {}
    docs_length = []
    for doc in docs:
        docs_length.append(len(doc.split()))

    for word in voc:
        nbDocsWordOccured = 0
        word_tf = []
        for idx, doc in enumerate(docs):
            nbWords = docs_length[idx]
            nbOcc = doc.count(word)
            if nbOcc > 0:
                nbDocsWordOccured += 1
            if nbWords > 0:
                word_tf.append(nbOcc / nbWords)
            else:
                word_tf.append(0)
        TF.append(word_tf)
        if nbDocsWordOccured > 0:
            IDF.append(math.log(nbDocs / nbDocsWordOccured, 2))
        else:
            IDF.append(0)
        dic_TF[word] = TF[-1]
        dic_IDF[word] = IDF[-1]

    """TF = [[]]
    IDF = []
    dic_TF = {}
    dic_IDF = {}
    for word in voc:
        occ = 0
        occ_doc = 0

        tf_idf = 0
        id = 0

        for doc in docs:
            if (word in doc):
                occ_doc += 1
            occ = doc.count(word)

            TF[id].append(float(occ) / (len(docs)))
            dic_TF[word] = float(occ) / (len(docs))
        IDF.append(math.log((len(docs)) / float(occ_doc),2))
        dic_IDF[word] = math.log((len(docs)) / float(occ_doc),2)

        id += 1"""

    return TF, IDF, dic_IDF, dic_TF


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
