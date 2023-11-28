from pathlib import Path

def display_content(path):
    """Display the content of a file"""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        # print(f"\nSorry, the file {path} could not be found.")
        pass
    else:
        print(f"\n{path}:")
        print(contents)

files = ['cats.txt', 'dogs.txt']

for file in files:
    path = Path(file)
    display_content(path)