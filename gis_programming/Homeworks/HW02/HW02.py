# program to multiply all items in a list using traversal
def multiplyList(part1):

    # mulitplies items one by one
    result = 1
    for a in part1:
        result = result * a
    return result

# driver code
part1 = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096]
print(multiplyList(part1))
print("")

# program adds all items in a list
def sumList(part2):

    sum = 0
    for b in part2:
        sum += b
    return sum

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
print(sumList(part2))
print("")

# program lists only even numbers in a list
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
for num in part3:
    if num % 2 == 0:    # divides number to find remainder
        print(num, end = " ")   




