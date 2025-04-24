employee_index_1 ={
    122: 45,
    123: 89,
    567: 69,
    670: 69
}

print(employee_index_1)

employee_index_2 = {
    222: 67,
    566: 90
}

print(employee_index_2)

employee_index_1.update(employee_index_2)
print(employee_index_1)

employee_index_1.popitem()
print(employee_index_1)