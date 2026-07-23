import os
from services.parser import load_bible

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "tsv_verses.xml")


def test_load_bible_verses():
    """Verify that Bible XML parser correctly loads verses."""
    verses = load_bible(DATA_FILE)
    
    assert isinstance(verses, list)
    assert len(verses) > 0

    first_verse = verses[0]
    assert "book" in first_verse
    assert "chapter" in first_verse
    assert "verse" in first_verse
    assert "text" in first_verse
    assert first_verse["chapter"] == 1
    assert first_verse["verse"] == 1