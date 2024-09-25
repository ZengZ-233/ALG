import math

def is_square(s):
    root = int(math.isqrt(s))
    return root * root == s

def is_equilateral_triangle(s):
    a2 = s * 4
    sqrt_a2 = int(math.isqrt(a2))
    if sqrt_a2 * sqrt_a2 != a2:
        return False
    
    return (sqrt_a2 * (sqrt_a2 + 1)) // 2 == s

T = int(input())
for _ in range(T):
    s = int(input())
    
    square_flag = is_square(s)
    triangle_flag = is_equilateral_triangle(s)
    
    if square_flag and triangle_flag:
        print(2)  
    elif square_flag:
        print(0)  
    elif triangle_flag:
        print(1)  
    else:
        print(3)  
