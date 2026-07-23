"""XML Bible Data Parser."""

from typing import Any, Dict, List
from lxml import etree

BOOKS: Dict[int, str] = {
    1: "ปฐมกาล",
    2: "อพยพ",
    3: "เลวีนิติ",
    4: "กันดารวิถี",
    5: "เฉลยธรรมบัญญัติ",
}


def load_bible(xml_path: str) -> List[Dict[str, Any]]:
    """Parse XML file containing Bible records into structured verse dictionaries.

    Args:
        xml_path: Path to the Bible XML data file.

    Returns:
        List of verse dictionaries containing book name, chapter, verse, and text.
    """
    tree = etree.parse(xml_path)
    root = tree.getroot()

    verses: List[Dict[str, Any]] = []

    for record in root.findall("RECORD"):
        book_num = int(record.findtext("book_num") or 0)
        chapter_num = int(record.findtext("chapter_num") or 0)
        verse_num = int(record.findtext("verse_num") or 0)
        detail_txt = record.findtext("detail_txtbox") or ""

        verses.append({
            "book": BOOKS.get(book_num, str(book_num)),
            "chapter": chapter_num,
            "verse": verse_num,
            "text": detail_txt,
        })

    return verses