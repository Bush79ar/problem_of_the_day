list1 = [[ 1, 2, 3,],
          [ 4, 5, 6,],
          [ 9, 8, 9,]]
x = 0
y= 0
n = len(list1)
for i in range(0, n): 
    x = x + list1[i][i]
    y = y + list1[i][n - i - 1]
r = x - y
    
print("1+5+6:", x)
print("3+5+9:", y)
print("|x-y|:",abs(r))
