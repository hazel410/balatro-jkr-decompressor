import os

decompressed_path = 'decompressed/profile_decoded.txt'

# opening file and storing the data
with open(decompressed_path, 'r') as file:
  raw_txt = file.read()
raw_txt = raw_txt[(raw_txt.find("{")+1):raw_txt.rfind("}")]

# initializing loop vars
left_bbracket = 0
right_bbracket = 0
left_cbracket = 0
right_cbracket = 0
section_keys = []
section_text = []
temp_list = []


def list_to_word(input_list):
  temp_output = ""
  for character in input_list:
    if character != "\"":
      temp_output = temp_output + character
  return temp_output

for char in raw_txt:
  # updating counts of brackets
  if char == "{":
    left_cbracket += 1
  elif char == "}":
    right_cbracket += 1
  elif char == "[":
    left_bbracket += 1
  elif char == "]":
    right_bbracket += 1
  
  # if we're inside box brackets that aren't nested in curly brackets, log the text
  if left_cbracket == right_cbracket and left_bbracket > right_bbracket:
    temp_list.append(char)
  
  # if we're inside un-nested cbrackets log the text
  if left_cbracket > right_cbracket:
    temp_list.append(char)
  
  # for the edge case of the format "[example_key]=20" (notice the lack of cbrackets)
  if left_bbracket == right_bbracket and left_cbracket == right_cbracket:
    temp_list.append(char)
  
  # if we're closing an un-nested curly bracket, log it
  if char == "}" and left_cbracket == right_cbracket:
    section_text.append(list_to_word(temp_list))
    temp_list = []
  
  # if we're closing an un-nested box bracket log it
  if char == "]" and left_cbracket == right_cbracket:
    section_keys.append(list_to_word(temp_list[1:]))
    temp_list = []
  
  # for the edge case
  if char == "{" and left_bbracket == right_bbracket and left_cbracket == right_cbracket + 1:
    section_text.append(list_to_word(temp_list))
    temp_list = []
  

# hopefully everything works now
# print(section_keys)

# print(len(section_keys))
# print(len(section_text))

  
  
  










