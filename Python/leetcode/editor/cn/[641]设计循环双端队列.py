# 设计实现双端队列。
# 你的实现需要支持以下操作：
#
# 
# MyCircularDeque(k)：构造函数,双端队列的大小为k。 
# insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。 
# insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。 
# deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。 
# deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。 
# getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。 
# getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。 
# isEmpty()：检查双端队列是否为空。 
# isFull()：检查双端队列是否满了。 
# 
#
# 示例： 
#
# MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
# circularDeque.insertLast(1);			        // 返回 true
# circularDeque.insertLast(2);			        // 返回 true
# circularDeque.insertFront(3);			        // 返回 true
# circularDeque.insertFront(4);			        // 已经满了，返回 false
# circularDeque.getRear();  				// 返回 2
# circularDeque.isFull();				        // 返回 true
# circularDeque.deleteLast();			        // 返回 true
# circularDeque.insertFront(4);			        // 返回 true
# circularDeque.getFront();				// 返回 4
#  
#
# 
#
# 提示： 
#
# 
# 所有值的范围为 [1, 1000] 
# 操作次数的范围为 [1, 1000] 
# 请不要使用内置的双端队列库。 
# 
# Related Topics 设计 队列


# leetcode submit region begin(Prohibit modification and deletion)
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._size = 0
        self._front, self._rear = 0, 0
        self._capacity = k
        self._data = [-1] * k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self._front] = value
        else:
            self._front = (self._front - 1) % self._capacity
            self._data[self._front] = value
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self._rear] = value
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._data[self._rear] = value
        self._size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._data[self._front] = -1
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._rear = self._front
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._data[self._rear] = -1
        self._rear = (self._rear - 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._front = self._rear
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self._data[self._front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self._data[self._rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._size == self._capacity

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
