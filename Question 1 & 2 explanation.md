# week-20-repository



2.	Document how to run the program you created in question 1 in a readme.md file in your repo. Be as clear as possible. Use proper markdown, and consider using screenshots. Be sure to briefly discuss why this kind of exercise might be helpful for NLP in your markdown. 

For question 1 ran the following in VS code:

import string
### Open the file in read mode
text = open("cats_txt.txt", encoding="utf8") 

### Create an empty dictionary
d = dict()

### Loop through each line of the file
for line in text:

    # Remove the leading spaces and newline character
    line = line.strip()
    
    # Convert the characters in line to 
    # lowercase to avoid case mismatch
    line = line.lower()
    
    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))
    # Split the line into words
    words = line.split(" ")
    
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
            
### Print the contents of dictionary

for key in list(d.keys()):
   print(key, ":", d[key])
   


From the commanand line I used the following command :
Python.cat.py

wherein I passed my filename after writing Python keyword.

With the above code I was able to provide cats_txt.txt file as input and could get  the frequency of all words 
and punctuation in that text file.



I have also attached the screenshot for the same. 


I think this exercise is useful because of the below mentioned reasons :

It is easy to run large pieces of code.
Editing your script is easier in script mode.


