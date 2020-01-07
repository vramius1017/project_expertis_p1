from peapp.views import TestBr, result_pine,result_polish,result_split,CleanChain,result_word

def test_TestBr(n):
    assert TestBr(0) == 0
    
def test_TestBr(n):
    assert TestBr(3) == 1

def test_TestBr(n):
    assert TestBr(2) == 1

def test_result_pine():
    return result_pine()  

def test_result_polish():
    return result_polish()

def test_result_split():
    return result_split()

def test_CleanChain(x):
    x = "#{}#"
    assert    CleanChain(x) ==  "#{}#"

def test_CleanChain(x):
    x = "[5,3]" 
    assert CleanChain(x) == "5 3"


def test_Result_words():
    return result_word()