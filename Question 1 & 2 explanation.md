# week-20-repository



2.	Document how to run the program you created in question 1 in a readme.md file in your repo. Be as clear as possible. Use proper markdown, and consider using screenshots. Be sure to briefly discuss why this kind of exercise might be helpful for NLP in your markdown. 

Basic functionality of he MapReduce algorithm :

It contains two important tasks, namely Map and Reduce.

    1)The Map task takes a set of data and converts it into another set of data, 
    where individual elements are broken down into tuples (key-value pairs).

    2) The Reduce task takes the output from the Map as an input and combines those data tuples 
    (key-value pairs) into a smaller set of tuples

Following  steps weere followed :


     1) Initially using vscode, "mapper.py" is created. In this file code is written to extract words and punctuations from the text file          named cat_txt.txt. Required nltk modules were imported.


       2) In reducer file, the code is written to reduce the intermediate values (values from the mapper). Values from the reducer are now      sorted.

       3)Also, all the mapper,reducer and text file are in the same folder.
       

From the command prompt, cat command is used to call the cat_txt.txt. file to the mapper and reducer .The command that were used was :

cat ./cats_txt.txt|./mapper.py
cat ./cats_txt.txt|./mapper.py|sort|./reducer.pycat ./cats_txt.txt|./mapper.py

With the above code I was able to provide cats_txt.txt file as input and could get the frequency of all words 
and punctuation in that text file.



I have also attached the images for the same. 


I think this exercise is useful because of the below mentioned reasons :

    1)Mapreduce is important as it  helps in running large pieces of code.It also uses parallel processing which help in dealing with big amount of data.
    
    2)Editing your script is easier in script mode.
    
    3)Also it helps in scheduling, monitering and rerunning the failed jobs.
    


