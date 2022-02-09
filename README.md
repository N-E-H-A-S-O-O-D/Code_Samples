# Code_Samples
Assortment of different coding tasks
a)	The program **robot_dynamics.py** solves the 2D robot dynamics differential equations given below:
̇px(t) = v(t) cos(φ(t)),
̇py(t) = v(t) sin(φ(t)),
̇φ(t) = ωgyro(t),
where px, py is the position, φ is the orientation angle, v is the speed input, and ωgyro is the gyroscope reading.
1)	The speed is constant v(t) = 2 for the time interval t ∈ [0, 10] and zero otherwise.
2)	The orientation of the robot is upwards (and thus it moves up) in all time moments except during t ∈ [3, 7) when it does a 360-degree turn clockwise.
The differential equations are solved numerically using Euler’s method and the solution is visualized.

b)	**Description of electricity.py**
This program reads from a file contract of electric companies, determines the energy consumption of the user based on the size of their apartment and the number of residents, and asks the user for an estimate of their energy consumption. The program determines the cheapest and the most eco-friendly electricity contracts for the calculated energy consumption and the energy consumption estimated by the user.
Progression of the program
1.	First, the main function asks the user for the filename (electricity_contracts_1.txt) and extracts the information of the electric contracts or informs the user if the file cannot be read. 
2.	If reading the file succeeds, the main function asks the user for the size of the apartment, the number of the residents, and an estimate of the electricity consumption. Next, the program prints all contracts for the user. 
3.	Next, the main function calculates the electricity consumption of the user based on the size of the apartment and residents. Finally, the main function determines and prints the cheapest and the most eco-friendly contracts for the user estimated and the calculated consumption. 

c)The program **wind_turbine.py** reads the wind speeds from the file (wind_data_1.txt), calculates the hourly power of the wind turbine, the amount of the generated electrical energy, and the capacity factor.

d) The programs in rent-apartment.py and rent_house.py calculate rental incomes, compares rental incomes of 2 apartments, calculate return on equity, and check the price level of user-inputted apartments.
