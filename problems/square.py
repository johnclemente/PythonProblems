def square(n):
        for i in range(0,n):
            if i == 0 or i == n-1:
                print("x " *n)
            else:
                print("x" + " "*((n*2)-3) + "x")
square(3)


# 5>7
# 3>3
# 4>5
# 6>9
# 7>11