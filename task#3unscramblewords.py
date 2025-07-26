# #['python','javascript','java','automation','pytest','guvi','selenium']
#
# import random
#
# # Original list of strings
# original_list = ['python','javascript','java','automation','pytest','guvi','selenium']
# print(original_list)
#
# # Empty list to store scrambled strings
# scrambled_list = []
#
# # Iterate over each string in the original list
# for string in original_list:
#     # Scramble the characters between the first and last characters
#     middle_chars = list(string[1:-1])
#     random.shuffle(middle_chars)
#     # Combine the first, scrambled middle, and last characters
#     scrambled_string = string[0] + ''.join(middle_chars) + string[-1]
#     # Append the scrambled string to the list of scrambled strings
#     scrambled_list.append(scrambled_string)
#
# # Print the scrambled list
# print("Scrambled strings in list are:", scrambled_list)

#num=[0,1,2,3,4,5,6]
# evens, odds =[], []
# for i in num:
#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         odds.append(i)
# print("Even number list:",evens)
# print("Odd number list:", odds)


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def count_and_print_primes(numbers):
#     prime_numbers = [num for num in numbers if is_prime(num)]
#     print(f"Prime numbers: {prime_numbers}")
#     print(f"Count of prime numbers: {len(prime_numbers)}")
#
# # Example usage
# numbers_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19]
# count_and_print_primes(numbers_list)

numbers_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19]

prime_numbers = []
for num in numbers_list:
    if num < 2:
        continue
    prime_num = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime_num  = False
            break
    if prime_num :
        prime_numbers.append(num)

print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", len(prime_numbers))