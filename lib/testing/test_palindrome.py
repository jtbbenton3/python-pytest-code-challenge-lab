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