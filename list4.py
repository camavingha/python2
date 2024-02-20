
dict_old = {'Volkswagan': 1, 'Toyota': 2, 'Tesla': 2}
input_data = input("Enter : ").split()

print("dict_old =", dict_old)

for i in range(0, len(input_data), 2):
    new_key = input_data[i]
    new_value = int(input_data[i + 1])
    if new_key in dict_old:
        print("{} exists in dicts".format(new_key))
        dict_old[new_key] += new_value
    else:
        print("{} does not exist".format(new_key))
        dict_old[new_key] = new_value

print("dict_new =", dict_old)
