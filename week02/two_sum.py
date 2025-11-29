from typing import Dict, List

def solution(list: List[int], target: int) -> List[int]:
    hash_table: Dict[int, int] = {}

    for i in range(len(list)):
        if list[i] in hash_table:
            return [hash_table[list[i]], i]
        
        hash_table[target - list[i]] = i


def main() -> None:
    input: List[int] = [3, 3]
    target: int = 6
    
    print(f"Input: {target} |", *input)
    print("Output:", *solution(input, target))

if __name__=="__main__":
    main()