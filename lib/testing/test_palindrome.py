import pytest
from lib.palindrome import longest_palindromic_substring

# Basic Cases
def test_basic_palindrome_babad():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_basic_palindrome_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_basic_palindrome_racecar():
    assert longest_palindromic_substring("racecar") == "racecar"

# Edge Cases
def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_no_palindrome():
    assert longest_palindromic_substring("abcdefgh") == "a"

def test_long_string():
    long_string = "a" + "b" * 998 + "a"
    assert longest_palindromic_substring(long_string) == "a" + "b" * 998 + "a"

# Boundary Cases
def test_two_chars():
    assert longest_palindromic_substring("aa") == "aa"

# Additional Edge Cases
def test_mixed_case():
    assert longest_palindromic_substring("RaCeCaR") == "aCeCa"

def test_max_length_no_palindrome():
    max_length_string = "".join(chr(i) for i in range(97, 97 + 1000))  # a to dxe...
    assert longest_palindromic_substring(max_length_string) == "a"

def test_repeated_chars():
    assert longest_palindromic_substring("aaa") in ["aaa", "aa"]