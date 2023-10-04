# 217. Contains Duplicate (Easy)

class Solution(object):
    def containsDuplicate(self, nums):
        testset = set()

        for num in nums:
            if num in testset:
                return True
            testset.add(num)

        return False