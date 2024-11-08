#The aim of this script is to create an automated method of performing heat transfer
#simulations on TexGen textiles in Abaqus
#Creates a voxel mesh objects and saves it
from tkinter import *
from tkinter import messagebox
from TexGen.Core import *

print("Start")
def thermal_data_properties():
    global conduct
    global emiss
    global film
    global ambient
    global bound1
    global bound2 

    conduct = float(t_conductivity.get())
    emiss = float(emissivity.get())
    ambient = float(amb_temp.get())
    film = float(film_co.get())
    bound1 = float(bt1.get())
    bound2 = float(bt2.get())

def thermal_properties():
    global t_conductivity
    global emissivity
    global amb_temp
    global film_co
    global bt1
    global bt2
    screen8.withdraw()
    screen7 = Toplevel(root)
    screen7.geometry('500x400')

    Label(screen7, text = "Enter Thermal Properties", font = ('Helvetic', 10, 'bold')).place(x = 130, y = 0)
    Label(screen7, text = "Thermal Conductivity:").place(x = 0, y = 50)
    t_conductivity = Entry(screen7, textvariable = StringVar)
    t_conductivity.place(x = 200, y = 50)

    Label(screen7, text = "Emissivity:").place(x = 0, y = 100)
    emissivity = Entry(screen7, textvariable = StringVar)
    emissivity.place(x = 200, y = 100)

    Label(screen7, text = "Ambient Temperature:").place(x = 0, y = 150)
    amb_temp = Entry(screen7, textvariable = StringVar)
    amb_temp.place(x = 200, y = 150)

    Label(screen7, text = "Film Coefficient:").place(x = 0, y = 200)
    film_co = Entry(screen7, textvariable = StringVar)
    film_co.place(x = 200, y = 200)

    Label(screen7, text = "Boundary Temp 1:").place(x = 0, y = 250)
    bt1 = Entry(screen7, textvariable = StringVar)
    bt1.place(x = 200, y = 250)

    Label(screen7, text = "Boundary Temp 2:").place(x = 0, y = 300)
    bt2 = Entry(screen7, textvariable = StringVar)
    bt2.place(x = 200, y = 300)

    Button(screen7, text = "Finish").place(x = 200, y = 350)

def create_voxel():
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
        element_type = ["C3D8R","C3D8"]
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

print("Finished")
