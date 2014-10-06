import re
'''
i have added the ability to have key="value"
added to tags for the extra credit
'''
__author__ = 'newScanTron'
print("what is up")
xml_file = open('XML.txt', 'r+')
read_xml = xml_file.read()
xml_file_list = []
space_num = []
#going to  use this tag_list to know how many indents to use
tag_list = []
words_list = []
string_two = ""
#this regEx checks for <tag> | <tag key="value"> and their equevelient
#closeing tags
xml_file_list = re.split('(<[\w\s]+?>|<[\w\s]+?[=\s\*\?]"[\w\s]+?">|<[/\w\s]+?>)', read_xml)

def spacer(num_of_spaces):
    """
    thinking this might be the way to add the appropriate
    white space also recurssion cus we are talking about it
    :param num_of_spaces:
    :return:
    """
    if num_of_spaces > 1:
        space_num.append("    ")
        num_of_spaces -= 1
        spacer(num_of_spaces)
    return space_num


for string_one in xml_file_list:
    if re.match('<[\w\s]+?>|<[\w\s]+?[=\s\*\?]"[\w\s]+?">', string_one):
        print(string_one.rjust(len(tag_list)*12, ' '))
        tag_list.append(string_one)
    elif re.match('<[/\w\s]+?>', string_one):
        tag_list.pop()
        string_one.splitlines()
        print(string_one.rjust(len(tag_list)*12+1, ' '))
    elif re.match('[\w\s]+?', string_one):
        for each in string_one.split():
            words_list.append(each)
        print(spacer(len(tag_list)), words_list)


