
class Queue:
    def __init__(self):
        self.head = []
        self.tail = []
    def enqueue(self, data):
        self.tail.append(data)
    def dequeue(self):
        if not self.head:
            while self.tail:
                self.head.append(self.tail.pop())
        return self.head.pop()
    def peek(self):
        if not self.head:
            while self.tail:
                self.head.append(self.tail.pop())
        return self.head[-1]

def main():
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    print(q.peek())
    print(q.dequeue())
    print(q.peek())
    print(q.dequeue()) 
if __name__ == '__main__':
    main()