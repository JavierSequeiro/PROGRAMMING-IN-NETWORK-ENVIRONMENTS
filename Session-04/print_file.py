from pathlib import Path

# We enter the name of the file
FILENAME = "RNU6_269P.txt"

# Open and read the file

file_contents = Path(FILENAME).read_text()

# Now we print the contents stored in file_contents

print(file_contents)
