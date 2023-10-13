numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum = 0
idx = 0
for el in numbers:
    if el == None:
        idx = numbers.index(el)
    else:
       sum+=el
numbers[idx] = round(sum/len(numbers),2)
print("Измененный список:", numbers)
