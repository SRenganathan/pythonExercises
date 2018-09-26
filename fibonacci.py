number_of_terms_in_series = int(input("Till how many numbers you want in the fibonacci?: "))

def generate_fibonacci(number_of_terms):
        
    if (number_of_terms == 1):
        fibonacci_series = [1]
    else:
        fibonacci_series = []
        for i in range(number_of_terms-2):
            if (i == 0):
                fibonacci_series = [1]
            fibonacci_series.append(fibonacci_series[i-1]+fibonacci_series[i])
        fibonacci_series.insert(0, 1)
        
    return(fibonacci_series)

print(generate_fibonacci(number_of_terms_in_series))
            