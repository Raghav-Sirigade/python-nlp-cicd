from nlplogic.corenlp import search_wikipedia, summarize_wikipedia, get_text_blob, get_phrase

def test_get_phrase():
    assert 'leopardus' in get_phrase('ocelot')