import re
'''
i have added the ability to have key="value"
added to tags for the extra credit
'''
__author__ = 'newScanTron'
print("what is up")
string_one = "this is stuff"

this = re.match('<[\w\s]+?>|<[\w\s]+?[=\s\*\?]"[\w\s]+?">', string_one)
this = re.match('<[\w\s]+?>', string_one)