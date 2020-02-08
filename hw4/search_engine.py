# Name: Adam Klingler
# Section: AB
# Description: This file contains the SearchEngine class, which represents


# imports here
import math
import os
import re
from document import Document


class SearchEngine:
    '''
    This class represents a bunch of documents. Can be searched based
    on relavancy to a search query.
    '''

    def __init__(self, directory):
        '''
        Constructs the search engine for the given directory.
        '''
        self._all_terms = dict()
        self._total_documents = 0  # speeds up _calculate_idf later

        for file_name in os.listdir(directory):
            self._total_documents += 1

            current_document = Document(directory + '/' + file_name)
            current_words = current_document.get_words()

            for word in current_words:
                if word in self._all_terms.keys():
                    # values for all_terms is a list
                    self._all_terms[word].append(current_document)
                else:
                    self._all_terms[word] = [current_document]

    def _calculate_idf(self, term):
        '''
        This function takes in a term and calculates the inverse document
        frequency for that term.
        '''
        if term in self._all_terms.keys():
            documents = self._all_terms[term]

            return math.log(self._total_documents/len(documents))
        else:
            # term not in any documents
            return 0

    def search(self, query):
        '''
        This function takes in a query and returns a list document names that
        contain at least part of the query, sorted by relevance.
        '''
        sub_queries = query.split()
        doc_scores = dict()

        for sub_query in sub_queries:
            sub_query = re.sub(r'\W+', '', sub_query)
            sub_query = sub_query.lower()
            if sub_query not in self._all_terms.keys():
                # abort this loop, start next one
                continue

            documents = self._all_terms[sub_query]
            for document in documents:
                tdidf = document.term_frequency(sub_query) * \
                        self._calculate_idf(sub_query)
                document_name = document.get_file_name()

                if document_name in doc_scores.keys():
                    # Add the tdidf of this sub query to the score
                    doc_scores[document_name] += tdidf
                else:
                    # First time seeing this document, initialize with this
                    # tdidf
                    doc_scores[document_name] = tdidf

        if doc_scores == dict():
            # No part of the query was found, return None per the spec
            return None

        documents = doc_scores.items()
        # documents is a list of (key, value) tuples, where
        # the key is the document name and the value is the
        # summed tdidf values over every sub query

        # Sort by tdidf, which is the second index, [1] of the tuple t
        documents = sorted(documents, key=lambda t: t[1], reverse=True)

        results = list()
        for document in documents:
            # document name is the first index, [0] of the tuple document
            results.append(document[0])
        return results
