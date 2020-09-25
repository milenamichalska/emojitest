import csv
import json

emojis_dump = []

with open('emojis.csv', encoding="utf8") as csvfile:
    emojireader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i, row in enumerate(emojireader):
        fixture_object = {
            "model": "emojiapp.emoji",
            "fields": {
                "emoji": row[0],
                "emojiName": row[1]
            }
        }
        emojis_dump.append(fixture_object)

with open("emoji_fixture.json", "w") as write_file:
    json.dump(emojis_dump, write_file)
