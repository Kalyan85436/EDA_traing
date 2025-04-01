from truth_table import*
import pytest

# @pytest.mark.parametrize("a,b,expected",[
#     (False, False, False),
#     (False, True, False),
#     (True, False, False),
#     (True, True, True)
# ])
# def test_and(a,b,expected):
#    assert  and_gate(a,b) == expected
#
#
# @pytest.mark.parametrize("a,b,expected",[
#     (False, False, False),
#     (False, True, True),
#     (True, False, True),
#     (True, True, True)
# ])
# def test_or(a,b,expected):
#     assert or_gate(a,b) == expected
#
#
# def test_not():
#     assert not_gate(0) == 1
#     assert  not_gate(1) == 0


@pytest.mark.parametrize("a,b,expected1 expected2",[
    (False, False, False, False),
    (False, True, True, False),
    (True, False, True, False),
    (True, True, False, True)
])

def test_half_adder(a,b,expected1,expected2):
    assert half_adder(a,b) == (expected1,expected2)


# def test_half_adder():
#     assert half_adder(0, 0) == (0,0)
#     assert half_adder(0, 1) == (1,0)
#     assert half_adder(1, 0) == (1,0)
#     assert half_adder(1, 1) == (0,1)
