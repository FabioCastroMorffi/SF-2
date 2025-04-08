from urllib.request import urlopen

def readFileURLString(url):
    data = urlopen(url)
    html_data = data.read()
    encoding = data.headers.get_content_charset('utf-8')
    decoded_html = html_data.decode(encoding)
    return decoded_html

data_str = readFileURLString('')
print(data_str)

'''
--> The function reads the file from a url into a string
    and returns that string
--> pick 5 books(give the url with 'plain text utf8')
--> read 4 of 5 books by using their url and the
    provided function. Automate this process as much
    as possible
--> write each of the books into a separate file(only
    the story, exclude the front matter and end matter)
    Make sure to open the file for writing with: encoding = 'UTF8'
--> the 5th book title keep in mind, but don't read or write it to
    the file

using try-except do the following for all 5 stories
--> read number of words of the story only
--> find the frequence of each word in the file 
--> number of paragraphs(exclude garbage)
--> number of sentences
--> most common vowel in the text
'''

