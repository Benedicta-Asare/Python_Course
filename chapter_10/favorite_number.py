from pathlib import Path
import json

path = Path('number.json')
if path.exists():
    entry = path.read_text()
    number = json.loads(entry)
    print(f"I know your favorite number! It's {number}.")

else:
    number = input("Enter your favorite number: ")
    entry = json.dumps(number)
    path.write_text(entry)