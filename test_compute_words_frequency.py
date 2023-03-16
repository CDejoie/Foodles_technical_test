import pytest

from main import compute_words_frequency


def test_when_sentences_then_return_right_tuple():
    assert compute_words_frequency(
        "baz bar foo foo zblah zblah zblah baz toto bar", 3
    ) == [("zblah", 3), ("bar", 2), ("baz", 2)]


def test_when_empty_sentences_then_return_empty_array():
    assert compute_words_frequency("", 10) == []


def test_when_null_limit_then_return_empty_array():
    assert compute_words_frequency("foo bar", 0) == []


def test_when_given_no_sentence_then_raise_an_error():
    with pytest.raises(ValueError):
        compute_words_frequency("foo bar", -2)
