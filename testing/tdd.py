def count_upper_case(message):
    upper = sum([2 for c in message if c.isupper()])   
    lower = sum([1 for c in message if c.islower()])  
    result = upper + lower 
    return result

return sum([2 for c in message if c.isupper()]) + sum([1 for c in message if c.islower()] + sum([5 for ])) 

print(count_upper_case("Conor Clarke"))

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 2, "One upper case"
assert count_upper_case("a") == 1, "One lower case"
assert count_upper_case("$%^&") == 0, "Only special characters"
assert count_upper_case("123") == 0, "Only numbers"

print("All tests pass")