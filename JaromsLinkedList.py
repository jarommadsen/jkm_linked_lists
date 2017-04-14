class LinkedList:
    def __init__(self, array):
        self.next = []
        self.previous = []
        self.value = []
        i = 0
        for val in array:
            self.next.append(i + 1 if i + 1 < len(array) else None)
            self.previous.append(i - 1 if i > 0 else None)
            self.value.append(array[i])
            i += 1

    # this method inserts a new value in place of the indicated index,
    # moving the current index up one
    def insert(self, index, value):
        # add new value
        self.value.append(value)
        # alter previous value of the index that was already there
        # You find it by iterating from the row with None as it's previous value
        # and moving forward 'index' number of steps
        i_new = len(self.next)
        index = max(0, min(index, i_new))
        i_next = self.previous.index(None)
        i_now = i_next
        i = index
        while i >= 0:
            if i is not index:
                i_now = i_next
                try:
                    # find where we're going next by searching our 'previous' for the current i_now index
                    i_next = self.previous.index(i_now)
                except ValueError:
                    pass
            if i is 0:
                if index is 0:
                    self.previous.append(None)
                else:
                    # The previous value whose next value points to new value
                    self.previous.append(i_now)
                    self.next[i_now] = i_new
            i -= 1
        if index is i_new:
            self.next.append(None)
        else:
            # The next value whose previous value points to new value
            self.next.append(i_next)
            self.previous[i_next] = i_new

        def delete(self, index):
            return None

        def __str__(self):
            to_return = ""
            to_return += "\nNext\n"
            to_return += str(self.next)
            to_return += "\nPrevious\n"
            to_return += str(self.previous)
            to_return += "\nValue\n"
            to_return += str(self.value)
            return str(to_return)

array = [0, 1, 2, 3, 4, 5]

l = LinkedList(array)

print(l)
l.insert(6, 6)
print("\n\n\n")
print(l)
l.insert(6, 7)
print("\n\n\n")
print(l)
l.insert(6, 8)
print("\n\n\n")
print(l)
l.insert(6, 9)
print("\n\n\n")
print(l)
l.insert(6, 10)
print("\n\n\n")
print(l)
