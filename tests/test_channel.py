from main.Channel import Channel, Video, PLVideo

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

class TestVideo(unittest.TestCase):
    def test__str__(self):
        video1 = Video('9lO06Zxhu88')
        video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
        assert video1.__str__() == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
        assert video2.__str__() == 'Пушкин: наше все?'