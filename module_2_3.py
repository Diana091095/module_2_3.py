my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
#Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не закончится список (выход за границу).

i = 0
while 0 < len(my_list):
    if int(my_list[i]) > 0:
        print(my_list[i])
        i += 1
        continue
    elif int(my_list[i]) == 0:

        i += 1
        continue

    else:
        break