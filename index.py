# in-memory index

class Index:
    def __init__(self):
        # our list of pairs
        self.entries = []

    def set(self, key, val):

        for i in range(len(self.entries)):
            # check if key exists
            if self.entries[i][0] == key:
                self.entries[i] = (key, val)
                return
            
            # dne? append instead
            self.entries.append((key, val))

    def get(self, key):
        for x, y in self.entries:
            if x == key:
                return y
        return None #if not found
    