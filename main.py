########################################################################################################################
############################### some definitions of the important valiables defined below ##############################

#1. dependency_file_name - input file name from the user  (this file must be in the local folder and the name should match with the inputed name)
#2. target_file_name - name of the file user wants to create (with extension)

#3. dependency_file_extension - extension of the dependency file
#4. target_file_extension - extension of the target file

#5. dependency_file_obj - depedency file object
#6. target_file_obj - target file object
########################################################################################################################

def main():
    print("\n\t\t\t\tWelcome, this is a file format converter, \n\t\t\tplease enter the dependency file name along with its extension")
    print("\t\t----------------------------------------------------------------------------------\n\n")
    dependency_file_name = input("\t\tEnter here: ")
    target_file_name = "target/" + input("\n\t\tEnter here: ")
    dependency_file_extension = dependency_file_name[(dependency_file_name.find('.')) : ]  #seperating extensions
    target_file_extension = target_file_name[(target_file_name.find('.')) : ]     #seperating extensions

    #Depedency file object creation
    try:
        dependency_file_obj = open(dependency_file_name, 'r')
    except:
        print("\t\tcould not find file named", dependency_file_name, "\n")
        exit(0)

    if not(target_file_extension == ".pdf"):    #dont create a target file if the extension turns out to be .pdf
        #target file object creation
        try:
            target_file_obj = open(target_file_name, 'x')    #creating a file for the first time
        except:
            try:
                target_file_obj = open(target_file_name, 'w')    #if the file already exists
            except:
                print("could not find file named", target_file_name, "\n")
                exit(0)

    #calling funcitons from here
    if dependency_file_extension == ".txt" and target_file_extension == ".hex":
        txt_to_hex(dependency_file_obj, target_file_obj)

    if dependency_file_extension == ".txt" and target_file_extension == ".bin":
        txt_to_bin(dependency_file_obj, target_file_obj)

    if dependency_file_extension == ".txt" and target_file_extension == ".pdf":
        txt_to_pdf(dependency_file_obj, target_file_name)

 
    

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
            val = bin(ord(chrs))[2:]  #converting each charecter to ASCII value, then to bin value, and chopping the '0b'
            if len(val)<8:
               for i in range(8-len(val)):  #adding extra '0' if the bin is not of 8bits
                   val = '0' + val
            target_file_obj.write(val + " ")
    target_file_obj.close()
    dependency_file_obj.close()

    print("\n\n\t\t your .txt file has been converted to .bin file\n\n")

def txt_to_pdf(dependency_file_obj, target_file_name):
    try:
        from fpdf import FPDF
    except:
        print("\t\tPlease install the 'fpdf' module in the current environment using command\n'pip install fpdf'\n")
        exit(0)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    for lines in dependency_file_obj:   #writing into the pdf file
        pdf.cell(200, 10, txt=lines, ln=1, align='L')
    pdf.output(target_file_name)

    print("\n\n\t\t your .txt file has been converted to .pdf file\n\n")


if __name__ == "__main__":
    main()

