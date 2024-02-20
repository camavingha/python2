print(" *** Find least frequent word ***")
texts = input("Enter text : ").split()
dict_count = {}
for text in texts:
    if text in dict_count:
        dict_count[text] += 1
    else:
        dict_count[text] = 1
least_text = min(dict_count, key = dict_count.get)
least_count = dict_count[least_text]
print(f"Least = {least_text} => {least_count}")

# ใช้ตัวแปร dictionary เพื่อหาคำที่เกิดขึ้นบ่อยน้อยที่สุด