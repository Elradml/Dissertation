#Abaqus Input file creation test
print("BEGIN")
def create_input(filename):
    with open(filename, 'w') as f:
        f.write("*Heading\n")
        f.write("** Heat Transfer\n")
        f.write("** Job name: HeatTransferJobTest\n")
        f.write("*Node\n")
        f.write("1, 1., 0.5, 6.\n")
        f.write("2, 1., 0.25, 6.\n")
        f.write("*Element, type = C3D8\n")
        f.write("1, 1, 2, 3, 4, 5, 6, 7 , 8\n")
        f.write("*Material, name = Material-1\n")
        f.write("*Density\n")
        f.write("7800.,\n")
        f.write("*Elastic\n")
        f.write("200.00E9, 0.3\n")
        f.write("*Solid Section, elset = All_Elements, material = Material-1\n")
        f.write("1.0\n")
        f.write("*End Part\n")
        f.write("*Assembly, name = Assembly\n")
        f.write("*Instance\n")
        f.write("Assembly-1, Part = Part-1\n")
        f.write("*End Instance\n")
        f.write("*End Assembly\n")
        f.write("Step\n")
        f.write("*Static\n")
        f.write("*Boundary\n")
        f.write("1,1, 3\n")
        f.write("*Load\n")
        f.write("2, 2, 100.0\n")
        f.write("*Output, field\n")
        f.write("*Element Output\n")
        f.write("S, E, U\n")
        f.write("*End Step\n")

create_input("Test File.inp")
print("TEST COMPLETE")