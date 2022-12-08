import re
import unicodedata
import string
import nltk
"""nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def process_queries(queries, vocab):
    queries = clean(queries)
    # Suppression des mots des queries qui ne sont pas dans le vocabulaire
    res = []
    for query in queries:
        words = query.split()
        query = ""
        for word in words:
            if word in vocab:
                query += word + " "
        res.append(query)
    return res


def remove_accents(input_str):
    """This method removes all diacritic marks from the given string"""
    norm_txt = unicodedata.normalize('NFD', input_str)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


def clean(textes):
    res = []
    for texte in textes:
        # Replace diacritics
        texte = remove_accents(texte)
        # Lowercase the document
        texte = texte.lower()
        # Remove punctuations
        texte = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', texte)
        # Remove stop-words
        texte = remove_stop_words(texte)
        # Lemmatization of the text
        texte = lemmatize(texte)
        res.append(texte)
    return res


def remove_stop_words(text):
    word_tokens = word_tokenize(text)
    filtered_text = ""
    for word in word_tokens:
        if word not in stop_words:
            filtered_text += word + " "
    return filtered_text


def lemmatize(text):
    word_tokens = word_tokenize(text)
    text = ' '.join([lemmatizer.lemmatize(w) for w in word_tokens])
    return text
