# Name: Adam Klingler
# Section: AC
# Description: This file contains tests for the document and search_engine
#   files.

# imports here
from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine

# File name constants
FILE1 = 'test-dir/document1.txt'
DIRECTORY = 'test-dir'

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
    assert_equals(0.1, test.term_frequency('super'))

# main program here


def main():
    '''
    Runs the tests for the Document and SearchEngine classes.
    '''
    print('Testing Document class')
    test_document_terms_field()
    test_document_get_words()
    test_document_term_frequency()

    # print('Testing SearchEngine class')


if __name__ == '__main__':
    main()
