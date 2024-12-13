#!/bin/python
import random
import json

def generate_data():
    data = {"number": random.randint(1, 100)}
    return json.dumps(data)

if __name__ == "__main__":
    data = generate_data()
    with open("data.json", "w") as f:  # Записываем данные в файл data.json
        f.write(data)
    print(data)
