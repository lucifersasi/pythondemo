def solution(number):
    Nums = list(range(0, number))
    multiples = []
    sum = 0
    for num in Nums:
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum


print(solution(10))
