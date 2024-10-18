
            
def solution(numbers, target):
    answer = 0
    nums = [0]
    for number in numbers:
        tmp = []
        for num in nums:
            tmp.append(num + number)
            tmp.append(num - number)
        nums = tmp
    for num  in nums:
        if target == num:
            answer += 1
    return answer