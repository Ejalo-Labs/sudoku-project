# string = "a quick brown fox jumps over the lazy dog"
# # def string_length(word):
# #     return 0 if word == "" else 1 + string_length(word[1:])
# # print(string_length(string))
# print(len(string))


# def factorial(n):
#     return n if n in [0,1] else n * factorial(n-1)
# print(factorial(6))



def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1)+fibonacci(n-2)
for i in range(15):
    print(fibonacci(i), " ", end = "")


# def permute(s, a, b, l):       #takes string(s), initial position(a), and final position(b) as parameters
#     if a == b:
#         print("".join(s[b-l+1:b+1]))  #prints every permutation reached by the function
#         return 
#     else:
#         for i in range(a, b+1):
#             s[a], s[i] = s[i], s[a]
#             permute(s, a+1, b, l)      # recursive function 
#             s[a], s[i] = s[i], s[a]         # backtracking
# string = list("abc")           #string to find permutation of
# a, b = 1, 3                      # a = starting position; b = ending position    INDEX STARTS FROM 0
# l = b - a + 1                 # total length of the string to permute
# print(f"{factorial(l)} permutations.")      
# permute(string, a, b, l)


