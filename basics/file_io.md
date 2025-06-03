# File I/O in Python

This notebook will cover the following topics:

1. Opening and closing files
2. Reading and writing text files
3. Reading and writing binary files
4. Using the `with` statement
5. Using the `pickle` module
6. Serializing objects with `pickle`
7. Reading and writing JSON files

## Opening and closing files

Let's start with the basics. To open a file, we use the built-in `open()` function. The `open()` function takes two arguments: the name of the file to open and the mode in which to open it. The mode can be one of the following:

* `'r'` - open for reading (default)
* `'w'` - open for writing, truncating the file first
* `'x'` - open for exclusive creation, failing if the file already exists
* `'a'` - open for writing, appending to the end of the file if it exists
* `'b'` - binary mode
* `'t'` - text mode (default)
* `'+'` - open a disk file for updating (reading and writing)

To make this tutorial more interesting, let's create a purpose for our code. Our goal is to create a logging system for players and their rolls. Every time a player rolls, we will add it to our log. We will also add a timestamp to each roll. We will store the log in a file called `log.txt`.


```python
import random
import datetime

# First, we'll open a file
fp = open("log.txt", "w")

# Let's create a list of players
players = ["Naomi", "James", "Amos", "Bobbie"]

# Let's roll a d20 for each player and write it in the log, including a timestamp
for player in players:
    roll = random.randint(1, 20)
    timestamp = datetime.datetime.now()
    fp.write(f"{timestamp} - {player} rolled a {roll}\n")

# Finally, let's close the file
fp.close()
```

It isn't recommended to open and close the file manually like this. Instead, we will use the `with` statement. This will ensure that the file is closed properly even if an exception is raised.

Additionally, it is possible that calling `write` without using `with` will not write to the file immediately. Instead, it will be buffered and written later. Using `with` will ensure that the file is written to immediately.

```python
import datetime

with open('log.txt', 'a') as f:
    f.write(f'{datetime.datetime.now()}: {player} rolled {roll}\n')
```

## Reading and writing binary files

For the next example, we will write the user's rolls as binary. Each user will get their own file so that we can easily read their rolls later.


```python
for player in players:
    rolls = [random.randint(1, 20) for _ in range(5)]
    with open("rolls/" + player + ".bin", "wb") as fp:
        fp.write(bytes(rolls))

# To verify, let's open the files and print the contents
for player in players:
    with open("rolls/" + player + ".bin", "rb") as fp:
        print(player, list(fp.read()))
```

    Naomi [2, 13, 18, 8, 16]
    James [7, 10, 17, 15, 15]
    Amos [19, 9, 11, 6, 3]
    Bobbie [16, 5, 18, 13, 1]


# Reading from CSV files

Python has a built-in module for reading and writing CSV files. CSV stands for comma-separated values. It is a common format for storing tabular data.


```python
# Load and parse CSV
import csv

# Store the data in a list of dictionaries
data = []
with open("../data/musicnet_metadata.csv", "r") as fp:
    reader = csv.reader(fp)
    keys = next(reader)
    for row in reader:
        data.append(dict(zip(keys, row)))

# Let's print the first 5 rows
for row in data[:5]:
    print(row)

# Count the number of Violin pieces are in the dataset
count = 0
for row in data:
    if "Violin" in row["ensemble"]:
        count += 1

print(f"There are {count} Violin pieces in the dataset")
```

    {'id': '1727', 'composer': 'Schubert', 'composition': 'Piano Quintet in A major', 'movement': '2. Andante', 'ensemble': 'Piano Quintet', 'source': 'European Archive', 'transcriber': 'http://tirolmusic.blogspot.com/', 'catalog_name': 'OP114', 'seconds': '447'}
    {'id': '1728', 'composer': 'Schubert', 'composition': 'Piano Quintet in A major', 'movement': '3. Scherzo: Presto', 'ensemble': 'Piano Quintet', 'source': 'European Archive', 'transcriber': 'http://tirolmusic.blogspot.com/', 'catalog_name': 'OP114', 'seconds': '251'}
    {'id': '1729', 'composer': 'Schubert', 'composition': 'Piano Quintet in A major', 'movement': '4. Andantino - Allegretto', 'ensemble': 'Piano Quintet', 'source': 'European Archive', 'transcriber': 'http://tirolmusic.blogspot.com/', 'catalog_name': 'OP114', 'seconds': '444'}
    {'id': '1730', 'composer': 'Schubert', 'composition': 'Piano Quintet in A major', 'movement': '5. Allegro giusto', 'ensemble': 'Piano Quintet', 'source': 'European Archive', 'transcriber': 'http://tirolmusic.blogspot.com/', 'catalog_name': 'OP114', 'seconds': '368'}
    {'id': '1733', 'composer': 'Schubert', 'composition': 'Piano Sonata in A major', 'movement': '2. Andantino', 'ensemble': 'Solo Piano', 'source': 'Museopen', 'transcriber': 'Segundo G. Yogore', 'catalog_name': 'D959', 'seconds': '546'}
    There are 35 Violin pieces in the dataset


# Application: List all works in the dataset by Bach for Solo Violin

Now that we have our data loaded. Let's use list comprehensions to print out all the works by Bach for solo violin. Our formatted table should show the following columns:
- id
- composition name
- seconds


```python
# Filter all lines that are written by Bach
bach = [row for row in data if "Bach" in row["composer"] and "Solo Violin" in row["ensemble"]]

# Print the number of Bach pieces
print(f"There are {len(bach)} Bach pieces in the dataset")

# Print them all out
for row in bach:
    print(row)
```

    There are 9 Bach pieces in the dataset
    {'id': '2186', 'composer': 'Bach', 'composition': 'Violin Partita No 3 in E major', 'movement': '1. Preludio', 'ensemble': 'Solo Violin', 'source': 'Oliver Colbentston', 'transcriber': 'suzumidi', 'catalog_name': 'BWV1006', 'seconds': '214'}
    {'id': '2191', 'composer': 'Bach', 'composition': 'Violin Partita No 3 in E major', 'movement': '6. Bourree', 'ensemble': 'Solo Violin', 'source': 'Oliver Colbentston', 'transcriber': 'suzumidi', 'catalog_name': 'BWV1006', 'seconds': '102'}
    {'id': '2241', 'composer': 'Bach', 'composition': 'Violin Sonata No 1 in G minor', 'movement': '1. Adagio', 'ensemble': 'Solo Violin', 'source': 'European Archive', 'transcriber': 'suzumidi', 'catalog_name': 'BWV1001', 'seconds': '242'}
    {'id': '2242', 'composer': 'Bach', 'composition': 'Violin Sonata No 1 in G minor', 'movement': '2. Fuga', 'ensemble': 'Solo Violin', 'source': 'European Archive', 'transcriber': 'suzumidi', 'catalog_name': 'BWV1001', 'seconds': '312'}
    {'id': '2243', 'composer': 'Bach', 'composition': 'Violin Sonata No 1 in G minor', 'movement': '3. Siciliana', 'ensemble': 'Solo Violin', 'source': 'European Archive', 'transcriber': 'suzumidi', 'catalog_name': 'BWV1001', 'seconds': '193'}
    {'id': '2244', 'composer': 'Bach', 'composition': 'Violin Sonata No 1 in G minor', 'movement': '4. Presto', 'ensemble': 'Solo Violin', 'source': 'European Archive', 'transcriber': 'suzumidi', 'catalog_name': 'BWV1001', 'seconds': '214'}
    {'id': '2288', 'composer': 'Bach', 'composition': 'Violin Partita No 1 in B minor', 'movement': '2. Corrente', 'ensemble': 'Solo Violin', 'source': 'John Garner', 'transcriber': 'suzumidi', 'catalog_name': 'BWV1002', 'seconds': '191'}
    {'id': '2289', 'composer': 'Bach', 'composition': 'Violin Partita No 1 in B minor', 'movement': '3. Sarabande', 'ensemble': 'Solo Violin', 'source': 'John Garner', 'transcriber': 'suzumidi', 'catalog_name': 'BWV1002', 'seconds': '203'}
    {'id': '2659', 'composer': 'Bach', 'composition': 'Violin Partita No 1 in B minor', 'movement': '6. Double', 'ensemble': 'Solo Violin', 'source': 'John Garner', 'transcriber': 'suzumidi', 'catalog_name': 'BWV1002', 'seconds': '108'}


It looks like this dataset is missing quite a few pieces. Bach wrote 6 sonatas and partitas for solo violin. We only have 3 of them in this dataset. Of the 3 that are included, partitas 1 and 3 are incomplete as well.

Based on the order of the ids, it looks like this data should be present. Let's see if we can fill some of this in.


```python
# The times are based on Hilary Hahn's recordings

missing_pieces = [
    {
        "id": "2679",
        "composer": "Bach",
        "composition": "Violin Partita No 3 in E major",
        "movement": "2. Loure",
        "ensemble": "Solo Violin",
        "source": "DASC 5300 Fall 2023",
        "transcriber": "none",
        "catalog_name": "BWV 1006",
        "seconds": "287"
    },
    {
        "id": "2680",
        "composer": "Bach",
        "composition": "Violin Partita No 3 in E major",
        "movement": "3. Gavotte en Rondeau",
        "ensemble": "Solo Violin",
        "source": "DASC 5300 Fall 2023",
        "transcriber": "none",
        "catalog_name": "BWV 1006",
        "seconds": "196"
    },
    {
        "id": "2681",
        "composer": "Bach",
        "composition": "Violin Partita No 3 in E major",
        "movement": "4. Menuet I",
        "ensemble": "Solo Violin",
        "source": "DASC 5300 Fall 2023",
        "transcriber": "none",
        "catalog_name": "BWV 1006",
        "seconds": "113"
    },
    {
        "id": "2682",
        "composer": "Bach",
        "composition": "Violin Partita No 3 in E major",
        "movement": "5. Menuet II",
        "ensemble": "Solo Violin",
        "source": "DASC 5300 Fall 2023",
        "transcriber": "none",
        "catalog_name": "BWV 1006",
        "seconds": "183"
    },
]
```

# Formatting Our Output

Viewing raw lines of a dictionary or CSV file is less than ideal. Let's format our output to make it easier to read. We will format the filtered Bach data. Since we know that every piece was written by him, we don't need to show that column.


```python
# Let's add the missing pieces to our dataset
data.extend(missing_pieces)

# Refilter the Bach pieces
bach = [row for row in data if "Bach" in row["composer"] and "Solo Violin" in row["ensemble"]]
print(f"There are {len(bach)} Bach pieces in the dataset")

# Print them all out, sorted by composition then movement
composition_width = max(len(row["composition"]) for row in bach)
movement_width = max(len(row["movement"]) for row in bach)
id_width = max(len(row["id"]) for row in bach)

print("{:<{}} | {:<{}} | {:<{}}".format("Composition", composition_width, "Movement", movement_width, "ID", id_width))
print("-" * (composition_width + movement_width + id_width + 6))
for row in sorted(bach, key=lambda x: (x["composition"], x["movement"])):
    print("{:<{}} | {:<{}} | {:<{}}".format(row["composition"], composition_width, row["movement"], movement_width, row["id"], id_width))

```

    There are 13 Bach pieces in the dataset
    Composition                    | Movement              | ID  
    -------------------------------------------------------------
    Violin Partita No 1 in B minor | 2. Corrente           | 2288
    Violin Partita No 1 in B minor | 3. Sarabande          | 2289
    Violin Partita No 1 in B minor | 6. Double             | 2659
    Violin Partita No 3 in E major | 1. Preludio           | 2186
    Violin Partita No 3 in E major | 2. Loure              | 2679
    Violin Partita No 3 in E major | 3. Gavotte en Rondeau | 2680
    Violin Partita No 3 in E major | 4. Menuet I           | 2681
    Violin Partita No 3 in E major | 5. Menuet II          | 2682
    Violin Partita No 3 in E major | 6. Bourree            | 2191
    Violin Sonata No 1 in G minor  | 1. Adagio             | 2241
    Violin Sonata No 1 in G minor  | 2. Fuga               | 2242
    Violin Sonata No 1 in G minor  | 3. Siciliana          | 2243
    Violin Sonata No 1 in G minor  | 4. Presto             | 2244



```python
# Now that it looks good, let's write the updated dataset to a new file
with open("../data/musicnet_metadata_updated.csv", "w") as fp:
    writer = csv.DictWriter(fp, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)
```

# Reading and Writing JSON

JSON stands for JavaScript Object Notation. It is a common format for storing and transmitting data. It is often used for web APIs. Python has a built-in module for reading and writing JSON files.

Let's open the CSV file from the previous example and write it to JSON.


```python
# Load and parse CSV
import csv
import json

# Store the data in a list of dictionaries
data = []
with open("../data/musicnet_metadata.csv", "r") as fp:
    reader = csv.reader(fp)
    keys = next(reader)
    for row in reader:
        data.append(dict(zip(keys, row)))

# Write the data to a JSON file
with open("musicnet_metadata.json", "w") as fp:
    json.dump(data, fp)
```

# Reading and Writing `pickle` Files

Python has a built-in module for reading and writing `pickle` files. `pickle` is a binary format for serializing Python objects. It is not human-readable, but it is very useful for storing and transmitting data. Note that `pickle` is not secure. It is possible to create malicious `pickle` files that can execute arbitrary code when loaded. Also, other languages cannot natively read `pickle` files. However, there are usually libraries available for reading `pickle` files in other languages.

Let's start by writing the list from the previous example to a `pickle` file.


```python
# Write the data to a pickle file
import pickle

with open("musicnet_metadata.pkl", "wb") as fp:
    pickle.dump(data, fp)

# Get the file size of the pickle file we just wrote
import os

print(os.path.getsize("musicnet_metadata.pkl"))
```

    52353


# Serializing Class Objects

Serializing objects is simple with Python. Let's create a simple class to represent the attributes of our dataset. We can then convert our previous list of dictionary data to a list of objects. Finally, we can serialize the list of objects to a `pickle` file.


```python
# Create a class for our data
class Piece:
    def __init__(self, data):
        self.id = data["id"]
        self.composer = data["composer"]
        self.composition = data["composition"]
        self.movement = data["movement"]
        self.ensemble = data["ensemble"]
        self.source = data["source"]
        self.transcriber = data["transcriber"]
        self.catalog_name = data["catalog_name"]
        self.seconds = data["seconds"]

    def __repr__(self):
        return f"<Piece {self.id}: {self.composer} - {self.composition}>"
    
    def __str__(self):
        return f"{self.composer} - {self.composition}"

# Convert our data into a list of objects and write it to a pickle file
pieces = [Piece(d) for d in data]
with open("musicnet_metadata.pkl", "wb") as fp:
    pickle.dump(pieces, fp)

# Print the size of this new file
print(os.path.getsize("musicnet_metadata.pkl"))
```

    54352


# Bonus: Write the class objects to JSON

We can't write the class objects to JSON directly. We need to convert them to a dictionary first. We can do this by implementing the `__dict__` method. Without explicitly defining `__dict__`, it will return the default dictionary for the class. However, we can override it to return a custom dictionary. The default version will include all of the class attributes. We can use this to our advantage to convert the class to a dictionary.


```python
# Bonus: Save the class data as JSON
import json

# Write the list of class objects to a JSON file
with open("musicnet_metadata.json", "w") as fp:
    json.dump(pieces, fp, default=lambda o: o.__dict__)
```
