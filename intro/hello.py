total = 0 
x = 1 
while x <= 10: 
    total = total + x
    x = x + 1    
print (total)


def sumnums(variable, n):
    y = variable
    total2 = 0
    while y <= n: 
        total2 = total2 + y
        y += 1 
    return total2
        
print (sumnums(4, 6))



def contains(a, b, c):
    while a <= b:
        if a == c:
            return True
        a += 1
    return False

print (contains(1, 10, 5))

#if weekday and not vacation:
#    return False

#  return True
  
# broken down into:
    
#return not weekday or vacation
        