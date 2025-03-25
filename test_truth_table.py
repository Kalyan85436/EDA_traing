from truth_table import*
import pytest

def test_and():
    assert and_gate(0,0) == 0
    assert and_gate(0,1) == 0
    assert and_gate(1, 0) == 0
    assert and_gate(1, 1) == 1

def test_or():
    assert or_gate(0,0) == 0
    assert or_gate(0,1) == 1
    assert or_gate(1, 0) == 1
    assert or_gate(1, 1) == 1

def test_not():
    assert not_gate(0) == 1
    assert  not_gate(1) == 0