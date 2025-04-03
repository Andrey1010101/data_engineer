import json
import yaml
import pandas as pd

# Данные для записи
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Запись в JSON файл
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Чтение из JSON файла
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)
    print('JSON Data:', json_data)

# Запись в YAML файл
with open('data.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file)

# Чтение из YAML файла
with open('data.yaml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)
    print('YAML Data:', yaml_data)

# Запись в CSV файл с использованием pandas
df = pd.DataFrame([data])  # Оборачиваем в список, чтобы создать DataFrame
df.to_csv('data.csv', index=False)

# Чтение из CSV файла с использованием pandas
csv_data = pd.read_csv('data.csv')
print('CSV Data:')
print(csv_data)