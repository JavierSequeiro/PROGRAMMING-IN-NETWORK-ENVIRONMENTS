from pathlib import Path

filename = "ADA.txt"

file_content = Path(filename).read_text()
useful_genome = file_content[file_content.find("\n"):].replace("\n", "")
print(f"There are {len(useful_genome)} bases in {filename}")
