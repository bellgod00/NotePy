# iterator3.py
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0
    print(f"여기를 다 찍나요?...1")
    def __iter__(self):
        return self
    print(f"여기를 다 찍나요?...2")
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result
    print(f"여기를 다 찍나요?...3")

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

if __name__ == "__main__":
    i = MyIterator([1,2,3])
    for item in i:
        print(item)
    i = ReverseIterator([1,2,3])
    for item in i:
        print(item)        