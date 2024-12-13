#!/bin/python
import json

def process_data(data):
    data = json.loads(data)
    data["number"] *= 2
    return json.dumps(data)

if __name__ == "__main__":
    try:
        with open("data.json", "r") as f:  # Используем относительный путь
            input_data = f.read()
        processed_data = process_data(input_data)
        with open("processed_data.json", "w") as f:  # Используем относительный путь
            f.write(processed_data)
        print(processed_data)
    except FileNotFoundError:
        print("Error: data.json not found")
