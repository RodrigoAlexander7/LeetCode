# # 54. Spiral Matrix

# from typing import List

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
#         left = up = False
#         i = j = 0
#         r = len(matrix)
#         c = len(matrix[0])

#         while r > 0 and c > 0:
#             while j > 0 and j < c:
#                 res.append(matrix[i][j])
#                 if not left :
#                     j+=1
#                 else:
#                     j-=1
#             r-=1
#             j+=1
#             left = not left

#             while i > 0 and i < r:
#                 res.append(matrix[i][j])
#                 if not up:
#                     i+=1
#                 else:
#                     i-=1
#             c-=1
#             i+=1
#             up = not up
#         return res
        