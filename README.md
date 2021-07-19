# Step-in_Python_mini_project
This is a python mini-project on file format converting

### commands to run

1. To run the main.py under your own environment, make new environment in the repo directory

            pip install venv
            
            python -m venv env
If OS is windows? run this

            env/Scripts/activate
            
If OS is linux? run this

            source env/Scripts/activate
            
2. Install the fpdf package 

            pip install fpdf
            
3. verify it 
 
            pip list
            
4. Run the main.py

            python main.py

5. To run the pytest on main

            pytest test_main.py


### Some details about the file structure and stuff

      main.py         ---> main program

      test_main.py    ---> pytest program for main.py

      myfile.txt      ---> a sample txt file to get started with

      /test           ---> contains all the template files for pytest(do not modify these)
      
      /target         ---> is where your converted file will be loacted(will be created only after running main.py once atleast)
      
      Python version  = 3.9
      pytest version  = 6.2.4
      no. of pytests  = 3
      
