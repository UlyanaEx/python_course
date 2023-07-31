# Задача 1
# Дан список чисел. Определить сколько в нем различныхт чисел

list = [1, 1, 2, 0, -1, 3, 4, 4]
# решение 1
# total_count = 0
# flag = True
# for i in range(len(list)-1):
#     for j in range(i+1, len(list)):
#         if list[i] == list [j]:
#             flag = False
#     if flag:
#         total_count +=1
#     flag = True
# if list[-2] == list[-1]:
#     total_count +=1
# print (total_count)

# решение 2
# превратим список в множество
list1 = set(list)
print(len(list1))