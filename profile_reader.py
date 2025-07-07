import os

decompressed_path = 'decompressed/profile_decoded.txt'

# opening file and storing the data
with open(decompressed_path, 'r') as file:
  raw_txt = file.read()
raw_txt = raw_txt[(raw_txt.find("{")+1):raw_txt.rfind("}")]

flag = "[\"joker_usage\"]="
joker_index = raw_txt.find(flag)
left_bracket = 0
right_bracket = 0
temp = ""

for character in raw_txt[joker_index + len(flag)]:
  if character == "{":
    left_bracket += 1
  elif character == "}":
    right_bracket += 1
  
  temp = temp + character
  
  

  


  
  
  










