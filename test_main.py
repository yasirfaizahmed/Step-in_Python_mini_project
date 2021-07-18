import sys
import os
#sys.path.insert(1, "C:\\Users\YASIR\Documents\STEPin Projects\Python_mini_project\src")
import main

#definifn all the test fucntions here
def test_txt_to_hex():
    test_output_file = open("test/test_hex.hex", 'x')  #generating a hex file to get it tested 
    test_input_file = open("test/template_myfile.txt", 'r') #our tepmplate txt file
    template_file = open("test/template_hex.hex", 'r')  #our template hex file for camparing with generated hex file

    main.txt_to_hex(test_input_file, test_output_file)  #gets generated here
    
    test_output_file = open("test/test_hex.hex", 'r')   #opening again 
    template_file = open("test/template_hex.hex", 'r')  #opening again
    for f, b in zip(template_file, test_output_file):   #testing here
        assert f == b
    test_output_file.close()
    template_file.close()

    os.remove("test/test_hex.hex")  #deleting the tested files



def test_txt_to_bin():
    test_output_file = open("test/test_bin.bin", 'x')
    test_input_file = open("test/template_myfile.txt", 'r')
    template_file = open("test/template_bin.bin", 'r')

    main.txt_to_bin(test_input_file, test_output_file)

    test_output_file = open("test/test_bin.bin", 'r')
    template_file = open("test/template_bin.bin", 'r')
    for f, b in zip(template_file, test_output_file):
        assert f == b
    test_output_file.close()
    template_file.close()

    os.remove("test/test_bin.bin")



def test_txt_to_pdf():
    #test_output_file = open("test/test_pdf.pdf", 'x')
    test_input_file = open("test/template_myfile.txt", 'r')
    template_file = open("test/template_pdf.pdf", 'rb')

    main.txt_to_pdf(test_input_file, "test_pdf.pdf")

    test_output_file = open("test_pdf.pdf", 'rb')

    for bits1, bits2 in zip(template_file, test_output_file):
       if b'/CreationDate' in bits1 or b'/CreationDate' in bits2:   #ignoring the DateOfCreation while comparing all the pdf bytes
           continue
       else:
           assert bits1 == bits2    #if not the DateOfCreation byte? assert 

    test_output_file.close()
    test_input_file.close()
    template_file.close()
    
    os.remove("test_pdf.pdf")
    



test_txt_to_pdf()