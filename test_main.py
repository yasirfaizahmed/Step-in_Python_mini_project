import sys
import os
#sys.path.insert(1, "C:\\Users\YASIR\Documents\STEPin Projects\Python_mini_project\src")
import main


def test_txt_to_hex():
    test_output_file = open("test/test_hex.hex", 'x')  #generating a hex file to get it tested 
    test_input_file = open("test/template_myfile.txt", 'r') #our tepmplate txt file
    template_file = open("test/template_hex.hex", 'r')  #our template hex file for camparing with generated hex file

    main.txt_to_hex(test_input_file, test_output_file)  #gets generated here
    
    test_output_file = open("test/test_hex.hex", 'r')
    template_file = open("test/template_hex.hex", 'r')
    for f, b in zip(template_file, test_output_file):   #testing here
        assert f == b
    test_output_file.close()
    template_file.close()


    os.remove("test/test_hex.hex")  #deleting the tested files


test_txt_to_hex()
    

