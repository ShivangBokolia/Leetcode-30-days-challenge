class MinStack(object):

    def __init__(self):
        self.items = []
        """
        initialize your data structure here.
        """

    def push(self, x):
        self.items.append(x)
        """
        :type x: int
        :rtype: None
        """

    def pop(self):
        self.items.pop()
        """
        :rtype: None
        """

    def top(self):
        """
        :rtype: int
        """
        return self.items[len(self.items) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.items)

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)