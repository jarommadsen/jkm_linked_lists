class LinkedList:
    def __init__(self, array):
        self.next = []
        self.previous = []
        self.value = []
        self.location = []
        i = 0
        for val in array:
            self.next.append(i + 1 if i + 1 < len(array) else None)
            self.previous.append(i - 1 if i > 0 else None)
            self.value.append(array[i])
            self.location.append(i)
            i += 1

    # this method inserts a new value in place of the indicated index,
    # moving the current index up one
    def insert(self, index, value):
        # alter previous value of the index that was already there
        # You find it by iterating from the row with None as it's previous value
        # and moving forward 'index' number of steps
        i_new = len(self.next)
        # add new value
        self.value.append(value)
        self.location.append(i_new)
        if i_new is 0:
            self.next.append(None)
            self.previous.append(None)
            return 0
        index = max(0, min(index, i_new))
        i_next = self.previous.index(None)
        i_prev = i_next
        i = index
        while i >= 0:
            # we skip the first iteration to have i_prev one place behind
            # 'index' and i_next on top of 'index'
            # We don't just set i = index - 1 because we still want to be able
            # to set index = 0 and not have it be -1
            if i is not index:
                i_prev = i_next
                try:
                    # find where we're going next by searching our 'previous' for the current i_prev index
                    i_next = self.previous.index(i_prev)
                except ValueError:
                    pass
            # if it's the last iteration, change previous value
            if i is 0:
                if index is 0:
                    self.previous.append(None)
                else:
                    # The previous value whose next value points to new value
                    self.previous.append(i_prev)
                    self.next[i_prev] = i_new
            i -= 1
        if index is i_new:
            self.next.append(None)
        else:
            # The next value whose previous value points to new value
            self.next.append(i_next)
            self.previous[i_next] = i_new

    def delete(self, index):
        size = len(self.next) - 1
        index = max(0, min(index, size))
        i_next = self.location[self.previous.index(None)]
        i_now = i_next
        i_prev = i_now
        # similar process to insert but we need the spot behind and in front
        # of our target index.
        i = index
        while i >= 0:
            # find where we're going next by searching our 'previous' for the current i_now index
            i_next = self.next[self.location.index(i_now)]
            if i_next is None:
                i_next = i_now
            # The last iteration we do our logic
            if i is 0:
                # Set previous index's 'next' to target's 'next'
                self.next[self.location.index(i_prev)] = self.next[self.location.index(i_now)]
                # Set next index's 'previous' to target's 'previous'
                self.previous[self.location.index(i_next)] = self.previous[self.location.index(i_now)]
                # Delete target
                del self.next[self.location.index(i_now)]
                del self.previous[self.location.index(i_now)]
                del self.value[self.location.index(i_now)]
                del self.location[self.location.index(i_now)]
            i_prev = i_now
            i_now = i_next
            i -= 1
    def f_print(self):
        to_return = ""
        to_return += "Locate\t"
        to_return += "Next\t"
        to_return += "Prev\t"
        to_return += "Value\t\n"
        i = 4
        while i:
            to_return += "-------\t"
            i -= 1
        to_return += "\n"
        i = self.previous.index(None)
        while True:
            to_return += str(self.location[i]) + "\t"
            to_return += str(self.next[i]) + "\t"
            to_return += str(self.previous[i]) + "\t"
            to_return += str(self.value[i]) + "\t\n"
            if self.next[i] is None:
                break
            i = self.location.index(self.next[i])
        print(to_return)

    def b_print(self):
        to_return = ""
        to_return += "Locate\t"
        to_return += "Next\t"
        to_return += "Prev\t"
        to_return += "Value\t\n"
        i = 4
        while i:
            to_return += "-------\t"
            i -= 1
        to_return += "\n"
        i = self.next.index(None)
        while True:
            to_return += str(self.location[i]) + "\t"
            to_return += str(self.next[i]) + "\t"
            to_return += str(self.previous[i]) + "\t"
            to_return += str(self.value[i]) + "\t\n"
            if self.previous[i] is None:
                break
            i = self.location.index(self.previous[i])
        print(to_return)

    def __str__(self):
        to_return = ""
        to_return += "Locate\t"
        to_return += "Next\t"
        to_return += "Prev\t"
        to_return += "Value\t\n"
        i = 4
        while i:
            to_return += "-------\t"
            i -= 1
        to_return += "\n"
        i = 0
        while i < len(self.location):
            to_return += str(self.location[i]) + "\t"
            to_return += str(self.next[i]) + "\t"
            to_return += str(self.previous[i]) + "\t"
            to_return += str(self.value[i]) + "\t\n"
            i += 1
        return to_return

array = ["Dog", "Cat", "Mouse", "Your mom", "TRex", "Will"]

l = LinkedList(array)

print(l)
l.delete(3)
print(l)
l.delete(3)
print(l)
l.delete(3)
print(l)
l.delete(3)
print(l)
l.delete(3)
print(l)
l.delete(3)
print(l)
l.insert(3, "Dude")
print("\n\n\n")
print(l)
l.insert(5, "Marley")
print("\n\n\n")
print(l)
l.insert(0, "Jarom")
print("\n\n\n")
print(l)
l.insert(100, "Pizza")
print("\n\n\n")
print(l)
l.insert(4, "Hamburgers")
print("\n\n\n")
print(l)
l.f_print()
l.b_print()
# print(l)
# l.delete(0)
# print(l)
# l.delete(0)
# print(l)
# l.delete(0)
# print(l)
# l.delete(3)
# print(l)
# l.delete(3)
# print(l)
