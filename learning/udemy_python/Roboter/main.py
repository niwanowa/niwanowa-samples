import csv

first_text = """\
こんにちは!私はRobokoです。あなたの名前は何ですか?
"""

second_text = """\
{}さん。どこのレストランが好きですか？
"""

recommend_text = """\
私のオススメのレストランは、{}です。
このレストランは好きですか？[Yes/No]
"""

last_text = """\
{}さん。ありがとうございました。
良い一日を！さようなら。
"""
user_name = input(first_text)

with open('roboter.csv', 'r+') as csv_file:
    reader = csv.DictReader(csv_file)
    fieldnames = ['NAME', 'COUNT']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    print(type(reader))
    for row in reader:
        answer = input(recommend_text.format(row['NAME']))
        if answer == 'Yes':
            writer.writerow({'NAME': row['NAME'], 'COUNT': str(int(row['COUNT']) + 1)})
            break
    else:
        recommended_restaurant = input(second_text.format(user_name)).capitalize()
        writer.writerow({'NAME': recommended_restaurant, 'COUNT': 1})
print(last_text.format(user_name))

