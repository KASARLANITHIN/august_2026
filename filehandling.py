#mode=r
# file=open("demo.txt",mode="r")
# read_date=file.readlines()
# print(read_date)
# file.close()

#read

#mode = a 
# file =open("demo.txt",mode="a")
# write_data=file.write("\nThis is append operation by using mode a")
# file.close()

# file=open("demo1.txt",mode="a")
# write_data=file.write("\nThis is append operation by using mode a")
# file.close()

#mode="w"
# voter=["pytionlife\n","Nithin\n","varun"]
# file = open("demo2.txt",mode="w")
# write_data=file.writelines(voter)
# file.close()

#TASK r+

#mode="r+"

# file=open("demo1.txt",mode="r+")
# # write_data=file.write("\nHello varun..")
# read_data=file.read()
# print(read_data)
# file.close() 

# #TASK a+
# #mode="a+"
# voters=["\n","nithin\n","ravi teja"]

# file=open("demo3.txt",mode="a+")
# write_data=file.write("\nHello Brothers..")
# print(file.tell())
# file.seek(0)
# read_data=file.read()
# print(read_data)
# file.close()

#mode="w+"
# file=open("demo4.txt",mode="w+")
# write_date=file.write("Welome to python")
# print(file.tell())
# file.seek(0)
# read_data=file.read()
# print(read_data)
# file.close()

# import os 
# fn="demo2.txt"
# nn="sample1.txt"
# os.rename(fn,nn)
         
# import os 
# os.remove("demo1.txt")
# os.remove("demo3.txt")
# os.remove("demo4.txt")
# os.remove("sample1.txt")

file=open("C:\\nithinfiles\\nithin\\OneDrive\\Desktop\\pythonlife.txt",mode="r")


read_data=file.read()
print(read_data)
file.close()