import re
'''
i have added the ability to have key="value"
added to tags for the extra credit
'''
__author__ = 'newScanTron'
xml_file = open('XML.txt', 'r+')
read_xml = xml_file.read()
xml_file_list = []
#going to  use this tag_list to know how many indents to use
tag_list = []
words_list = []
string_string = ""
#this regEx checks for <tag> | <tag key="value"> and their equevelient
#closeing tags
xml_file_list = re.split('(<[\w\s]+?>|<[\w\s]+?[=\s\*\?]"[\w\s]+?">|<[/\w\s]+?>)', read_xml)


def spacer(num_of_spaces):
    """
    thinking this might be the way to add the appropriate
    white space also recurssion cus we are talking about it. for some
    reason that does not work right so a while loop is less stupid to fix
    :param num_of_spaces:
    :return:
    """
    space_num = ""
    # if num_of_spaces > 1:
    #     space_num += "    "
    #     num_of_spaces -= 1
    #     spacer(num_of_spaces)
    while num_of_spaces > 1:
        space_num += "    "
        num_of_spaces -= 1
    return space_num

for string_one in xml_file_list:
    if re.match('<[\w\s]+?>|<[\w\s]+?[=\s\*\?]"[\w\s]+?">', string_one):
        tag_list.append(string_one)
        print(spacer(len(tag_list)), string_one)

    elif re.match('<[/\w\s]+?>', string_one):
        string_one.splitlines()
        print(spacer(len(tag_list)), string_one)
        tag = tag_list.pop()
        #split here on the not words stuff

        if not re.match('<[/\w\s]+?>', tag):
            print(" you suck so hard")
    elif re.match('[\w\s]+?', string_one):
        string_one = re.split('[\s]+?', string_one)
        for each in string_one:
            string_string += each

        if len(string_string) > 0:
            print(spacer(len(tag_list)), string_string)
            string_string = ''


