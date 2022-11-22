import re
import math

def Tf_idf(docs):

    # creer le vocabulaire (liste)
    voc = []
    for doc in docs:
        text = doc
        text = text.split()
        voc = voc + text



    # supprimer les char spéciaux
    """index = 0
    for word in voc:
        if (not word.isapha()):
            wordN = re.sub('[^A-Za-z0-9]+', '', word)
            voc[index] = wordN
        index = index + 1"""

    # supprimer les doublons
    vocabulaire = []

    for element in voc:
        if element not in vocabulaire:
            vocabulaire.append(element)

    #print("vocabulaire de : ", vocabulaire)

    nbDocs = len(docs)
    # calculer tfidf de chaque mot de chaque doc.


    TF = []
    IDF = []
    TF_IDF = []

    # on parcours notre voc et on calcule TFIDF de ce mot dans notre doc
    """ind = 0
    for doc in docs:
        text = doc
        nbwords = len(text.split())
        for word in vocabulaire:
            ######calculer le nb de docs dans lequel un mot est apparu#######
            nbDocsWordOccured = 0
            for doc in docs:
                if (word in text):
                    nbDocsWordOccured = nbDocsWordOccured + 1
            #########################################
            nboccurence = text.count(word)
            tf = nboccurence / nbwords
            TF.append(tf)
            if (nbDocsWordOccured != 0):
                idf = nbDocs / nbDocsWordOccured
            else :
                idf = 0
            IDF.append(idf)
            TF_IDF.append(tf * idf)
"""

    for word in vocabulaire:
        occ = 0
        occ_doc = 0
        TF = [[]]
        IDF = []
        tf_idf = 0
        id = 0

        for doc in docs:
            if (word in doc):
                occ_doc += 1
            occ = doc.count(word)

            TF[id].append(float(occ) / (len(docs)))
        IDF.append(math.log((len(docs)) / float(occ_doc),2))


        id += 1

        print(TF)
