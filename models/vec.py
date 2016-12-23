# math
from math import log


def to_unicode(terms):
    unicode_terms = []
    for term in terms:
        if (isinstance(term, str)):
            unicode_terms.append(unicode(term, 'utf-8'))
        else:
            unicode_terms.append(term)

    return unicode_terms


def train_vector(tone, term_voc, doc_voc, terms, features):
    "build vector"
    vector = [tone, {}]
    for feature_name in features.keys():
        index = term_voc.get_term_index(feature_name)
        vector[1][index] = features[feature_name]

    unicode_terms = to_unicode(terms)
    for term in unicode_terms:
        index = term_voc.get_term_index(term)
        vector[1][index] = tf(term, unicode_terms)*idf(term, term_voc, doc_voc)
    return vector


def tf(term, doc_terms):
    """
    Calculate tf measure for a document
    """
    return doc_terms.count(term)*1.0/len(doc_terms)


def idf(term, term_voc, doc_voc):
    """
    Calculate idf measure for vocabulary
    """
    return log(doc_voc.get_docs_count()*1.0 /
               doc_voc.get_term_in_docs_count(term))
