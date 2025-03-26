
# a)
output_file = open('words_updated.txt','w')
input_file = open('words.txt', 'r')
lst_words = input_file.readlines()
new_lst = []
for word in lst_words:
    new_lst.append((word.rstrip())+' ')

output_file.writelines(new_lst)
output_file.close()
#print(new_lst)

# b)
'''
(b) Create an integer num_words that will hold the number of words that you have
    in your words_updated.txt (or words.txt) file.  Now prompt the user to read
    an integer k (between 1 and 80) from the user.  Make sure to do input 
    validation so to be assured that the user abides the constraints on k.  

    Open a new file called result.txt with writing mode, and read the words 
    from your words_updated.txt file and write them in result.txt such that
    the number of characters on each line of result.txt is at most k (not
    counting the spaces between the words).  That is, if the next word 
    begin considered fits on the current line, add it to the current line
    (make sure to include a space between each pair of words on the line). 
    Otherwise, put this word on a new line (which will become the new
    current line).

    One you finish writing to your result.txt file, print the content of
    your file.  Make sure to close all files that you have opened.  
'''
num_words = len(lst_words)
input_file = open('words_updated.txt', 'r')
k = int(input())
while k <1 and k > 80:
    k = int(input())
output_file = open('result.txt', 'w')
lst_words_updated = input_file.readlines()
for word in lst_words_updated:
    word.rstrip()
    k -= len(word)
    if k >= 0:
        output_file.write(word + ' ')
    else:
        k 

