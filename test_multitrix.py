from multitrix import matrix_converter, valid, rows_columns, can_multiply, multiply
import pytest

def test_matrix_converter():
    # converts matrices with 1 single digit numbers 
    assert matrix_converter('[[1,2,3],[4,5,6]]') == [[1,2,3],[4,5,6]]

    # converts matrices with double digit numbers 
    assert matrix_converter('[[11,22,33],[44,55,66]]') == [[11,22,33],[44,55,66]]

    # converts matrices with double digit numbers 
    assert matrix_converter('[[111,222,333],[444,555,666]]') == [[111,222,333],[444,555,666]]

def test_valid():
    # returns false when the outputed nested list is not in a matrix format 
    assert valid([['1','2','3'],['4','5']]) == False 
    assert valid([['4','5'],['1','2','3']]) == False  

def test_rows_columns():

    assert rows_columns([[1,2,3],[4,5,6]]) == (2,3)
    assert rows_columns([[1,2,3],[4,5,6],[2,3,4]]) == (3,3)

def test_can_multiply():
    assert can_multiply([[1,2,3],[4,5,6],[2,3,4]],[[1,2,3],[4,5,6]]) == False
    assert can_multiply([[1,2,3],[4,5,6],[2,3,4]],[[1,2,3],[4,5,6],[2,3,4]]) == True

def test_multiply():
    assert multiply([[1,2],[3,4]],[[5,6],[7,8]]) == [[19,22],[43,50]]
    assert multiply([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]]) == [[58,64],[139,154]]
    assert multiply([[1,4],[2,5],[3,6]],[[7,8,9],[10,11,12]]) == [[47,52,57],[64,71,78],[81,90,99]]
    assert multiply([[2,0],[1,3]],[[4],[5]]) == [[8],[19]]
