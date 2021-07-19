import os
import sys

def main():
    print("\n\t\t\t\tWelcome, this is a file format converter, \n\t\t\tplease enter the dependency file name along with its extension")
    print("\t\t\t\t For example type 'myfile.txt' ")
    print("\t\t----------------------------------------------------------------------------------\n\n")
    dependency_file_name = input("\t\tEnter input file name here: ")
    try:
        os.mkdir("target")
        target_file_name =  "target/" + input("\n\t\tEnter output file name here: ")
    except:
        target_file_name =  "target/" + input("\n\t\tEnter output file name here(with extension): ")
    dependency_file_extension = dependency_file_name[(dependency_file_name.find('.')) : ]  #seperating extensions
    target_file_extension = target_file_name[(target_file_name.find('.')) : ]     #seperating extensions

    #Depedency file object creation
    try:
        dependency_file_obj = open(dependency_file_name, 'r')
    except:
        print("\t\tcould not find file named", dependency_file_name, "\n")
        sys.exit(0)

    if not target_file_extension == ".pdf":    #dont create a target file if the extension turns out to be .pdf
        #target file object creation
        try:
            target_file_obj = open(target_file_name, 'x')    #creating a file for the first time
        except:
            try:
                target_file_obj = open(target_file_name, 'w')    #if the file already exists
            except:
                print("could not find file named", target_file_name, "\n")
                sys.exit(0)

    #calling funcitons from here
    if dependency_file_extension == ".txt" and target_file_extension == ".hex":
        txt_to_hex(dependency_file_obj, target_file_obj)

    if dependency_file_extension == ".txt" and target_file_extension == ".bin":
        txt_to_bin(dependency_file_obj, target_file_obj)

    if dependency_file_extension == ".txt" and target_file_extension == ".pdf":
        txt_to_pdf(dependency_file_obj, target_file_name)

def txt_to_hex(dependency_file_obj, target_file_obj):
    """converts text file to hex file"""
    val = 0x00
    for lines in dependency_file_obj:
        for chrs in lines:
            val = hex(ord(chrs))[2:]    #converting each charecter to ASCII value, then to hex value, and chopping the '0x'
            target_file_obj.write(val+" ")
    target_file_obj.close()
    dependency_file_obj.close()

    print("\n\n\t\t your .txt file has been converted to .hex file, check 'target' folder\n\n")

def txt_to_bin(dependency_file_obj, target_file_obj):
    """converts text file to bin file"""
    val = 0
    for lines in dependency_file_obj:
        for chrs in lines:
            val = bin(ord(chrs))[2:]  #converting each charecter to ASCII value, then to bin value, and chopping the '0b'
            if len(val)<8:
                for _ in range(8-len(val)):  #adding extra '0' if the bin is not of 8bits
                    val = '0' + val
            target_file_obj.write(val + " ")
    target_file_obj.close()
    dependency_file_obj.close()

    print("\n\n\t\t your .txt file has been converted to .bin file, check 'target' folder\n\n")

def txt_to_pdf(dependency_file_obj, target_file_name):
    """converts text file to pdf file"""
    try:
        from fpdf import FPDF
    except:
        print("\t\tPlease install the 'fpdf' module in the current environment using command\n'pip install fpdf'\n")
        sys.exit(0)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    for lines in dependency_file_obj:   #writing into the pdf file
        pdf.cell(200, 10, txt=lines, ln=1, align='L')
    pdf.output(target_file_name)

    print("\n\n\t\t your .txt file has been converted to .pdf file, check 'target' folder\n\n")


if __name__ == "__main__":
    main()