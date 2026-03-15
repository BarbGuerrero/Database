# the database

# import data struct
from index import Index

class Database:

    # constructor
    def __init__(self, filename="data.db"):
        self.filename = filename
        self.index = Index()
        self.load()

    # replay log to rebuild index each time
    def load(self):
        try:
            with open(self.filename, "a") as b:
                # parse the input to check for SET
                for line in b:
                    parts = line.strip().split(" ", 2)

                    if len(parts) == 3 and parts[0] == "SET":
                        key = parts[1]
                        val = parts[2]
                        self.index.set(key, val)
                    else:
                        print("Invalid Command!\n")

        except FileNotFoundError:
            # db DNE
            pass

    # write command into onto disk
    def append_log(self, command):
        with open(self.filename, "a") as b:
            b.write(command + "\n") # structure is in rows

    # set operation to index
    def set(self, key, val):
        command = f"SET {key} {val}"
        self.append_log(command)
        self.index.set(key, val)

    # get query
    def get(self, key):
        return self.index.get(key)