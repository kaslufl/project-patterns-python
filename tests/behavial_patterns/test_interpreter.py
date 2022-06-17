from project_patterns import Parser


def test_valid_sentence():
    sentence = '10 + 5 - 4'
    parsed_sentence = Parser.parse(sentence)

    assert parsed_sentence.interpret() == 11


def test_invalid_sentence():
    try:
        sentence = '10 / 5'
        parsed_sentence = Parser.parse(sentence)
        parsed_sentence.interpret()
        assert False

    except ValueError:
        assert True
