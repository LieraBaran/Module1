import pytest
import os
from file import count_words,count_sentences


@pytest.fixture
def text_file():
    content = "Hello, world! This is a test.\nThis is only a test.\n"
    filename = "test.txt"
    with open(filename, "w") as f:
        f.write(content)
    yield filename
    os.remove(filename)

def test_count_words(text_file):
    assert count_words(text_file) == 11

@pytest.mark.parametrize("expected_count", [3, 3])
def test_count_sentences(text_file, expected_count):
    assert count_sentences(text_file) == expected_count
