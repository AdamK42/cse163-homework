# Name: Adam Klingler
# Section: AC
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
        This function takes in a query and returns a list of the most relevant
        document name.
        '''
        pass
