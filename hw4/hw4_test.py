# Name: Adam Klingler
# Section: AB
# Description: This file contains tests for the document and search_engine
#   files.

# imports here
from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine

import math

# File name constants
DIRECTORY = 'test-dir'
FILE1 = DIRECTORY + '/document1.txt'
FILE2 = DIRECTORY + '/document2.txt'
FILE3 = DIRECTORY + '/document3.txt'

# tests here


def test_document_terms_field():
    '''
    Tests the construction of the terms field of a document.
    '''
    test = Document(FILE1)

    expected = {'i': 0.1, 'like': 0.1, 'apple': 0.2, 'pie': 0.2,
                'is': 0.1, 'super': 0.1, 'duper': 0.1, 'cool': 0.1}
    assert_equals(expected, test._terms)


def test_document_get_words():
    '''
    Tests the get_words function.
    '''

    test = Document(FILE1)

    expected = ['i', 'like', 'apple', 'pie', 'is', 'super', 'duper', 'cool']
    assert_equals(expected, test.get_words())


def test_document_term_frequency():
    '''
    Tests the term_frequency function.
    '''
    test = Document(FILE1)

    assert_equals(0, test.term_frequency('spinach'))
    assert_equals(0.2, test.term_frequency('appLe'))
    assert_equals(0.1, test.term_frequency('super!'))


def test_searchengine_fields():
    '''
    Tests the fields of a search engine after construction.
    '''
    test = SearchEngine(DIRECTORY)
    doc1 = Document(FILE1)
    doc2 = Document(FILE2)
    doc3 = Document(FILE3)

    assert_equals(3, test._total_documents)

    expected = {'i': [doc1, doc2, doc3], 'like': [doc1, doc2],
                'apple': [doc1], 'pie': [doc1, doc2], 'is': [doc1, doc3],
                'super': [doc1], 'duper': [doc1], 'cool': [doc1, doc3],
                'also': [doc2], 'chocolate': [doc2, doc3], 'cake': [doc3],
                'guess': [doc3]}

    assert_equals(expected, test._all_terms)


def test_searchengine_calculate_idf():
    '''
    Tests the term_frequency function.
    '''
    test = SearchEngine(DIRECTORY)

    assert_equals(0, test._calculate_idf('croissant'))
    assert_equals(0, test._calculate_idf('i'))
    assert_equals(math.log(1.5), test._calculate_idf('chocolate'))
    assert_equals(math.log(3), test._calculate_idf('apple'))


def test_searchengine_search():
    '''
    Tests the search function.
    '''
    test = SearchEngine(DIRECTORY)

    expected = [FILE1]
    assert_equals(expected, test.search('super'))
    assert_equals(None, test.search('croissant'))
    expected = [FILE1, FILE2]
    assert_equals(expected, test.search('Apple pie'))
# main program here


def main():
    '''
    Runs the tests for the Document and SearchEngine classes.
    '''
    print('Testing Document class')
    test_document_terms_field()
    test_document_get_words()
    test_document_term_frequency()

    print('Testing SearchEngine class')
    test_searchengine_fields()
    test_searchengine_calculate_idf()
    test_searchengine_search()


if __name__ == '__main__':
    main()
