import shutil
import os
import zlib

# establishing variables
home = os.path.expanduser('~')
balatro_path = home + '/.steam/debian-installation/steamapps/compatdata/2379780/pfx/drive_c/users/steamuser/AppData/Roaming/Balatro/'
save_file = '1'
file_names = ['meta','profile','save']
decompressed_path = home + '/Documents/coding/python/jkr_decompressor/decompressed'

# goes through meta, profile, and save
for current_file in range(len(file_names)):

  # establishes shorthand for paths
  input_path = balatro_path+save_file+'/'+file_names[current_file]
  output_path = decompressed_path+'/'+file_names[current_file]

  # makes a copy of the file to work with
  shutil.copyfile(input_path+'.jkr',output_path+'_copy.jkr')

  # opening file and storing the data
  with open(output_path+'_copy.jkr', 'rb') as file:
    save_file_data = file.read()

  # decompressing the file
  output_data = zlib.decompress(save_file_data, wbits=-zlib.MAX_WBITS)  

  # writes the decrypted file to output
  with open(output_path+'_decoded.txt', 'w', encoding="ascii") as current_output:
    current_output.write(str(output_data))

  # deletes the copy
  os.remove(output_path+'_copy.jkr')

print("code done now :]")






