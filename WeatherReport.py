# an aggie does not lie cheat or steal nor tolerate those who do
# i did not receive unaothorized aid on this assignment
# daniel lohn   427004202    510



import matplotlib.pyplot as plt



average_temp = []
average_pressure = []
average_dew = []
precipitation = []
pressure = []
# i am very sorry for what youre about to see, but yah boi ran out of options on how to solve this very tedious problem
month_1_avg_temp = []  # January
month_2_avg_temp = []  # February
month_3_avg_temp = []  # March
month_4_avg_temp = []  # April
month_5_avg_temp = []  # May
month_6_avg_temp = []  # June
month_7_avg_temp = []  # July
month_8_avg_temp = []  # August
month_9_avg_temp = []  # Sept
month_10_avg_temp = []  # October
month_11_avg_temp = []  # November
month_12_avg_temp = []  # December
date_sup_list = []
# gotta isolate these variables ya dig
with open('WeatherDataWindows.csv', 'r') as my_file:
    # Skip Header
    my_file.readline()
    for i in range(0, 1095):   # reads literally every day in this sheet
        date_str = my_file.readline()   # nah this reads everything
        date_list = list((date_str[:(len(date_str) - 1)]).split(','))
        average_temp.append(float(date_list[2]))  # temp is found in the third column
        pressure.append(float(date_list[11]))  # pressure is found in the 12th column
        precipitation.append(float(date_list[13]))   # precipitation is found in the 14th column
        average_dew.append(float(date_list[5]))    # dew is found in the 6th column
        date = date_list[0].split('/')    # dat, of course, found in first column
        date_sup_list.append(float(date[0])+(float(date[1])/32)+((float(date[2])-2015)*12))

        # This Part basically splits the months up into separate files so i can further mess with them
        # also this basically checks the months using the first digit in the dates list, it works because the dates
        # start with the month
        if date[0] == '1':
            month_1_avg_temp.append(float(date_list[2]))
        elif date[0] == '2':
            month_2_avg_temp.append(float(date_list[2]))
        elif date[0] == '3':
            month_3_avg_temp.append(float(date_list[2]))
        elif date[0] == '4':
            month_4_avg_temp.append(float(date_list[2]))
        elif date[0] == '5':
            month_5_avg_temp.append(float(date_list[2]))
        elif date[0] == '6':
            month_6_avg_temp.append(float(date_list[2]))
        elif date[0] == '7':
            month_7_avg_temp.append(float(date_list[2]))
        elif date[0] == '8':
            month_8_avg_temp.append(float(date_list[2]))
        elif date[0] == '9':
            month_9_avg_temp.append(float(date_list[2]))
        elif date[0] == '10':
            month_10_avg_temp.append(float(date_list[2]))
        elif date[0] == '11':
            month_11_avg_temp.append(float(date_list[2]))
        elif date[0] == '12':
            month_12_avg_temp.append(float(date_list[2]))
# imma make the pressure and temp graph here
fig, ax1 = plt.subplots()    # thanks a lot stack overflow for showing me how to do this
ax2 = ax1.twinx()    # again thank stack overflow for showing me how to make two variables into one axis
ax2.plot(date_sup_list, pressure, color='b')    # i wanted mine to be blue
ax1.plot(date_sup_list, average_temp)   #
ax1.set_title("Average Temperature And Pressure")
ax1.set_xlabel("Months Since January 2015")
ax1.set_ylabel("Average Temperature", color='g')
ax2.set_ylabel("Average Pressure", color='r')
plt.show()


fig, pre = plt.subplots()
pre.hist(precipitation)
pre.set_title("Precipitation Over Time")
pre.set_xlabel("Amount of Precipitation(in.)")
pre.set_ylim([-100, 1100])
pre.set_ylabel("Occurrence")
plt.show()
fig, scat = plt.subplots()
scat.scatter(average_temp,average_dew)
scat.set_title("Dew Point Compared To Temperature")
scat.set_xlabel("Temperature")
scat.set_ylabel("Dew Point")
plt.show()
x_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mean_temp = []

e= []
# i couldve found a way to loop this but syed convinced me copying and pasting this was easier
mean_temp.append(sum(month_1_avg_temp)/len(month_1_avg_temp))
mean_temp.append(sum(month_2_avg_temp)/len(month_2_avg_temp))
mean_temp.append(sum(month_3_avg_temp)/len(month_3_avg_temp))
mean_temp.append(sum(month_4_avg_temp)/len(month_4_avg_temp))
mean_temp.append(sum(month_5_avg_temp)/len(month_5_avg_temp))
mean_temp.append(sum(month_6_avg_temp)/len(month_6_avg_temp))
mean_temp.append(sum(month_7_avg_temp)/len(month_7_avg_temp))
mean_temp.append(sum(month_8_avg_temp)/len(month_8_avg_temp))
mean_temp.append(sum(month_9_avg_temp)/len(month_9_avg_temp))
mean_temp.append(sum(month_10_avg_temp)/len(month_10_avg_temp))
mean_temp.append(sum(month_11_avg_temp)/len(month_11_avg_temp))
mean_temp.append(sum(month_12_avg_temp)/len(month_12_avg_temp))
e.append((max(month_1_avg_temp)-min(month_1_avg_temp))/2)
e.append((max(month_2_avg_temp)-min(month_2_avg_temp))/2)
e.append((max(month_3_avg_temp)-min(month_3_avg_temp))/2)
e.append((max(month_4_avg_temp)-min(month_4_avg_temp))/2)
e.append((max(month_5_avg_temp)-min(month_5_avg_temp))/2)
e.append((max(month_6_avg_temp)-min(month_6_avg_temp))/2)
e.append((max(month_7_avg_temp)-min(month_7_avg_temp))/2)
e.append((max(month_8_avg_temp)-min(month_8_avg_temp))/2)
e.append((max(month_9_avg_temp)-min(month_9_avg_temp))/2)
e.append((max(month_10_avg_temp)-min(month_10_avg_temp))/2)
e.append((max(month_11_avg_temp)-min(month_11_avg_temp))/2)
e.append((max(month_12_avg_temp)-min(month_12_avg_temp))/2)
fig, ax = plt.subplots()
ax.bar(x_pos, mean_temp, yerr=e, align='center', alpha=0.5, ecolor='black')  # stack overflow
ax.set_ylabel("Average Temperature")  # label tool labels the graph to what i say
ax.set_xlabel("Months")
ax.set_title("Temperatures per Months")
plt.show()   # plots the graph
















