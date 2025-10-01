'''
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
'''
n = int(input("Enter: "))

row = [1]  # first row

for i in range(n):
    # print spaces for alignment
    print(" " * (n - i), end="")
    
    # print numbers in the row
    for num in row:
        print(num, end=" ")
    print()
    
    # build the next row
    new_row = [1]
    for j in range(len(row) - 1):
        new_row.append(row[j] + row[j + 1])
    new_row.append(1)
    row = new_row
