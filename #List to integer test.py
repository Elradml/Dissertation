#List to integer test

list = ['10', '20', '30', '40', '50']

int_list = [int(x) for x in list]
print(int_list)

str_list = [str(x) for x in int_list]
print(str_list)