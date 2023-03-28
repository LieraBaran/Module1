import pytest
from file import count_words_and_sentences

@pytest.mark.parametrize("expected_result, filename", [(10, "test.txt"), (15, "test2.txt")])
def test_count_words_and_sentences(expected_result, filename):
    assert count_words_and_sentences(filename) == expected_result