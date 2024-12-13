#!/bin/python
import json

def display_data(data):
    data = json.loads(data)
    print(f"Processed number: {data['number']}")

if __name__ == "__main__":
    try:
        with open("processed_data.json", "r") as f:  # Используем относительный путь
            input_data = f.read()
        display_data(input_data)
    except FileNotFoundError:
        print("Error: processed_data.json not found")
