print(" *** Creating Dictionary ***")
input1 = input("Enter text : ").split()
dict_text = {}
for i in range(0, len(input1), 2):
    key = input1[i]
    value = input1[i+1]
    dict_text[key] = value
print(dict_text)