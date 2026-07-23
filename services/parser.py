from lxml import etree

BOOKS = {
    1: "ปฐมกาล",
    2: "อพยพ",
    3: "เลวีนิติ",
    4: "กันดารวิถี",
    5: "เฉลยธรรมบัญญัติ",
}


def load_bible(xml_path):
    tree = etree.parse(xml_path)
    root = tree.getroot()

    verses = []

    for record in root.findall("RECORD"):

        book = int(record.findtext("book_num"))
        chapter = int(record.findtext("chapter_num"))
        verse = int(record.findtext("verse_num"))
        text = record.findtext("detail_txtbox")

        verses.append({
            "book": BOOKS.get(book, str(book)),
            "chapter": chapter,
            "verse": verse,
            "text": text
        })

    return verses