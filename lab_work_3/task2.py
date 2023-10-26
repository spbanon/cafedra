# TODO Напишите функцию find_common_participants
def find_common_participants(l1,l2,sym):
    l1 = set(l1.split(sym))
    l2 = set(l2.split(sym))
    res = list(l1.intersection(l2))
    return sorted(res)




participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
#print(find_common_participants(participants_first_group,participants_second_group,'|'))