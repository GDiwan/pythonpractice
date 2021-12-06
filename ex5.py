#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes..

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

lista_count = len(a)
listb_count = len(b)

a_is_bigger = lista_count > listb_count

common_element = []
if a_is_bigger:
    for i in a:
        for j in b:
            if i == j:
                common_element.append(i)
else:
    for i in b:
        for j in a:
            if i == j:
                common_element.append(i)

unique_common_elements = set(common_element)

print(unique_common_elements)

#### Python way

print("Concise python way..")
c = []
for i in b:
    if i in a:
        if i not in c:
            c.append(i)

print(c)







