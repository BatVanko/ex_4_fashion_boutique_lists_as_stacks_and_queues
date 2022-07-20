clothes = [int(el) for el in input().split(" ")]
capacity_of_rack = int(input())
numbers_of_racks = 1
current_rack = 0
while clothes:
    if current_rack + clothes[-1] <= capacity_of_rack:
        current_rack += clothes.pop()

    else:
        numbers_of_racks += 1
        current_rack = 0
print(numbers_of_racks)



