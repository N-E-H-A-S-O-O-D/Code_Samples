import math

BASE_CONSM=2206 #kW
def calculate_consumption(size, residents):
    diff=size-30
    track=math.ceil(diff/10)
    percent_rise=0
    if track <=8:
        percent_rise=track*16
    else:
        track_large=math.ceil((size-110)/10)
        percent_rise=8*16 + track_large*5
    if (residents-1) <=2:
        percent_rise += (residents-1)*12
    else:
        percent_rise +=  2*12 + (residents-3) *7
    total_increase=BASE_CONSM*(1+percent_rise/100)
    return total_increase
def find_cheapest_contract(contracts, consumption):
    #The function returns the name of the cheapest contract and its annual costs in euros
    contract_list=[]
    contract_name=[]
    for namez, values in contracts.items():
        name=namez
        kWh_price=values['kWh_price']
        month_price=values["month_price"]
        annual_costs= month_price*12 + (consumption*kWh_price)/100
        contract_name.append([name, annual_costs])
        contract_list.append(annual_costs)
    contract_list.sort()
    cheapest_cost=contract_list[0]
    name=""
    for cn in contract_name:
        if cn[1] == cheapest_cost:
            name = cn[0]
    return name, cheapest_cost

def find_ecofriendly_contract(contracts, consumption):
    #The function returns the name of the cheapest contract and its annual costs in euros
    contract_list=[]
    contract_list_eco=[]
    contract_name=[]
    for namez, values in contracts.items():
        #values=contract.values()
        name=namez
        kWh_price=values['kWh_price']
        month_price=values["month_price"]
        annual_costs= month_price*12 + (consumption*kWh_price)/100
        contract_name.append([name, annual_costs, values["renewable"]])
        contract_list.append(annual_costs)
        contract_list_eco.append(values["renewable"])
    contract_list.sort()
    contract_list_eco.sort()
    #cheapest_cost=contract_list[0]
    eco_contract=contract_list_eco[len(contract_list_eco)-1]
    name=""
    eco_contracts=[]
    eco_contracts_cost=[]
    for cn in contract_name:
        if cn[2] == eco_contract:
            eco_contracts.append(cn)
            eco_contracts_cost.append(cn[1])
    eco_contracts_cost.sort()
    cheapest_cost=0
    for ec in eco_contracts:
        if ec[1] == eco_contracts_cost[0]:
            name=ec[0]
            cheapest_cost=ec[1]
    return name, cheapest_cost
def print_all_contracts(contracts):
    for k, v in contracts.items():
        print(k)
        print("   kWh_price: {:.2f}".format(v["kWh_price"]))
        print("   month_price: {:.2f}".format(v["month_price"]))
        print("   renewable: {:.2f}".format(v["renewable"]))
def main():
    name = input("Enter the file name.\n")
    contracts={}
    try:
        tempfile = open(name, "r")
        next(tempfile)
        for line in tempfile:
            line = line.rstrip()
            row = line.split(",")
            if (len(row) == 4):
                try:
                    contracts_temp={ row[0] : {"kWh_price": float(row[1]) , "month_price": float(row[2]), "renewable": float(row[3])/100}}
                    contracts.update(contracts_temp)
                except ValueError:
                    print("Invalid value: {},{},{},{}".format(row[0],row[1],row[2],row[3] ))
            elif(row[0] != ""):
                listToStr = ','.join([str(elem) for elem in row])
                print("Invalid line: {}".format(listToStr))
        tempfile.close()
        size = float(input("Enter the size of your apartment (m2).\n"))
        residents = int(input("Enter the number of residents.\n"))
        estimate = int(input("Enter an estimate of your annual electricity consumption (kWh).\n"))
        print_all_contracts(contracts)
        consumption=calculate_consumption(size, residents)
        namec, cheap_contract=find_cheapest_contract(contracts, consumption)
        name, cheapest_cost=find_ecofriendly_contract(contracts, consumption)
        print("\n")
        print("The best deals according to the calculated consumption ({:.0f} kwh):".format(consumption))
        if(cheap_contract == cheapest_cost):
            print("The cheapest contract is also the most eco-friendly and it is{} and costs {:.2f} eur/year.".format(name,cheapest_cost))
        else:
            print("The cheapest contract is {} and costs {:.2f} eur/year.".format(namec,cheap_contract ))
            print("The most eco-friendly contract is {} and costs {:.2f} eur/year.".format(name, cheapest_cost))
        print("\n")
        namec, cheap_contract = find_cheapest_contract(contracts, estimate)
        name, cheapest_cost = find_ecofriendly_contract(contracts, estimate)
        print("The best deals according to the user estimated consumption ({:.0f} kwh):".format(estimate))
        if(cheap_contract == cheapest_cost ):
            print("The cheapest contract is also the most eco-friendly and it is{} and costs {:.2f} eur/year.".format(namec, cheapest_cost))
        else:
            print("The cheapest contract is {} and costs {:.2f} eur/year.".format(namec, cheap_contract))
            print("The most eco-friendly contract is {} and costs {:.2f} eur/year.".format(name, cheapest_cost))
    except OSError:
        print("")
        print("Error while reading the file. Program ends.")
    except ValueError:
        print("Invalid value: {}.".format(row))

main()
