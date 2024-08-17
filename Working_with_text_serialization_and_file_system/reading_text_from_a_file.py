#3
from collections import Counter

# Открываем файл для чтения
with open('text.txt', 'r') as file:
    for line in file:
        # Разбиваем строку на слова
        words = line.lower().split()
        # Считаем частоту каждого слова
        word_counts = Counter(words)
        # Находим самое часто встречаемое слово
        most_common_word, frequency = word_counts.most_common(1)[0]
        # Выводим результат
        print(f"Самое часто встречаемое слово: {most_common_word}, Количество повторений: {frequency}")
        
#8.1
import json

file_path = 'employees.json'

# Открываем файл для чтения
with open(file_path, 'r') as file:
    data = json.load(file)

# Теперь переменная 'data' содержит данные из файла в формате Python
# Я могу обращаться к ним, как к обычному словарю или списку
print(data)

#8.3

import pandas as pd

# Загрузка данных из JSON-файла 
json_file_path = 'employees.json'
df = pd.read_json(json_file_path)

# Сохранение данных в CSV-файл 
csv_file_path = 'exel.csv'
df.to_csv(csv_file_path, index=False)

print(f"Данные успешно сохранены в {csv_file_path}")