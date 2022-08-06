"""THIS FILE CLEANS DATA FROM raw_data.txt AND OUTPUT IS IN clean_data.txt"""

"""REMOVE EMPTY LINES"""
"""REMOVE '*' AND REPLACE"""
"""REMOVE LINES THAT START WITH '(' (this is required for getting data into dataModel)"""
"""GETs DATA INTO REQUIRED FORM"""
    
def readfile(file):
    with open(file,'r') as f:
        text = f.read()
    return text
def writefile(file,data):
    with open(file,'w') as f:
        f.write(data)

"""BELOW FUNCTION REMOVES EMPTY LINES AND LINES THAT START WITH '(' """

def remove_empty_lines(original_file,updated_file):
    with open(original_file, 'r') as f:
        lines = f.readlines()
    with open(updated_file, 'w') as f:
        lines = filter(lambda x: x.strip(), lines)
        f.writelines(lines)
#remove_empty_lines('storage/raw_data.txt','storage/line_operation1.txt')

def remove_line(infile,outfile):
    with open(infile,'r') as infile:
        dataList= infile.readlines()
        updated_dataList = []
        for list_ele in dataList:
            if list_ele[0] != '(':
                updated_dataList.append(list_ele)
    str1 = ''
    updated_dataList_string = str1.join(updated_dataList)
    writefile(outfile,updated_dataList_string)

#remove_line('storage/line_operation1.txt','storage/line_operation2.txt')

#####----------------------------------------------------------------------#####

ReplaceWordList = {
    "sh1t" : "shit",
    "f*cking" : "fucking",
    "f*ck" : "fuck",
    "f*uckin": "fuckin",
    "C*nty" : "Cunty",
    "f**ked": "fucked",

}
def string_replacement(read_file,write_file):
    data = open(read_file,'r').read()
    for word,replacement in ReplaceWordList.items():
        data = data.replace(word, replacement)
    with open(write_file,'w') as f:
        f.write(data)
#string_replacement('storage/line_operation2.txt','storage/words_removed.txt')

####----------------------------------------------------------------------#######
