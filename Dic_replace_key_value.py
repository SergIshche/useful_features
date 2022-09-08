# зміна місцями ключ/значення
dict_list={"a":1,"b":2,"c":3}
inverse_dict=dict([val,key] for key,val in dict_list.items())
print(inverse_dict)


