#Test bed for creating element sets for Faces A, B, E, and F

path = "seven.inp"
#Face A
count = 0
with open(path, "r") as file:
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

with open(path, "r") as file:
    for index, line in enumerate(file):
        if line.strip() == "*Element, Type=DC3D8":
            index1 = index + 1
        elif line.strip() == "*** ORIENTATIONS ***":
            index2 = index - 1
            travel = index2 - index1
            break

a_matches = []
with open(path, "r") as file:
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
    a_matches_final = [item + "," for item in a_matches1]

#Face B
with open(path, "r") as file:
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

with open(path, "r") as file:
    for index, line in enumerate(file):
        if line.strip() == "*Element, Type=DC3D8":
            index1 = index + 1
        elif line.strip() == "*** ORIENTATIONS ***":
            index2 = index - 1
            travel = index2 - index1
            break

b_matches = []
with open(path, "r") as file:
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
    b_matches_final = [item + "," for item in b_matches1]


#FaceE
with open(path, "r") as file:
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

with open(path, "r") as file:
    for index, line in enumerate(file):
        if line.strip() == "*Element, Type=DC3D8":
            index1 = index + 1
        elif line.strip() == "*** ORIENTATIONS ***":
            index2 = index - 1
            travel = index2 - index1
            break

e_matches = []
with open(path, "r") as file:
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
    e_matches_final = [item + "," for item in e_matches1]

#FaceF
with open(path, "r") as file:
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

with open(path, "r") as file:
    for index, line in enumerate(file):
        if line.strip() == "*Element, Type=DC3D8":
            index1 = index + 1
        elif line.strip() == "*** ORIENTATIONS ***":
            index2 = index - 1
            travel = index2 - index1
            break

f_matches = []
with open(path, "r") as file:
    file.seek(0)
    for i in range(index1):
        file.readline()
    for x in range(index1, index2 + 1):
        line = file.readline()
        row = line.split()
        for ro in row:
            elementsf1.append(ro)
            elementsf2 = [find.replace(",", "") for find in elementsf1]
            result = all(item in elements_F1 for item in elementsf2)
            print(result)
            if result == True:
                f_matches.append(elementsf2[0]) 
                elementsf1.clear()
            else:
                pass       

            #for y in elements_F1:
                #found = False
                #for y1 in elementsf2:
                    #if y == y1:
                        #found = True
                        #f_matches.append(y)
                        #elementsf1.clear()

    f_matches1 = list(set(f_matches))
    f_int_list = [int(x) for x in f_matches1]
    f_int_list.sort()
    f_str_list = [str(x) for x in f_int_list]
    f_matches_final = [item + "," for item in f_str_list]    

with open(path, "r") as file:
    lines = file.readlines()
    start = "*NSet, NSet=MasterNode8, Unsorted\n"
    start_index = lines.index(start) + 3

with open("TESTER1.inp", "w") as file:
    file.writelines(lines)
    file.write('*Elset, elset=FaceA11\n')
    for i in range(start_index, len(a_matches_final), 16):
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

print(e_matches_final)
print(f_matches_final)