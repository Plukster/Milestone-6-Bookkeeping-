from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    n = len(li)
    for i in range(n):
        for j in range(i + 1, n):
            if li[i] + li[j] == target:
                return (i, j)
    
def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    seen = set()
    for index, value in enumerate(li):
        complement = target - value
        if complement in seen:
            return (li.index(complement), index)
        seen.add(value)
    
print(find_sum(5, [1, 2, 3, 4, 5]))  # Output should be in {(0, 3), (1, 2)}
print(find_sum_fast(5, [1, 2, 3, 4, 5]))  # Output should be in {(0, 3), (1, 2)}