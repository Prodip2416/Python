#Open file.............
# Open others file file_to_work = open("test")

#File Open...............................
# my_Files = open("test.txt")

#File Read.................................
# my_Files = open("test.txt","r")

# content = my_Files.read()
# print(content)
# lines = my_Files.readline()
# print(lines)
# my_Files.close()
#

# Write in a file...............................
# files = open("test.txt","r")
# print(files.read())
# files.close()

# files = open("test.txt","w")
# files.write("How r u?")
# files.close()
#
# files = open("test.txt","r")
# print(files.read())
# files.close()

# file_to_work = open("test.txt", "w")
# is_writing_done = file_to_work.write("I am writing!!!")
#
# if is_writing_done:
#     print("Yes, {0} byte(s) has been written!".format(is_writing_done))
# file_to_work.close()

try:
    files = open(" dfgregtest.txt","r")
    print(files.read())
except FileNotFoundError:
    print("File Not Found!")
finally:
    files.close()