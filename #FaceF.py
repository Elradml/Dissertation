path = "last.inp"

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
counter_a = 0
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
            print(elements1)
            result = set(elements1).issubset(elements_A1)
            print(x, result)
            if result == True:
                counter_a += 1
                a_matches.append(elements1[0])
                elements.clear 
                elements1.clear()
            else:
                elements.clear()
                elements1.clear()

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
counter_b = 0
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
            print(elementsb2)
            result = set(elementsb2).issubset(elements_B1)
            print(x, result)
            if result == True:
                counter_b += 1
                b_matches.append(elementsb2[0])
                elementsb1.clear 
                elementsb2.clear()
            else:
                elementsb1.clear()
                elementsb2.clear()

    b_matches1 = list(set(b_matches))
    b_matches_final = [item + "," for item in b_matches1]

counter_e = 0
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
            print(elementse2)
            result = set(elementse2).issubset(elements_E1)
            print(x, result)
            if result == True:
                counter_e += 1
                e_matches.append(elementse2[0])
                elementse1.clear 
                elementse2.clear()
            else:
                elementse1.clear()
                elementse2.clear()

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
counter = 0
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
            print(elementsf2)
            result = set(elementsf2).issubset(elements_F1)
            print(x, result)
            if result == True:
                counter += 1
                f_matches.append(elementsf2[0])
                elementsf1.clear 
                elementsf2.clear()
            else:
                elementsf1.clear()
                elementsf2.clear()

    f_matches1 = list(set(f_matches))
    f_int_list = [int(x) for x in f_matches1]
    f_int_list.sort()
    f_str_list = [str(x) for x in f_int_list]
    f_matches_final = [item + "," for item in f_str_list]


print("e", e_matches_final)
print("f", f_matches_final)
#print(counter)