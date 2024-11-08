#Testing bed for portion of code which will edit the input file to be used in Abaqus
#This method was used in the final code
print("Start")
path = "TexGen_generated_test.inp"

def add(new_path, add_lines, position):
    with open(new_path, "r") as file:
        lines = file.readlines()
    lines[position:position] = add_lines

    with open("Add.inp", "w") as file:
        file.writelines(lines)

    with open("Add.inp", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "*Element, Type=C3D8" in line:
                lines[i] = line.replace(line, "*Element, Type=DC3D8\n")
    with open("Add.inp", "w") as file:
        file.writelines(lines)
            
    


def delete(path, remove_indices):
    global updated_lines
    global new_path
    updated_lines = []
    count = 0
    with open(path, "r") as file:
        lines = file.readlines()

    updated_lines = [line for i, line in enumerate(lines, start = 1) if i not in remove_indices]

    with open("delete_output.inp", "w") as file:
        file.writelines(updated_lines)
    new_path = "delete_output.inp"    
    add(new_path, add_lines, position)
     



def search():
    global blank_count
    global remove
    global ending1
    global remove_indices
    global traverse
    global traverse1
    global position
    count = 0
    with open("TexGen_generated_test.inp","r") as f:
        blank_count = 0
        remove = []
        while True:
            count += 1
            line = f.readline()

            if line.strip() == "*** MATERIALS ***":
                find = True
                remove_indices = []
                index = count - 1
                ending = index + 13
                traverse = ending - index
                while find == True:
                    for i in range(traverse):
                        row = f.readline()
                        remove.append(row)
                        index += 1
                        remove_indices.append(index)
                    if index == ending:
                        break
                count += 13
            if line.strip() == "*** BOUNDARY CONDITIONS ***":
                find1 = True
                index1 = count - 1
                ending1 = index1 + 304
                traverse1 = ending1 - index1
                print("ENDING1", ending1)
                while find1 == True:
                    for i in range(traverse1):
                        row1 = f.readline()
                        remove.append(row1)
                        index1 += 1
                        remove_indices.append(index1)
                    if index1 == ending1:
                        break
            print("{}: {}".format(count, line.strip()))
            if not line:
                blank_count += 1
            if blank_count == 15:
                break
    position = ending1 - (traverse1 + traverse + 1)
    delete(path, remove_indices)

add_lines = ['**\n', '** STEP: Heating Step\n', '**\n','*Step, name="Heating Step", nlgeom=NO\n', 'Apply heat in this step\n', '*Heat Transfer, steady state, deltmx=0.\n', '1., 1., 1e-05, 1.,\n', '**\n', '** BOUNDARY CONDITIONS\n','**\n','** Name: Const temp surf 1 Type: Temperature\n','*Boundary\n', 'Set-1, 11, 11, 400.\n', '** Name: Const temp surf2 Type: Temperature\n', '*Boundary\n', 'Set-2, 11, 11, 300.\n', '**\n', '** INTERACTIONS\n', '**', '** Interaction: Convection 1\n', '*Sfilm\n', 'Surf-1, F, 200., 13.\n', '** Interaction: Convection 2\n', '*Sfilm\n', 'Surf-2, F, 200., 13.\n', '** Interaction: Convection 3\n', '*Sfilm\n', 'Surf-3, F, 200., 13.\n', '** Interaction: Convection 4\n', '*Sfilm\n', 'Surf-4, F, 200., 13.\n', '** Interaction: Radiation 1\n', '*Sradiate\n', 'Surf-5, R, 200., 0.78\n', '** Interaction: Radiation 2\n', '*Sradiate\n', 'Surf-6, R, 200., 0.78\n', '** Interaction: Radiation 3\n', '*Sradiate\n', 'Surf-7, R, 200., 0.78\n', '** Interaction: Radiation 4\n', '*Sradiate\n', 'Surf-8, R, 200., 0.78\n', '**\n', '** OUTPUT REQUESTS\n', '**\n', '*Restart, write, frequency=0\n', '**\n', '** FIELD OUTPUT: F-Output-1\n', '**\n', '*Output, field, variable=PRESELECT\n', '*Output, history, frequency=0\n', '*End Step\n']


search()
#print(blank_count)
print(remove_indices)
#print(updated_lines)
print(position)
test = ['faidaijfsf\n', f'dasfas{position}\n', 
        'fadsfd',position,'\n']
print(test)
print("Finish")