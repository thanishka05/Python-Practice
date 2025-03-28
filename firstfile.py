marks=input("enter the max marks out of 100 \n").split(",")
# print(marks)
for n in range(len(marks)):
    marks[n] = int(marks[n])
# print(marks)
max_num = marks[0]
for num in marks:
    # marks[n] = int(marks[n])
    if num > max_num:
        max_num = num
print(max_num)