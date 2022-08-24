"""THIS FILE RETURNS character_name_list and quote_list """

from data_cleaning import *

DataModel = {"character_name": "","quote":""}

def listToString(s): 
    str1 = "" 
    return (str1.join(s))

character_name_list = []
quotes_list = []

def get_lists(readfile):
    with open(readfile, 'r') as f:
        data_list = f.readlines()
        ##SUBSTRING TILL ':' OCCURS END WHEN
        for list_ in data_list:
            c_name = list_.split(':')[0]
            quote_ = list_.split(':')[1]

            #performing string operations to quote_. REMOVE '\n' and space in the beginning.
            quote_ = quote_[1:]
            quote_ = quote_[:-1]

            character_name_list.append(c_name)
            quotes_list.append(quote_)
    return(character_name_list,quotes_list)
get_lists("storage/words_removed.txt")

DataModel = {"character_name": "","quote":""}
