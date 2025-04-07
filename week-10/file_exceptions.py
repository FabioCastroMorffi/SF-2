# file_name = 'book.txt'
# try:
#     input_file = open(file_name, 'r')
# except FileNotFoundError:
#     print('file does not exist')
#     output_file = open(file_name, 'w', encoding='UTF-8')
# else:
#     for line in input_file:
#         print(line.rstrip())

# input_file = open('words.txt', 'r', encoding='UTF-8')
# words_lst = input_file.readlines()
# output_file.writelines(words_lst)

# input_file.close()
# output_file.close()


'''
a) print the story (only) to the user
'''
input_file = open('book.txt','r')
# empty_lines = 0
# flag = False
# for line in input_file:
#     if flag:
#         print(line)
#     if line == '\n':
#         count += 1
#         if count == 3:
#             flag = True
#     else:
#         count = 0

    

'''
b) count the number of words in the story
'''

lst_of_lines = input_file.readlines()
for line in lst_of_lines:
    item = line.rstrip().split()
    print(item)


