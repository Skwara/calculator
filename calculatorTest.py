import pytest

from calculator import calculate, convert_to_rpn


def test_returns_single_number():
    assert calculate('2') == 2


def test_adds_two_numbers():
    assert calculate('2+3') == 5


def test_calculate():
    assert calculate('3+4*2/4-2') == 3


def test_converts_to_rpn():
    assert convert_to_rpn('2+3') == ['2', '3', '+']


def test_converts_to_rpn_with_associative_operators():
    assert convert_to_rpn('3+4*2') == ['3', '4', '2', '*', '+']


def test_converts_to_rpn_with_all_operators():
    assert convert_to_rpn('3+4*2/4-2') == ['3', '4', '2', '*', '4', '/', '+', '2', '-']
