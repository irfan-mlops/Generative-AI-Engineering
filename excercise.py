'''
1 . Evaluate the follow ing expressions:

(x < y) or (not(z == y) and (z < x))
1 . x = 0, y = 6 , z = 1 0
2 . x = 1 , y = 1 , z = 1

'''

# Solution

x, y,  z = 0, 6, 10
# x, y,  z = 1, 1, 1

exp = (x < y) or (not(z == y) and (z < x))

print(exp)

