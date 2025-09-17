from typing import List
from collections import defaultdict

    # firs count the elements
    # then sort the keys by value and store it on an list or something

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dc = defaultdict(int)
        
        for n in nums:
            dc[n] += 1
            
        dc_sorted = dict(sorted(dc.items(), key= lambda i: i[1], reverse=True))        # sorted(each element, key = the value use to sort) -> we use i[i] cause is the second value of the pair on items

        sorted_list = list(dc_sorted.keys())
        for i in range(k):  # go all the array form the k element to chek if there are two or more elements with the same count 
            res.append(sorted_list[i])
        return res
    
        # k = 1 | k = 0
        

        '''
        mi_dict = {'a': 3, 'b': 1, 'c': 2}
        mi_dict.items() → [('a', 3), ('b', 1), ('c', 2)]
        '''
