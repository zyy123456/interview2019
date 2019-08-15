import random #import rand
class Solution:

    def __init__(self, nums: List[int]):
        self.v = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.v

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = self.v[:]
        for i in range(len(res)):
            t = random.randint(i, len(res)-1)
            res[i], res[t] = res[t], res[i]
        return res
