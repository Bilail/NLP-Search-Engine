def get_dico(doc):
    try:
        DICO = open(doc, 'r', encoding="utf-8").read()
    except:
        DICO = open(doc, 'r').read()

    return DICO


def remove_accents(input_str):
    """This method removes all diacritic marks from the given string"""
    norm_txt = unicodedata.normalize('NFD', input_str)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


def clean_sentence(texte):
    # Replace diacritics
    texte = remove_accents(texte)
    # Lowercase the document
    texte = texte.lower()
    # Remove Mentions
    texte = re.sub(r'@\w+', '', texte)
    # Remove punctuations
    texte = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', texte)
    # Remove the doubled space
    texte = re.sub(r'\s{2,}', ' ', texte)
    # remove whitespaces at the beginning and the end
    texte = texte.strip()

    return texte


def tokenize_sentence(texte):
    # clean the sentence
    texte = clean_sentence(texte)
    # tokenize
    liste_words = texte.split()
    # return
    return liste_words


def strip_apostrophe(liste_words):
    get_radical = lambda word: word.split('\'')[-1]
    return list(map(get_radical, liste_words))


def pre_process(sentence):
    # remove '_' from the sentence
    sentence = sentence.replace('_', '')

    # get words fro the sentence
    liste_words = tokenize_sentence(sentence)
    # cut out 1 or 2 letters ones
    liste_words = [elt for elt in liste_words if len(elt) > 2]
    # prendre le radical après l'apostrophe
    liste_words = strip_apostrophe(liste_words)
    print('\nsentence to words : ', liste_words)
    return liste_words