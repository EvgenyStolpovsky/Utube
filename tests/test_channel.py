from main.Channel import Channel

def test__init__():
    id1 = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    id2 = 'UC1eFXmJNkjITxPFWTy6RsWg'
    assert id1 == 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    assert id2 == 'UC1eFXmJNkjITxPFWTy6RsWg'

def test__str__():
    id1 = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    id2 = 'UC1eFXmJNkjITxPFWTy6RsWg'
    assert id1.__str__() == 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    assert id2.__str__() == 'UC1eFXmJNkjITxPFWTy6RsWg'

def test__lt__():
    id1 = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    id2 = 'UC1eFXmJNkjITxPFWTy6RsWg'
    assert ch1.__lt__(ch2) is False

def test__gt__():
    id1 = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    id2 = 'UC1eFXmJNkjITxPFWTy6RsWg'
    assert ch1.__lt__(ch2) is True

def test__add__():
    id1 = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    id2 = 'UC1eFXmJNkjITxPFWTy6RsWg'
    assert ch1.__add__(ch2) == 14_000_000