
def main():
    print("\n\t\t\t\tWelcome, this is a file format converter, \n\t\t\tplease enter the dependency file name along with its extension")
    print("\t\t----------------------------------------------------------------------------------\n\n")
    dependency_file_name = input("\t\tEnter here: ")
    target_file_name = input("\n\t\tEnter here: ")
    dependency_file_extension = dependency_file_name[(dependency_file_name.find('.')) : ]  #seperating extensions
    target_file_extension = target_file_name[(target_file_name.find('.')) : ]     #seperating extensions

    #Depedency file object creation
    try:
        dependency_file_obj = open(dependency_file_name, 'r')
    except:
        print("\t\tcould not find file named\n", dependency_file_name)
    
    #target file object creation
    try:
        target_file_obj = open(target_file_name, 'x')    #creating a file for the first time
    except:
        try:
            target_file_obj = open(target_file_name, 'w')    #if the file already exists
        except:
            print("could not find file named", target_file_name, "\n")
            exit(0)


    if dependency_file_extension == ".txt" and target_file_extension == ".hex":
        txt_to_hex(dependency_file_obj, target_file_obj)
    if dependency_file_extension == ".txt" and target_file_extension == ".bin":
        txt_to_bin(dependency_file_obj, target_file_obj)

 
    

def txt_to_hex(dependency_file_obj, target_file_obj):
    val = 0x00  
    for lines in dependency_file_obj:
        for chrs in lines:
            val = hex(ord(chrs))[2:]    #converting each charecter to ASCII value, then to hex value, and chopping the '0x'
            target_file_obj.write(val+" ")
    target_file_obj.close()
    dependency_file_obj.close()

    print("\n\n\t\t your .txt file has been converted to .hex file\n\n")

def txt_to_bin(dependency_file_obj, target_file_obj):
    val = 0
    for lines in dependency_file_obj:
        for chrs in lines:
            val = bin(ord(chrs))[2:]
            if len(val)<8:
               for i in range(8-len(val)):
                   val = '0' + val
            target_file_obj.write(val + " ")
    target_file_obj.close()
    dependency_file_obj.close()

    print("\n\n\t\t your .txt file has been converted to .bin file\n\n")




if __name__ == "__main__":
    main()

