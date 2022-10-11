class Stack_Limit:

    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):

        values = [str(i) for i in reversed(self.list)]
        return '\n'.join(values)

    def isFull(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.list == None:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return 'List is full'
        else:
            self.list.append(value)

        return 'element is inserted'

    def pop(self):
        if self.isEmpty():
            return 'list is Empty'
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'list is empty'

        else:
            return self.list[-1]

    def delete(self):
        self.list = None
        return 'The stack is destroyed'


if __name__ == '__main__':
    custom_stack = Stack_Limit(5)
    custom_stack.push(2)
    custom_stack.push(4)
    custom_stack.push(6)
    custom_stack.push(8)
    custom_stack.push(10)
    custom_stack.push(12)
    print(custom_stack)
    print("*******************")
    custom_stack.pop()
    print(custom_stack)