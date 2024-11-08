#Test bed for section of the code that will edit the input file
#This method was not used in the final code but could be used as an alternative method
thermal_conductivity1 = "401.,\n"
thermal_conductivity2 = "200.,\n"

print("Start")
def edit_input(input_file):
    with open(input_file, 'r') as f:
        input_contents = f.readlines()
    for i, line in enumerate(input_contents):
        print(line)
        try:
            words = line.strip().split()
        except:
            print("Empty row")
        if line[0:13] == "*** MATERIALS" in line:
            input_contents[i] = line.replace(line, "** MATERIALS\n")
        elif line[0:7] == "*Elasti":
            input_contents[i] = line.replace(line, "* Conductivity\n")
        elif line[0:10] == "3e+09, 0.2" in line:
            input_contents[i] = line.replace(line, thermal_conductivity1)
        elif line == "*Expansion,":
            input_contents[i].replace(line, "** PHYSICAL CONSTANTS\n")
        elif line == "*Expansion":
            input_contents[i] = line.replace(line, "**WHY\n")
        elif "6.5e-06" in line:
            input_contents[i] = line.replace(line, "DELETE\n")
        elif line[0:47] == "2e+11, 1e+10, 1e+10, 0.3, 0.4, 0.4, 5e+09, 5e+0" in line:
            input_contents[i] = line.replace(line, thermal_conductivity2)
        elif line[0:4] == "5e+0" in line:
            input_contents[i] = line.replace(line, "**\n")
        elif line[0:19] == "-2e-07, 3e-06, 3e-0" in line:
            input_contents[i] = line.replace(line, "**\n")
        elif line[0:42] == "*Solid Section, ElSet=Matrix, Material=Mat" in line:
            input_contents[i] = line.replace(line, "**Physical Constants, absolute zero=273.15, stefan boltzmann=5.67e-08\n** ----------------------------------------------------------------\n*Solid Section, ElSet=Matrix, Material=Mat0\n")
        #elif "" in line: 
            #input_contents[i] = line.replace(line, "** ----------------------------------------------------------------\n*Solid Section, ElSet=Matrix, Material=Mat0\n")

            
    


    with open("output_file.inp", 'w') as f:
        f.writelines(input_contents)

#Adds lines which are needed
    with open("output_file.inp", "r") as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            if line.strip() == "*Solid Section, ElSet=Matrix, Material=Mat0":
                index = i
                print("index is", index)

        add_lines = ['**\n', '** STEP: Heating Step\n', '**\n','*Step, name="Heating Step", nlgeom=NO\n', 'Apply heat in this step\n', '*Heat Transfer, steady state, deltmx=0.\n', '1., 1., 1e-05, 1.,\n', '**\n', '** BOUNDARY CONDITIONS\n','**\n','** Name: Const temp surf 1 Type: Temperature\n','*Boundary\n', 'Set-1, 11, 11, 400.\n', '** Name: Const temp surf2 Type: Temperature\n', '*Boundary\n', 'Set-2, 11, 11, 300.\n', '**\n', '** INTERACTIONS\n', '**', '** Interaction: Convection 1\n', '*Sfilm\n', 'Surf-1, F, 200., 13.\n', '** Interaction: Convection 2\n', '*Sfilm\n', 'Surf-2, F, 200., 13.\n', '** Interaction: Convection 3\n', '*Sfilm\n', 'Surf-3, F, 200., 13.\n', '** Interaction: Convection 4\n', '*Sfilm\n', 'Surf-4, F, 200., 13.\n', '** Interaction: Radiation 1\n', '*Sradiate\n', 'Surf-5, R, 200., 0.78\n', '** Interaction: Radiation 2\n', '*Sradiate\n', 'Surf-6, R, 200., 0.78\n', '** Interaction: Radiation 3\n', '*Sradiate\n', 'Surf-7, R, 200., 0.78\n', '** Interaction: Radiation 4\n', '*Sradiate\n', 'Surf-8, R, 200., 0.78\n', '**\n', '** OUTPUT REQUESTS\n', '**\n', '*Restart, write, frequency=0\n', '**\n', '** FIELD OUTPUT: F-Output-1\n', '**\n', '*Output, field, variable=PRESELECT\n', '*Output, history, frequency=0\n', '*End Step\n']
        lines[index:index] = add_lines

    with open("final_output.inp","w") as f:
        f.writelines(lines)

#Deletes lines which are not needed
    with open("final_output.inp", "r") as f:
        lines = f.readlines()
        for i, lines in enumerate(lines):
            if lines.strip() == "*** CREATE STEP ***":
                index = i - 1
            elif lines.strip() == "*Node Output, nset=ConstraintsDriver2":
                index2 = i + 3

    print("first index", index)
    print("second index", index2)
    lines = [line for i, line in enumerate(lines) if i < index or i > index2]
    with open("final_output.inp", "w") as f:
        f.writelines(lines)

input_file = "TexGen_generated_test.inp"
edit_input(input_file)
print("Finish")

#temp = f.readlines()
        #add_lines = []
        #for line in enumerate(temp):
            #add_lines.append(line)
            #if "*Solid Section, ElSet=Matrix, Material=Mat0" in line:
                #add_lines.append("")