# Name: Adam Klingler
# Section: AB
# Description: This file contains the Document class, which represents all the
#   words and word frequency in a document.

# imports here
import re


class Document:
    '''
    This object represents a wikipedia document. It keeps track of the words in
    a document and their frequency.
    '''

    def __init__(self, file_name):
        '''
        Constructs a new document object, which creates a dictionary with
        keys being terms in the document and values being the term frequency.
        '''
        self._terms = dict()
        self._file_name = file_name

        with open(file_name) as file_name:
            lines = file_name.readlines()
            # lines is a list of long space filled strings
            for line in lines:
                tokens = line.split()
                # tokens is a list
                for token in tokens:
                    # token needs to be stripped of punctuation
                    word = re.sub(r'\W+', '', token)
                    word = word.lower()

                    if word in self.get_words():
                        self._terms[word] += 1
                    else:
                        # Add word to terms dictionary
                        self._terms[word] = 1

        # Convert counts to frequency
        total_words = sum(self._terms.values())

        for term in self._terms.keys():
            self._terms[term] = self._terms[term] / total_words

    def term_frequency(self, term):
        '''
        This function takes in a term and returns the frequency in this
        document. If the term is not in this document, returns 0.
        '''
        term = re.sub(r'\W+', '', term)
        term = term.lower()

        if term in self.get_words():
            return self._terms[term]
        else:
            return 0

    def get_words(self):
        '''
        Returns a list of words in the document.
        '''
        return self._terms.keys()

    def get_file_name(self):
        '''
        Returns a string of the file name of the document being represented.
        '''
        return self._file_name

    def __eq__(self, other):
        '''
        Defines an ability to compare documents for equality
        '''
        is_same_name = self._file_name == other._file_name
        is_same_terms = self._terms == other._terms

        return is_same_name and is_same_terms
