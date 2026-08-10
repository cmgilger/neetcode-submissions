from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        common_tuples = Counter(nums).most_common(k)
        indices = []
        for i in common_tuples:
            indices.append(i[0])
        return indices
