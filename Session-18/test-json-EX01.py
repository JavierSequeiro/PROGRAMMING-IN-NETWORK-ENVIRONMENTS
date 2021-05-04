import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-EX01.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)
limit = len(person["Firstname"])
# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'
print(f"Total people in the database: {limit}")
# Print the information on the console, in colors
for i in range(0, limit):
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'][i], person['Lastname'][i])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'][i])

    # Get the phoneNumber list
    phoneNumbers = person['phoneNumber'][i]

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for n, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(n), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])