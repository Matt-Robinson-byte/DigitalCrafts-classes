num_list = [0,1]
total = 0
big_total = 0
while big_total < 4000000:
    total = num_list[0] + num_list[1]
    if total % 2 == 0:
        big_total = big_total + total
        if big_total < 4000000:
            print(big_total)
    num_list.append(total)
    num_list.pop(0)
