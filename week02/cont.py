from typing import List

def area(left: int, right: int, h1: int, h2: int) -> int:
    return min(h1, h2) * (right - left)




def solution(array: List[int]) -> int:
    left: int = 0
    right: int = len(array) - 1
    max_area: int = 0

    while left <= right:
        current: int = area(left, right, array[left], array[right])
        if current > max_area:
            max_area = current
        
        if array[left] >= array[right]:
            right -= 1
        else:
            left += 1

    return max_area

def main() -> None:
    input: List[int] = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Input:", *input)
    print(f"Output: {solution(input)}")

if __name__ == "__main__":
    main()