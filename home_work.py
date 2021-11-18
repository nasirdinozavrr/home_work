def algorithm(numbers, desired_sum):
    for n in numbers:
        for d in numbers[numbers.index(n)+1:]:
            if n+d==desired_sum:
                return(numbers.index(n),numbers.index(d))



print(algorithm([2, 7, 11, 15], 9))