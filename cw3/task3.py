a = {'V': "S001", 'V': "S002", 'VI': "S001", 'VI': "S005",
     'VI': "S005", 'VII': "  S005 ", " V ": " S009 ", " VIII ": " S007 ", "IV": "S002"}
b = list()
for el in a:
    b.append(a[el])
print(set(b))


# Напишите программу для печати всех уникальных значений в словаре.

# V : "S001"
# V : "S002"
# VI : "S001"
# VI : "S005"
# VI: "S005"
# VII:"  S005 "
# " V ":" S009 "
# " VIII ":" S007 "
