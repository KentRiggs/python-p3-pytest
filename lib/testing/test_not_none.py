#!/usr/bin/env python3

from not_none_functions import return_not_none

def test_return_not_none():
    '''Tests that the function "return_not_none" returns a value that is None.'''
    assert return_not_none() is None
