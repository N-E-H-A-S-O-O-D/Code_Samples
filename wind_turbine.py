RHO =1.225
#in kW
MAX_POWER=3450
CUT_IN_VEL=3 #m/s
CUT_OUT_VEL=25 #m/s
A=8659 #metre square
def calculate_powers(velocities_list):
    power_list=[]
    p=0.0
    #hourly power in kW
    for v in velocities_list:
        if v < CUT_IN_VEL or v> CUT_OUT_VEL:
            p=0.0
        else:
            p = (8 / 27 * RHO * v**3 * A)/1000
        power_list.append(p)
    return power_list
def calculate_capacity_factor(power_list):
    capacity_factor=0
    #generated electric energy
    gen_elec_energy=sum(power_list)
    highest_power= MAX_POWER*len(power_list)
    if highest_power!=0:
        capacity_factor=gen_elec_energy/highest_power
    return capacity_factor
def main():
    name = input("Enter the name of the file containing wind velocities.\n")
    wind_speed = []
    try:
        tempfile = open(name, "r")
        next(tempfile)
        for line in tempfile:
            line = line.rstrip()
            row=line.split(",")
            if(len(row) == 6):
                wind_speed.append(float(row[5]))
        tempfile.close()
        power_list = calculate_powers(wind_speed)
        capacity_factor = calculate_capacity_factor(power_list)
        gen_elec_energy = sum(power_list)
        if len(power_list) != 0:
            print("The maximum power of the wind turbine was {:.1f} kW.".format(max(power_list)))
        print("The wind turbine generated {:.1f} kWh of electricity.".format(gen_elec_energy))
        print("The capacity factor of the wind turbine was {:.3f}.".format(capacity_factor))
    except OSError:
        print("")
        print("Error while reading the '{}' file. Program ends.".format(name))
    except ValueError:
        print("Incorrect time in the file {}. Program ends.".format(name))

main()