my_list = [1,2,3,4,5,6]
even_list = []
for list_element in my_list :
    if list_element % 2 ==0:
        print(list_element)
        even_list.append(list_element)
print(even_list)
