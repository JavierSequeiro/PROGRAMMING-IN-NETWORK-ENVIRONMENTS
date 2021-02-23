from pathlib import Path

filename = "U5.txt"

file_contents = Path(filename).read_text()
free_genome = file_contents[file_contents.find("\n") + 1:]
print(f"Body of the {filename} file:\n" + free_genome)

