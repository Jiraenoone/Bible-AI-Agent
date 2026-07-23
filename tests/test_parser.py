from services.parser import load_bible

verses = load_bible("data/tsv_verses.xml")

print("จำนวนข้อทั้งหมด :", len(verses))

print("\nข้อแรก")

print(verses[0])

print("\nข้อที่ 100")

print(verses[100])