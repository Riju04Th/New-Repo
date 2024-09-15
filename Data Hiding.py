# class Solution:
# 	__privateCounter = 0
# 	def sum(self):
# 		self.__privateCounter += 1
# 		print(self.__privateCounter)
# count = Solution()
# count.sum()
# count.sum()
# print(count.__privateCounter)

# can't use the private class function

# class Solution:
# 	__privateCounter = 0
# 	def sum(self):
# 		self.__privateCounter += 1
# 		print(self.__privateCounter)
# count = Solution()
# count.sum()
# count.sum()
# count.sum()
# count.sum()
# count.sum()
# print(count._Solution__privateCounter)

# use the private class function

# class A:
#     def __init__(self):
#         self._p_var = 10
#     def _p_m(self):
#         print("protected variable")
#     def pub_m(self):
#         self._p_m()

# obj = A()
# obj.pub_m()

class A:
    def __init__(self):
        self.__p_var = 10
    def __p_m(self):
        print("protected variable")
    def pub_m(self):
        self.__p_m()

obj = A()
obj.pub_m()