
#### this module converts .txt file to .hex format 
dependentfilename = "myfile.txt"    #our file of depedency
try:
    file_txt = open(dependentfilename, 'r')
except:
    print("could not find file Named ", dependentfilename,"\n")
    exit(0)


targetfilename = "file_hex.hex"     #our file of target


    
def txt_to_hex(file_txt, targetfilename):
    try:
        file_hex = open(targetfilename, 'x')    #creating a file for the first time
    except:
        try:
            file_hex = open(targetfilename, 'w')    #if the file already exists
        except:
            print("could not find file named", targetfilename, "\n")
            exit(0)

    val = 0x00  
    for lines in file_txt:
        for chrs in lines:
            val = hex(ord(chrs))[2:]    #converting each charecter to ASCII value, then to hex value, and chopping the '0x'
            file_hex.write(val+" ")
    file_hex.close()
    file_txt.close()



txt_to_hex(file_txt, targetfilename)

