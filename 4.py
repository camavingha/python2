# ให้นักศึกษาเขียนโปรแกรมเพื่อรับอินพุท

# แล้วให้หาว่า คำไหนเกิดขึ้นเป็นจำนวนครั้งมากที่สุด

# และ คำไหนเกิดขึ้นเป็นจำนวนครั้งน้อยที่สุด

# แล้วแสดงผล ตามตัวอย่าง

# รับค่า 'a a b'

# 'a' เกิดบ่อยทีสุด คือ 2 ครั้ง

# 'b' มีน้อยที่สุด คือ 1 ครั้ง

# 2+1 = 3

# แสดงผลดังนี้

# ab = 3
print(" *** Show max/min key and their summation ***")
texts = input("Enter text : ").split()
dict_count = {}
for text in texts:
    if text in dict_count:
        dict_count[text] += 1
    else:
        dict_count[text] = 1
min_text = min(dict_count, key = dict_count.get)
max_text = max(dict_count, key = dict_count.get)
min_count = dict_count[min_text]
max_count = dict_count[max_text]
print(f"{max_text+min_text} sum = {min_count+max_count}")