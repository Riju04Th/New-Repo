# class Solution:
# 	__privateCounter = 0
# 	def sum(self):
# 		self.__privateCounter += 1
# 		print(self.__privateCounter)
# count = Solution()
# count.sum()
# count.sum()
# print(count.__privateCount)

# can't use the private class function

class Solution:
	__privateCounter = 0
	def sum(self):
		self.__privateCounter += 1
		print(self.__privateCounter)
count = Solution()
count.sum()
count.sum()
count.sum()
count.sum()
print(count._Solution__privateCounter)

# use the private class function