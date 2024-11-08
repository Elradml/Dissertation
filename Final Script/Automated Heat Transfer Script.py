#The aim of this script is to create an automated method of performing heat transfer
#simulations on TexGen textiles in Abaqus
#Creates a voxel mesh objects and saves it
from tkinter import *
from tkinter import messagebox
import os
import subprocess
from TexGen.Core import *

print("START")

def run_inp(input_path):
    input_name = os.path.basename(input_path)

    job_name = os.path.splitext(input_name)[0]
    abaqus_command = f'abaqus job={job_name} inp="{input_path}"'
    
    try:
        subprocess.run(abaqus_command, shell = True, check = True)
        print(f"Job {job_name} completed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error running job {job_name}")
        print(e)
    print("FINISHED")

def add(new_path, add_lines, position):
    with open(new_path, "r") as file:
        lines = file.readlines()

    with open(new_path, "a") as file:
        for i in add_lines:
            file.write(i)
    
    with open(new_path, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "*Element, Type=C3D8" in line:
                lines[i] = line.replace(line, "*Element, Type=DC3D8\n")
    with open(new_path, "w") as file:
        file.writelines(lines)
    run_inp(new_path) 

def element_sets():
    #Face A
    count = 0
    with open(new_path, "r") as file:
        elements_A = []
        while True:
            end = False
            line = file.readline()
            if line.strip() == "*NSet, NSet=FaceA, Unsorted":
                found = True
                row = file.readline()
                while row:
                    if row.strip() == "*NSet, NSet=FaceB, Unsorted":
                        end = True
                        break
                    numbers = row.split()
                    row = file.readline()
                    for num in numbers:
                        elements_A.append(num)
            if end == True:
                break
        elements_A1 = [number.replace(",", "") for number in elements_A]
        elements = []

    with open(new_path, "r") as file:
        for index, line in enumerate(file):
            if line.strip() == "*Element, Type=C3D8" or line.strip() == "*Element, Type=C3D8R":
                index1 = index + 1
            elif line.strip() == "*** ORIENTATIONS ***":
                index2 = index - 1
                travel = index2 - index1
                break

    a_matches = []
    with open(new_path, "r") as file:
        file.seek(0)
        for i in range(index1):
            file.readline()
        for x in range(index1, index2 + 1):
            line = file.readline()
            row = line.split()
            for ro in row:
                elements.append(ro)
                elements1 = [find.replace(",", "") for find in elements]
                for y in elements_A1:
                    found = False
                    for y1 in elements1:
                        if y == y1:
                            found = True
                            a_matches.append(y)
                            elements.clear()

        a_matches1 = list(set(a_matches))
        a_int_list = [int(x) for x in a_matches1]
        a_int_list.sort()
        a_str_list = [str(x) for x in a_int_list]
        a_matches_final = [item + "," for item in a_str_list]

    #Face B
    with open(new_path, "r") as file:
        elements_B = []
        while True:
            end = False
            line = file.readline()
            if line.strip() == "*NSet, NSet=FaceB, Unsorted":
                found = True
                row = file.readline()
                while row:
                    if row.strip() == "*NSet, NSet=FaceC, Unsorted":
                        end = True
                        break
                    numbers = row.split()
                    row = file.readline()
                    for num in numbers:
                        elements_B.append(num)
            if end == True:
                break
        elements_B1 = [number.replace(",", "") for number in elements_B]
        elementsb1 = []

    with open(new_path, "r") as file:
        for index, line in enumerate(file):
            if line.strip() == "*Element, Type=DC3D8":
                index1 = index + 1
            elif line.strip() == "*** ORIENTATIONS ***":
                index2 = index - 1
                travel = index2 - index1
                break

    b_matches = []
    with open(new_path, "r") as file:
        file.seek(0)
        for i in range(index1):
            file.readline()
        for x in range(index1, index2 + 1):
            line = file.readline()
            row = line.split()
            for ro in row:
                elementsb1.append(ro)
                elementsb2 = [find.replace(",", "") for find in elementsb1]
                for y in elements_B1:
                    found = False
                    for y1 in elementsb2:
                        if y == y1:
                            found = True
                            b_matches.append(y)
                            elementsb1.clear()

        b_matches1 = list(set(b_matches))
        b_int_list = [int(x) for x in b_matches1]
        b_int_list.sort()
        b_str_list = [str(x) for x in b_int_list]
        b_matches_final = [item + "," for item in b_str_list]


    #FaceE
    with open(new_path, "r") as file:
        elements_E = []
        while True:
            end = False
            line = file.readline()
            if line.strip() == "*NSet, NSet=FaceE, Unsorted":
                found = True
                row = file.readline()
                while row:
                    if row.strip() == "*NSet, NSet=FaceF, Unsorted":
                        end = True
                        break
                    numbers = row.split()
                    row = file.readline()
                    for num in numbers:
                        elements_E.append(num)
            if end == True:
                break
        elements_E1 = [number.replace(",", "") for number in elements_E]
        elementse1 = []

    with open(new_path, "r") as file:
        for index, line in enumerate(file):
            if line.strip() == "*Element, Type=DC3D8":
                index1 = index + 1
            elif line.strip() == "*** ORIENTATIONS ***":
                index2 = index - 1
                travel = index2 - index1
                break

    e_matches = []
    with open(new_path, "r") as file:
        file.seek(0)
        for i in range(index1):
            file.readline()
        for x in range(index1, index2 + 1):
            line = file.readline()
            row = line.split()
            for ro in row:
                elementse1.append(ro)
                elementse2 = [find.replace(",", "") for find in elementse1]
                for y in elements_E1:
                    found = False
                    for y1 in elementse2:
                        if y == y1:
                            found = True
                            e_matches.append(y)
                            elementse1.clear()

        e_matches1 = list(set(e_matches))
        e_int_list = [int(x) for x in e_matches1]
        e_int_list.sort()
        e_str_list = [str(x) for x in e_int_list]
        e_matches_final = [item + "," for item in e_str_list]

    #FaceF
    with open(new_path, "r") as file:
        elements_F = []
        while True:
            end = False
            line = file.readline()
            if line.strip() == "*NSet, NSet=FaceF, Unsorted":
                found = True
                row = file.readline()
                while row:
                    if row.strip() == "*NSet, NSet=Edge1, Unsorted":
                        end = True
                        break
                    numbers = row.split()
                    row = file.readline()
                    for num in numbers:
                        elements_F.append(num)
            if end == True:
                break
        elements_F1 = [number.replace(",", "") for number in elements_F]
        elementsf1 = []

    with open(new_path, "r") as file:
        for index, line in enumerate(file):
            if line.strip() == "*Element, Type=DC3D8":
                index1 = index + 1
            elif line.strip() == "*** ORIENTATIONS ***":
                index2 = index - 1
                travel = index2 - index1
                break

    f_matches = []
    with open(new_path, "r") as file:
        file.seek(0)
        for i in range(index1):
            file.readline()
        for x in range(index1, index2 + 1):
            line = file.readline()
            row = line.split()
            for ro in row:
                elementsf1.append(ro)
                elementsf2 = [find.replace(",", "") for find in elementsf1]
                for y in elements_F1:
                    found = False
                    for y1 in elementsf2:
                        if y == y1:
                            found = True
                            f_matches.append(y)
                            elementsf1.clear()

        f_matches1 = list(set(f_matches))
        f_int_list = [int(x) for x in f_matches1]
        f_int_list.sort()
        f_str_list = [str(x) for x in f_int_list]
        f_matches_final = [item + "," for item in f_str_list]    

    print(a_matches_final)
    print(b_matches_final)
    print(e_matches_final)
    print(f_matches_final)

    with open(new_path, "r") as file:
        lines = file.readlines()

    with open(new_path, "w") as file:
        file.writelines(lines)
        file.write('*Elset, elset=FaceA11\n')
        for i in range(0, len(a_matches_final), 16):
            line = " ".join(a_matches_final[i:i+16])
            file.writelines(line + "\n")
        file.write("*Surface, NAME=FaceA1, TYPE=ELEMENT\n")
        file.write("FaceA11, S4\n")

        file.write('*Elset, elset=FaceB11\n')
        for i in range(0, len(b_matches_final), 16):
            line = " ".join(b_matches_final[i:i+16])
            file.writelines(line + "\n")
        file.write("*Surface, NAME=FaceB1, TYPE=ELEMENT\n")
        file.write("FaceB11, S4\n")

        file.write('*Elset, elset=FaceE11\n')
        for i in range(0, len(e_matches_final), 16):
            line = " ".join(e_matches_final[i:i+16])
            file.write(line + "\n")
        file.write("*Surface, NAME=FaceE1, TYPE=ELEMENT\n")
        file.write("FaceE11, S4\n")

        file.write('*Elset, elset=FaceF11\n')
        for i in range(0, len(f_matches_final), 16):
            line = " ".join(f_matches_final[i:i+16])
            file.write(line + "\n")
        file.write("*Surface, NAME=FaceF1, TYPE=ELEMENT\n")
        file.write("FaceF11, S4\n")
        
    add(new_path, add_lines, position)

def delete(inp, remove_indices):
    global updated_lines
    global new_path
    updated_lines = []
    count = 0
    with open(inp, "r") as file:
        lines = file.readlines()

    updated_lines = [line for i, line in enumerate(lines, start = 1) if i not in remove_indices]

    with open("delete_output.inp", "w") as file:
        file.writelines(updated_lines)
    new_path = inp
    
    element_sets()

def search():
    global blank_count
    global remove
    global ending1
    global remove_indices
    global traverse
    global traverse1
    global position
    count = 0
    with open(inp,"r") as f:
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
    print(position)
    delete(inp, remove_indices)

def new_lines():
    global add_lines
    add_lines = ['** MATERIALS\n', '*Material, name=Mat0\n', '*Conductivity, TYPE=ORTHO\n',
                  f'{int(conduct1)}.,\n', '**\n', '*Material, name=Mat1\n', '*Conductivity, TYPE=ORTHO\n' f'{int(conduct2)}.,\n' '**\n', '** PHYSICAL CONSTANTS\n', '**\n', 
                  '*Physical Constants, absolute zero=273.15, stefan boltzmann=5.67e-08\n', '** ----------------------------------------------------------------\n', 
                  '**\n', '** STEP: Heating Step\n', '**\n', '*Step, name="Heating Step", nlgeom=NO\n', 'Apply heat in this step\n', '*Heat Transfer, steady state, deltmx=0.\n', 
                  '1., 1., 1e-05, 1.,\n', '**\n', '** BOUNDARY CONDITIONS\n', '**\n', '** Name: Const temp surf 1 Type: Temperature\n', 
                  '*Boundary\n', f'FaceD, 11, 11, {int(bound1)}.\n', '** Name: Const temp surf2 Type: Temperature\n', '*Boundary\n',
                    f'FaceC, 11, 11, {int(bound2)}.\n', '**\n', '** INTERACTIONS\n', '**\n', '** Interaction: Convection 1\n', '*Sfilm\n',
                    f'FaceB1, F, {int(ambient)}., {int(film)}.\n', '** Interaction: Convection 2\n', '*Sfilm\n', f'FaceA1, F, {int(ambient)}., {int(film)}.\n',
                    '** Interaction: Convection 3\n', '*Sfilm\n', f'FaceE1, F, {int(ambient)}., {int(film)}.\n', '** Interaction: Convection 4\n',
                    '*Sfilm\n', f'FaceF1, F, {int(ambient)}., {int(film)}.\n', '** Interaction: Radiation 1\n', '*Sradiate\n', f'FaceB1, R, {int(ambient)}., {emiss1}\n',
                    '** Interaction: Radiation 2\n', '*Sradiate\n', f'FaceA1, R, {int(ambient)}., {emiss1}\n', '** Interaction: Radiation 3\n', '*Sradiate\n',
                    f'FaceE1, R, {int(ambient)}., {emiss2}\n', '** Interaction: Radiation 4\n', '*Sradiate\n', f'FaceF1, R, {int(ambient)}., {emiss2}\n',
                    '**\n', '** OUTPUT REQUESTS\n', '**\n', '*Restart, write, frequency=0\n', '**\n', '** FIELD OUTPUT: F-Output-1\n',
                    '**\n', '*Output, field, variable=PRESELECT\n', '*Output, history, frequency=0\n', '*End Step\n']
    search()


def thermal_data_properties():
    global conduct1
    global conduct2
    global emiss1
    global emiss2
    global film
    global ambient
    global bound1
    global bound2 

    conduct1 = float(t_conductivity1.get())
    conduct2 = float(t_conductivity2.get())
    emiss1 = float(emissivity1.get())
    emiss2 = float(emissivity2.get())
    ambient = float(amb_temp.get())
    film = float(film_co.get())
    bound1 = float(bt1.get())
    bound2 = float(bt2.get())

def thermal_properties():
    global t_conductivity1
    global t_conductivity2
    global emissivity1
    global emissivity2
    global amb_temp
    global film_co
    global bt1
    global bt2
    screen8.withdraw()
    screen7 = Toplevel(root)
    screen7.geometry('500x500')

    Label(screen7, text = "Thermal Properties", font = ('Helvetic', 10, 'bold')).place(x = 130, y = 0)
    Label(screen7, text = "Thermal Conductivity 1:").place(x = 0, y = 50)
    t_conductivity1 = Entry(screen7, textvariable = StringVar)
    t_conductivity1.place(x = 200, y = 50)

    Label(screen7, text = "Thermal Conductivity 2:").place(x = 0, y = 100)
    t_conductivity2 = Entry(screen7, textvariable = StringVar)
    t_conductivity2.place(x = 200, y = 100)

    Label(screen7, text = "Emissivity 1:").place(x = 0, y = 150)
    emissivity1 = Entry(screen7, textvariable = StringVar)
    emissivity1.place(x = 200, y = 150)

    Label(screen7, text = "Emissivity 2:").place(x = 0, y = 200)
    emissivity2 = Entry(screen7, textvariable = StringVar)
    emissivity2.place(x = 200, y = 200)

    Label(screen7, text = "Ambient Temperature (K):").place(x = 0, y = 250)
    amb_temp = Entry(screen7, textvariable = StringVar)
    amb_temp.place(x = 200, y = 250)

    Label(screen7, text = "Film Coefficient:").place(x = 0, y = 300)
    film_co = Entry(screen7, textvariable = StringVar)
    film_co.place(x = 200, y = 300)

    Label(screen7, text = "Boundary Temp 1 (K):").place(x = 0, y = 350)
    bt1 = Entry(screen7, textvariable = StringVar)
    bt1.place(x = 200, y = 350)

    Label(screen7, text = "Boundary Temp 2 (K):").place(x = 0, y = 400)
    bt2 = Entry(screen7, textvariable = StringVar)
    bt2.place(x = 200, y = 400)

    Button(screen7, text = "Finish", command = lambda:[thermal_data_properties(), new_lines()]).place(x = 200, y = 450)

def create_voxel():
    global inp
    inp = str(filename.get()) + ".inp"
    element = element_value.get()
    if element == "C3D8R":
        element = 0
    else:
        element = 1
    Textile.AssignDomain(CDomainPlanes(XYZ(-0.5, 0, -0.5), XYZ(1.5, 7, 0.5)))
    vox = CRectangularVoxelMesh()
    vox.SaveVoxelMesh(Textile, inp, int(vx.get()), int(vy.get()), int(vz.get()), output_matrix.get(), output_yarns.get(), MATERIAL_CONTINUUM, element)
    thermal_properties()

#Creates a volume pixel (voxel export) of the textile
def voxel_data():
    global filename
    global element_value
    global output_matrix
    global output_yarns
    global vx
    global vy
    global vz
    global screen8
    create = messagebox.askyesno(message = "Textile Created \n Would you like to create a voxel export of it?")
    if create == False:
        pass
    else:
        screen8 = Toplevel(root)
        screen8.geometry('350x450')
        Label(screen8, text = "X Voxel").place(x = 0, y = 0)
        Label(screen8, text = "Count:").place(x = 0, y = 25)
        vx = Entry(screen8, textvariable = IntVar)
        vx.place(x = 150, y = 25)

        Label(screen8, text = "Y Voxel").place(x = 0, y = 75)
        Label(screen8, text = "Count:").place(x = 0, y = 100)
        vy = Entry(screen8, textvariable = IntVar)
        vy.place(x = 150, y = 100)

        Label(screen8, text = "Z Voxel").place(x = 0, y = 150)
        Label(screen8, text = "Count:").place(x = 0, y = 175)
        vz = Entry(screen8, textvariable = IntVar)
        vz.place(x = 150, y = 175)

        Label(screen8, text = "Select Element Type:").place(x = 0, y = 210)
        element_type = ["C3D8","DC3D8"]
        element_value = StringVar(root)
        element_value.set("Select")
        option_menu = OptionMenu(screen8, element_value, *element_type)
        option_menu.place(x = 0, y = 250)

        output_yarns = BooleanVar()
        output_matrix = BooleanVar()
        Checkbutton(screen8, text = "Output Yarns", variable = output_yarns).place(x = 0, y = 310)
        Checkbutton(screen8, text = "Ouput Matrix", variable = output_matrix).place(x = 150, y = 310)

        Label(screen8, text = "Enter Input Filename:").place(x = 0, y = 355)
        filename = Entry(screen8, textvariable = StringVar)
        filename.place(x = 200, y = 355)

        Button(screen8, text = "finish", command = create_voxel).place(x = 150, y = 400)
        


#Creates the orthogonal 3D weave based upon the values received by the script (Taken from TexGen scripting guide)
def orthogonal():
    global Textile
    Textile = CTextileOrthogonal(direction_value, weft_yarn_value, spacing_value, spacing, height_value, height, brefine)
    Textile.SetWarpRatio(w_ratio)
    Textile.SetBinderRatio(binder)
    Textile.SetupLayers(num_layers1, layers)

    Textile.SetWarpYarnWidths(width_value)
    Textile.SetWarpYarnHeights(height_value)
    Textile.SetWarpYarnSpacings(spacing_value)

    Textile.SetBinderYarnWidths(bwidth)
    Textile.SetBinderYarnHeights(bheight)
    Textile.SetBinderYarnSpacings(bspacing)
    Textile.SetGapSize(bgap)

    Textile.SetYYarnWidths(width)
    Textile.SetYYarnSpacings(spacing)

    Textile.SetWarpYarnPower(power_value2)
    Textile.SetWeftYarnPower(power_value)
    Textile.SetBinderYarnPower(bpower_value)

    Textile.SwapBinderPosition(0,2)
    Textile.SwapBinderPosition(2,2)
    Textile.SwapBinderPosition(1,5)
    Textile.SwapBinderPosition(3,5)

    Textile.AssignDefaultDomain()

    Textile.SetFibreDiameter(WARP, diameter1, "m")
    Textile.SetFibreDiameter(WEFT, diameter, "m")
    Textile.SetFibreDiameter(BINDER, bdiameter, "m")

    Textile.SetFibresPerYarn(WARP, fpy1)
    Textile.SetFibresPerYarn(WEFT, fpy)
    Textile.SetFibresPerYarn(BINDER, bfpy)

    Textile.SetYarnLinearDensity(WARP, linear_density1, "kg/m")
    Textile.SetYarnLinearDensity(WEFT,linear_density, "kg/m")
    Textile.SetYarnLinearDensity(BINDER, bld, "kg/m")

    Textile.SetFibreDensity(WARP, fibre_density1, "kg/m^3")
    Textile.SetFibreDensity(WEFT, fibre_density, "kg/m^3")
    Textile.SetFibreDensity(BINDER, bfd, "kg/m^3")

    Textile.SetFibreArea(WARP, area1, "m^2")
    Textile.SetFibreArea(WEFT, area, "m^2")
    Textile.SetFibreArea(BINDER, barea, "m^2")

    Textile.SetThickness(thick_value)
    Textile.SetMaxVolFraction(bvol)
    Textile.SetDomainZValues()
    AddTextile(Textile)
    voxel_data()


def finish():
    complete = messagebox.askyesno(message = "Textile Data complete\n Are you sure you want to proceed?")
    if complete == True:
        root.iconify()
        screen6.withdraw()
        orthogonal()
    else:
        pass

def binder_data_properties():
    global bld
    global bfd
    global barea
    global bdiameter
    global bfpy

    bld = float(binder_Ldensity.get())
    bfd = float(binder_Fdensity.get())
    barea = float(binder_area.get())
    bdiameter = float(binder_diameter.get())
    bfpy = int(binder_fpy.get())

def binder_properties():
    global screen6
    global screen6_called
    global binder_Ldensity
    global binder_Fdensity
    global binder_area
    global binder_diameter
    global binder_fpy

    screen6_called = 1
    screen5.withdraw()
    screen6 = Toplevel(root)
    screen6.geometry('425x350')
    Label(screen6, text = "Enter Binder Yarn Properties", font = ('Helvetic', 10, 'bold')).place(x = 130, y = 0)
    Label(screen6, text = "Yarn Linear Density:").place(x = 0, y = 50)
    binder_Ldensity = Entry(screen6, textvariable = StringVar)
    binder_Ldensity.place(x = 160, y = 50)
    Label(screen6, text = "kg/m").place(x = 350, y = 50)

    Label(screen6, text = "Fibre Density:").place(x = 0, y = 100)
    binder_Fdensity = Entry(screen6, textvariable = StringVar)
    binder_Fdensity.place(x = 160, y = 100)
    Label(screen6, text = "kg/m^3").place(x = 350, y = 100)
    
    Label(screen6, text = "Fibre Area:").place(x = 0, y = 150)
    binder_area = Entry(screen6, textvariable = StringVar)
    binder_area.place(x = 160, y = 150)
    Label(screen6, text = "m^2").place(x = 350, y = 150)

    Label(screen6, text = "Fibre Diameter:").place(x = 0, y = 200)
    binder_diameter = Entry(screen6, textvariable = StringVar)
    binder_diameter.place(x = 160, y = 200)
    Label(screen6, text = "m").place(x = 350, y = 200)

    Label(screen6, text = "Fibres per Yarn:").place(x = 0, y = 250)
    binder_fpy = Entry(screen6, textvariable = StringVar)
    binder_fpy.place(x = 160, y = 250)
    
    Button(screen6, text = "Back", command = warp_properties).place(x = 165, y = 300)
    Button(screen6, text = "Finish", command = lambda:[binder_data_properties(), finish()]).place(x = 220, y = 300)

def warp_data_properties():
    global diameter1
    global fpy1
    global linear_density1
    global fibre_density1
    global area1

    fibre_density1 = float(warp_Fdensity.get())
    linear_density1 = float(warp_Ldensity.get())
    area1 = float(warp_area.get())
    diameter1 = float(warp_diameter.get())
    fpy1 =  int(warp_fpy.get())

def warp_properties():
    global screen5
    global warp_Ldensity
    global warp_Fdensity
    global warp_area
    global warp_diameter
    global warp_fpy
    global screen5_called
    global screen6_called
    if screen6_called == 1:
        screen6.withdraw()
    else:
        screen6_called = 0

    screen5_called = 1
    screen4.withdraw()
    screen5 = Toplevel(root)
    screen5.geometry('425x350')
    Label(screen5, text = "Enter Warp Yarn Properties", font = ('Helvetic', 10, 'bold')).place(x = 130, y = 0)
    Label(screen5, text = "Yarn Linear Density:").place(x = 0, y = 50)
    warp_Ldensity = Entry(screen5, textvariable = StringVar)
    warp_Ldensity.place(x = 160, y = 50)
    Label(screen5, text = "kg/m").place(x = 350, y = 50)

    Label(screen5, text = "Fibre Density:").place(x = 0, y = 100)
    warp_Fdensity = Entry(screen5, textvariable = StringVar)
    warp_Fdensity.place(x = 160, y = 100)
    Label(screen5, text = "kg/m^3").place(x = 350, y = 100)

    Label(screen5, text = "Fibre Area:").place(x = 0, y = 150)
    warp_area = Entry(screen5, textvariable = StringVar)
    warp_area.place(x = 160, y = 150)
    Label(screen5, text = "m^2").place(x = 350, y = 150)

    Label(screen5, text = "Fibre Diameter:").place(x = 0, y = 200)
    warp_diameter = Entry(screen5, textvariable = StringVar)
    warp_diameter.place(x = 160, y = 200)
    Label(screen5, text = "m").place(x = 350, y = 200)

    Label(screen5, text = "Fibres per Yarn:").place(x = 0, y = 250)
    warp_fpy = Entry(screen5, textvariable = StringVar)
    warp_fpy.place(x = 160, y = 250)
    
    Button(screen5, text = "Back", command = weft_properties).place(x = 165, y = 300)
    Button(screen5, text = "Next", command = lambda:[warp_data_properties(), binder_properties()]).place(x = 220, y = 300)

def weft_data_properties():
    global diameter
    global fpy
    global linear_density
    global fibre_density
    global area

    fibre_density = float(weft_Fdensity.get())
    linear_density = float(weft_Ldensity.get())
    area = float(weft_area.get())
    diameter = float(weft_diameter.get())
    fpy =  int(weft_fpy.get())

def weft_properties():
    global screen4
    global screen4_called
    global weft_Fdensity
    global weft_Ldensity
    global weft_area
    global weft_diameter
    global weft_fpy

    global screen5_called
    if screen5_called == 1:
        screen5.withdraw()
    else:
        screen5_called = 0

    screen4_called = 1
    screen3.withdraw()
    if ai == 0:
        global screen4
        screen4 = Toplevel(root)
        screen4.geometry('425x350')
        Label(screen4, text = "Enter Weft Yarn Properties", font = ('Helvetic', 10, 'bold')).place(x = 130, y = 0)
        Label(screen4, text = "Yarn Linear Density:").place(x = 0, y = 50)
        weft_Ldensity = Entry(screen4, textvariable = StringVar)
        weft_Ldensity.place(x = 160, y = 50)
        Label(screen4, text = "kg/m").place(x = 350, y = 50)

        Label(screen4, text = "Fibre Density:").place(x = 0, y = 100)
        weft_Fdensity = Entry(screen4, textvariable = StringVar)
        weft_Fdensity.place(x = 160, y = 100)
        Label(screen4, text = "kg/m^3").place(x = 350, y = 100)

        Label(screen4, text = "Fibre Area:").place(x = 0, y = 150)
        weft_area = Entry(screen4, textvariable = StringVar)
        weft_area.place(x = 160, y = 150)
        Label(screen4, text = "m^2").place(x = 350, y = 150)

        Label(screen4, text = "Fibre Diameter:").place(x = 0, y = 200)
        weft_diameter = Entry(screen4, textvariable = StringVar)
        weft_diameter.place(x = 160, y = 200)
        Label(screen4, text = "m").place(x = 350, y = 200)

        Label(screen4, text = "Fibres per Yarn:").place(x = 0, y = 250)
        weft_fpy = Entry(screen4, textvariable = StringVar)
        weft_fpy.place(x = 160, y = 250)
        
        Button(screen4, text = "Back", command = binder_screen).place(x = 165, y = 300)
        Button(screen4, text = "Next", command = lambda:[weft_data_properties(), warp_properties()]).place(x = 220, y = 300)
    else:
        pass

def angle_int():
    screen3.withdraw()
    textile = CTextileAngleInterlock(direction_value, weft_yarn_value, spacing_value, spacing, height_value, height)

    textile.SetWarpRatio(w_ratio)
    textile.SetBinderRatio(binder)
    textile.SetupLayers(num_layers1, layers)

    textile.SetWarpYarnWidths(width_value)
    textile.SetBinderYarnWidths(bwidth)
    textile.SetBinderYarnHeights(bheight)
    textile.SetWarpYarnHeights(height_value)
    textile.SetWarpYarnSpacings(spacing_value)
    textile.SetBinderYarnSpacings(bspacing)
    textile.SetYYarnSpacings(spacing)
    textile.SetGapSize(bgap)
    textile.SetWeftYarnPower(power_value)
    textile.SetWarpYarnPower(power_value2)
    textile.SetBinderYarnPower(bpower_value)

    textile.SetBinderYarnPositions(2,2)
    textile.SetBinderYarnPositions(4,1)
    textile.SetBinderYarnPositions(0,0)

    textile.AssignDefaultDomain()
    AddTextile(textile)

def binder_data():
    global bwidth
    global bheight
    global bspacing
    global bpower_value
    global thick_value
    global bvol
    global bgap
    global brefine

    bwidth = float(byarn_width.get())
    bheight = float(byarn_height.get())
    bspacing = float(byarn_spacing.get())
    bpower_value = float(bpower.get())
    bdomain1 = float(domain1.get())
    bdomain2 = float(domain2.get())
    bgap = float(gap_size.get())
    if ai == 0:
        thick_value = float(thickness.get())
        bvol = float(vol_frac.get())
        brefine = refine.get()
    else:
        pass 

def binder_screen():
    global screen4_called
    if screen4_called == 1:
        screen4.withdraw()
    else:
        screen4_called = 0
    global screen3_called
    global screen3
    global byarn_height
    global byarn_spacing
    global byarn_width
    global gap_size
    global bpower
    global thickness
    global vol_frac
    global refine
    global domain1
    global domain2
    screen2.withdraw()
    screen3_called = 1
    screen3 = Toplevel(root)
    screen3.geometry('500x500')
    Label(screen3, text = "Enter binder yarn data", font = ('Helvetic', 10, 'bold')).place(x = 170, y = 0)
    Label(screen3, text = "Yarn Width:").place(x = 0, y = 50)
    byarn_width = Entry(screen3, textvariable = StringVar)
    byarn_width.place(x = 150, y = 50)

    Label(screen3, text = "Yarn Height:").place(x = 0, y = 100)
    byarn_height = Entry(screen3, textvariable = StringVar)
    byarn_height.place(x = 150, y = 100)

    Label(screen3, text = "Yarn Spacing:").place(x = 0, y = 150)
    byarn_spacing = Entry(screen3, textvariable = StringVar)
    byarn_spacing.place(x = 150, y = 150)

    Label(screen3, text = "Gap size:").place(x = 0, y = 200)
    gap_size = Entry(screen3, textvariable = StringVar)
    gap_size.place(x = 150, y = 200)

    Label(screen3, text = "Power:").place(x = 0, y = 250)
    bpower = Entry(screen3, textvariable = StringVar)
    bpower.place(x = 150, y = 250)

    Label(screen3, text = "Target Thickness:").place(x = 0, y = 300)
    thickness = Entry(screen3, textvariable = StringVar)
    thickness.place(x = 150, y = 300)
    if ai == 1:
        thickness.config(state = "disabled")
    else:
        pass

    Label(screen3, text = "Max Yarn Volume \n Fraction:").place(x = 0, y = 350)
    vol_frac = Entry(screen3, textvariable = StringVar)
    vol_frac.place(x = 150, y = 350)
    if ai == 1:
        vol_frac.config(state = "disabled")
    else:
        pass

    refine = BooleanVar()
    domain1 = IntVar()
    domain2 = IntVar()
    if ai == 0:
        Checkbutton(screen3, text = "Refine", variable = refine).place(x = 20, y = 400)
    else:
        pass
    Checkbutton(screen3, text = "Create default domain", variable = domain1).place(x = 100, y = 400)
    Checkbutton(screen3, text = "Add 10% to domain height", variable = domain2).place(x = 310, y = 400)
    Button(screen3, text = "Back", command = warp_screen).place(x = 210, y = 450)
    if ai == 1:
        Button(screen3, text = "Finish", command = lambda:[binder_data(), angle_int()]).place(x = 270, y = 450)
    else:
        Button(screen3, text = "Next", command = lambda:[binder_data(), weft_properties()]).place(x = 270, y = 450)

def warp_data():
    global direction_value
    global binder
    global w_ratio
    global num_layers1
    global spacing_value
    global width_value
    global height_value
    global power_value2

    direction_value = int(yarn_direction.get())
    binder = int(binder_ratio.get())
    w_ratio = int(warp_ratio.get())
    spacing_value = float(warp_spacing.get())
    width_value = float(warp_width.get())
    height_value = float(warp_height.get())
    power_value2 = float(warp_power.get())
    num_layers1 = int(warp_layers.get())

def back2():
    screen2.withdraw()

def warp_screen():
    global screen3_called
    screen1.withdraw()
    if screen3_called == 1:
        screen3.withdraw()
    else:
        screen3_called = 0
    screen1.withdraw()
    global yarn_direction
    global binder_ratio
    global warp_ratio
    global warp_layers
    global warp_spacing
    global warp_width
    global warp_height
    global warp_power
    global screen2
    screen2_called = 1
    
    #Creation of screen 2
    screen2 = Toplevel(root)
    screen2.geometry('550x440')
    Label(screen2, text = "Enter warp yarn data:", font = ('Helvetic', 10, 'bold')).place(x = 110, y = 0)
    Label(screen2, text = "Yarns in warp direction:").place(x = 0, y = 50)
    yarn_direction = Entry(screen2, textvariable = StringVar)
    yarn_direction.place(x = 225, y = 50)

    Label(screen2, text = "Ratio of binder yarns:").place(x = 0, y = 100)
    binder_ratio = Entry(screen2, textvariable = StringVar)
    binder_ratio.place(x = 175, y = 100)

    Label(screen2, text = "to warp yarns:").place(x = 245, y = 100)
    warp_ratio = Entry(screen2, textvariable = StringVar)
    warp_ratio.place(x = 381, y = 100)

    Label(screen2, text = "Num. of yarn layers:").place(x = 0, y = 150)
    warp_layers = Entry(screen2, textvariable = StringVar)
    warp_layers.place(x = 225, y = 150)

    Label(screen2, text = "Yarn Spacing:").place(x = 0, y = 200)
    warp_spacing = Entry(screen2, textvariable = StringVar)
    warp_spacing.place(x = 225, y = 200)

    Label(screen2, text = "Yarn Width:").place(x = 0, y = 250)
    warp_width = Entry(screen2, textvariable = StringVar)
    warp_width.place(x = 225, y = 250)

    Label(screen2, text = "Yarn Height:").place(x = 0, y = 300)
    warp_height = Entry(screen2, textvariable = StringVar)
    warp_height.place(x = 225, y = 300)

    Label(screen2, text = "Power:").place(x = 0, y = 350)
    warp_power = Entry(screen2, textvariable = StringVar)
    warp_power.place(x = 225, y = 350)

    Button(screen2, text = "Back", command = lambda:[weft_screen(), back2()]).place(x = 195, y = 385)
    Button(screen2, text = "Next", command = lambda:[warp_data(), binder_screen()]).place(x = 250, y = 385)

def weft_data():
    #Retrieves all values in the weft_screen entry boxes
    global power_value
    global weft_yarn_value
    global layers
    global spacing
    global width
    global height
    weft_yarn_value = int(weft_yarn.get())
    layers = int(num_layers.get())
    spacing = float(yarn_spacing.get())
    width = float(yarn_width.get())
    height = float(yarn_height.get())
    power_value = float(power.get())
    if ai == 1:
        woffset = offset.get()
        print(woffset)
    else:
        pass
def back1():
    #closes weft_screen
    screen1.withdraw()

def weft_screen():
    global screen1
    global weft_yarn
    global num_layers
    global yarn_spacing
    global yarn_width
    global yarn_height
    global power
    global screen2_called
    global offset
    if screen2_called == 1:
        screen2.withdraw()
    else:
        screen2_called = 0
    screen1 = Toplevel(root)
    screen1.geometry('350x450')
    Label(screen1, text = "Enter weft yarn data:", font = ('Helvetic', 10, 'bold')).place(x = 55, y = 0)
    Label(screen1, text = "Yarns:").place(x = 0, y = 50)
    weft_yarn = Entry(screen1, textvariable = StringVar)
    weft_yarn.place(x = 175, y = 50)

    Label(screen1, text = "Num. of yarn layers:").place(x = 0, y = 100)
    num_layers = Entry(screen1)
    num_layers.place(x = 175, y = 100)

    Label(screen1, text = "Yarn spacing:").place(x = 0, y = 150)
    yarn_spacing = Entry(screen1)
    yarn_spacing.place(x = 175, y = 150)

    Label(screen1, text = "Yarn width:").place(x = 0, y = 200)
    yarn_width = Entry(screen1)
    yarn_width.place(x = 175, y = 200)

    Label(screen1, text = "Yarn height:").place(x = 0, y = 250)
    yarn_height = Entry(screen1)
    yarn_height.place(x = 175, y = 250)

    Label(screen1, text = "Power ellipse section:").place(x = 0, y = 300)
    power = Entry(screen1)
    power.place(x = 175, y = 300)
    
    Button(screen1, text = "Back", command = back1).place(x = 145, y = 400)
    Button(screen1, text = "Next", command = lambda:[weft_data(), warp_screen()]).place(x = 200, y = 400)
    offset = BooleanVar()
    if ai == 1:
        Checkbutton(screen1, text = "Offset weft yarns", variable = offset).place(x = 100, y = 350)
    else:
        pass

def orth_screen():
    global ai
    ai = 0

def angle_screen():
    global ai
    ai = 1

def root():
    global screen2_called
    global screen3_called
    global screen4_called
    global screen5_called
    global screen6_called
    global ai
    screen2_called = 0
    screen3_called = 0
    screen4_called = 0
    screen5_called = 0
    screen6_called = 0
    global root
    root = Tk()
    root.title("Automated Heat Transfer Script")
    Label(text = "Select Weave Type: ").pack()
    Button(text = "Orthogonal", command = lambda:[orth_screen(), weft_screen()]).pack()
    Button(text = "Angle Interlock", command = lambda:[angle_screen(), weft_screen()]).pack()
    Button(text = "Layer to Layer").pack()
    ai = 0
    root.mainloop()
root()

print("CLOSED")
