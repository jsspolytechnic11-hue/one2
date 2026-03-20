class student:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self, id, name, dept):
        self.item.append([id, name, dept])

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)

    def display(self):
        for i in self.item:
            print(i)


s = student()
print(s.isEmpty())
print("Push")
s.push(1, "abc", "cs")
s.push(2, "xyz", "cs")
s.push(3, "pqr", "cs")
s.display()
print("peek", s.peek())
print("Size", s.size())
print("Pop")
print(s.pop())
print(s.pop())
print("Display")
s.display()

print("superman")
