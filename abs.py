import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}  # Maps value to index in list
        self.values = []        # Stores values

    def insert(self, val):
        """
        Inserts a value if not present.
        Returns True if inserted, False if it was already present.
        """
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """
        Removes a value if present.
        Returns True if removed, False if it wasn't found.
        """
        if val not in self.val_to_index:
            return False

        # Move the last element to the place of the element to remove
        last_val = self.values[-1]
        index_to_replace = self.val_to_index[val]

        self.values[index_to_replace] = last_val
        self.val_to_index[last_val] = index_to_replace

        # Remove the last element
        self.values.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self):
        """
        Returns a random element.
        """
        return random.choice(self.values)
