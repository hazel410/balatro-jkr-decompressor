import os

decompressed_path = 'decompressed/profile_decoded.txt'

# opening file and storing the data
with open(decompressed_path, 'r') as file:
  raw_txt = file.read()

# indexing flags
flags = [
  "[\"career_stats\"]",
  "[\"all_unlocked\"]",
  "[\"stake\"]",
  "[\"joker_usage\"]",
  "[\"deck_stakes\"]",
  "[\"voucher_usage\"]",
  "[\"challenge_progress\"]",
  "[\"MEMORY\"]",
  "[\"hand_usage\"]",
  "[\"progress\"]",
  "[\"deck_usage\"]",
  "[\"consumable_usage\"]",
  "[\"high_scores\"]",
  "[\"name\"]",
  "[\"challenges_unlocked\"]"
]

# raw strings
string_list = [None] * len(flags)
for flag_num in range(len(flags)):
  start_str = raw_txt.find(flags[flag_num])
  if flag_num < 14:
    string_list[flag_num] = raw_txt[start_str:raw_txt.find(flags[flag_num+1])]
  else:
    string_list[flag_num] = raw_txt[start_str:]
print(raw_txt.find(flags[3]))
print(raw_txt.find(flags[4]))
print(string_list[3])

# ["stake"] isnt being properly found-- idk what memory is doing






