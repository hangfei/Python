'''******************************************
Created on 2013-1-25
author: Hangfei Lin
author: Josef Andrews
******************************************'''

import random
import string
OUT_FILE = "kwic_index.txt"

def main():
    dictionary = {}
    user_input_list = []

    user_input = raw_input("Please enter the name of a text file: ")
    if(user_input != ""):
        user_input_list.append(user_input)
    while(user_input != ""):
        user_input = raw_input("Please enter another text file name: ")
        if(user_input != ""):
            user_input_list.append(user_input)

     #clear the file on each run of main
    write_line(OUT_FILE, "", "w")
    
    for element in user_input_list:
        write_line(OUT_FILE, "\n" + element + "\n", "a")
        dictionary = process_file(element)
        write_to_file(dictionary, element, OUT_FILE)
        
    #string_test = pre_process("'@@$$++It 2 was'' the 'best of' times it was the worst of times")
    #print chomp('ddd\n')
    #process_file_dct = process_file("test_kwic.txt")
    #user_input = "test_kwic.txt"
    #user_input_list = "test_kwic.txt test_kwic2.txt"

def chomp(s):
    """To delete the \n in the end of string"""
    if s.endswith('\n'):
        return s[:-1]
    else:
        return s

def pre_process(line):
    """takes a line from a file, lowercases
       and removes all digits and punctuation and keywords"""
    stop_copy = line
    
    #Step 1: lowercase
    stop_copy = stop_copy.lower()

    #Step 2: del digits
    for element in line:
        if element.isdigit():
            stop_copy = stop_copy.replace(element,'')
            
    #Step 3: del puncuation. including "@#$%" and so on.
    for puncn in string.punctuation:
        if puncn != "'":
            stop_copy = stop_copy.replace(puncn, '')
    
    #???the split would return or change?
    #!!!split judge by spaces and so apostrophe(')would belong to the nearest word
    #!!!the split would del the spaces.
    #!!!so I assigned a new list

    #Step 4: open the file and read
    stop_copy_list = stop_copy.split()
    #!!!the .remove would change the element of list, so we need a new list to modify
    stop_result_list = stop_copy.split()
    stop_file = open("stop_words.txt")
    stop_line = stop_file.readline()
    
    #Step 5: check if there are any stop words and delete
    for element in stop_copy_list:
        stop_file = open("stop_words.txt")
        #bug1: we mistaking use stop_file instead of stop_line
        stop_line = stop_file.readline()
        while stop_line != '':
            #there are blank spaces in the file, so replace the blanks first
            stop_line = stop_line.replace(' ','')
            #print element, "and", chomp(stop_line)
            #the readed line contains a '\n'
            if(element == chomp(stop_line)):
                stop_result_list.remove(element)
            stop_line = stop_file.readline()
        #!!!we need to search the file again for each element
        stop_file.close()
        
    #using join would result in no spaces
    #processed_line = ''.join(stop_result_list)
    #convert the result list to a str(processed_line)
    processed_line = ""
    for word in stop_result_list:
        processed_line += word + ' '
    #???we can return list?
    return stop_result_list

def count_words(words, processed_dct, line_number):
    """to count the numbers of lines of each word"""
    #update dictionary for each word
    #with line number
    
    for word in words:
        lst = processed_dct.get(word,[])
        if (lst.count(line_number) == 0):
            lst.append(line_number)
        processed_dct[word] = lst
        #print "count test", word, words, lst, line_number, processed_dct
    
def process_file(input_file):
    """Process a file, give the key word and the line number,
       store in a dict"""
    input_file = open(input_file)
    read_line = input_file.readline()
    process_dct = {}
    line_number = 1
    while read_line:
        #if the line in the file is weird, the pre_process() funcn would be wrong
        #say numbers
        pre_processed_line = pre_process(read_line)
               
        count_words(pre_processed_line, process_dct, line_number)
        #print "line_number", line_number, read_line
        line_number += 1
        read_line = input_file.readline()
    input_file.close()
        #print "read_line",line_number,read_line
    return process_dct

##def process_files(user_input_str):
##    """process files using process_file function
##    input a str separated by spaces
##    return a tuple of a list and a list of dictionaries
##    """
##    #!!!Notice: it seems we don't need the process_files.
##    #it makes the project more complicated. But I still write one
##    #in case u need it.
##    
##    #Step 1: convert input str to list
##    user_input_list = user_input_str.split()
##    processed_files_list = []
##    #Step 2: process each file using process_files
##    for input_file in user_input_list:
##        processed_file_result = process_file(input_file)
##        processed_files_list.append(processed_file_result)
##    #Step 3: return (the input files list, the processed list of dcts)
##    return (user_input_list, processed_files_list)


#~~~~~~~~~~~~~~~~write~~~~~~~~~~~
#i write a basic structure of the write part based on my previous reading code
#so that the read part and the write would cooperate better

def file_to_list(file_name):
    """takes a file and returns a list of the file line by line"""
    in_file = open(file_name)
    lst = in_file.read()
    in_file.close()
    return lst.split("\n")

def write_to_file(dct, in_file, out_file):
    """print the formatted text to the desired output file based on lines
       from an original input file and a related dictionary """
    in_lst = file_to_list(in_file)
    sorted_keys = sort_dictionary(dct)
    for element in sorted_keys:
        for i in range(0, len(dct[element])):
            write_line(out_file, format_justify(in_lst[dct[element][i] - 1], dct[element][i], element), "a")
    
def write_line(file_name, line, mode):
    """writes or appends the formated string into the file.(no string process here)"""
    output_file = open(file_name, mode)
    output_file.write(line)
    output_file.close()

def format_justify(line_str, line_number, key_word):
    """helper function(for the format_result_file).
       give the keyword, and return string,with 30 characters before justified
       , extra space, the keyword, and another 30 characters behind"""
    #find the case sensitive version of the keyword
    line_lower = line_str.lower()
    key_index = line_lower.find(key_word)
    key_word = line_str[key_index: key_index + len(key_word)]
    
    partition = line_str.partition(key_word)
    #cut off the first part of the string if it is too long
    if(len(partition[0]) > 30):
        first_portion = partition[0][len(partition[0]) - 30:]
    else:
        first_portion = partition[0]
    return str(line_number).ljust(4) + first_portion.rjust(30) + " " + partition[1] + partition[2].ljust(30) + "\n"

def sort_dictionary(dct):
    """sorts the elements of the dictionary numerically and returns a list
       of the dictionary keys sorted alphabetically"""
    key_list = []
    for i in range(0, len(dct)):
        dct[dct.keys()[i]].sort()
        key_list.append(dct.keys()[i])
    key_list.sort()
    return key_list

##def format_result_file(process_file_name):
##    """
##    format the result of a file(not files)
##    an element of process_files's list
##    """        
    
if __name__ == "__main__":
  main()

    
