
#### this module converts .txt file to .hex format 
dependentfilename = "myfile.txt"    #our depedency file
try:
    file_txt = open(dependentfilename, 'r')
except:
    print("could not find file Named ", dependentfilename,"\n")
    exit(0)




targetfilename = "file_hex.hex"     #our target file

def main():
    print("\n\t\t\t\tWelcome, this is a file format converter, \n\t\t\tplease enter the dependency file name along with its extension")
    print("\t\t----------------------------------------------------------------------------------\n\n")
    depdendency_file_name = input("\t\tEnter here: ")
    target_file_name = input("\n\t\tEnter here: ")
    depdendency_file_extension = depdendency_file_name[(depdendency_file_name.find('.')+1) : ]  #here we are detecting the extension of the dependency file
    print(depdendency_file_extension)
 
    

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


if __name__ == "__main__":
    main()
    txt_to_hex(file_txt, targetfilename)

