# an aggie does not lie cheat or steal, nor tolerate those who do
# i did not receive any unathorized aid on this assignment
# daniel lohn      427004202     section 510

# part A


def dimensions():

    import matplotlib
    length = float(input('what is the length of the box?'))
    width = float(input('what is the width of the box'))
    height = float(input('what is the height of the box?'))
    radius = float(input('what is the radius of the hole?'))
    if radius <= width/2 and length /2:
        volume = (length * width * height) - (pi * (radius**2) * height)
        print(volume)
    if radius >= width/2 and length/2:
        print('the hole is too big')


# part B
facility_name = ['facility1', 'facility2', 'facility3', 'facility4']
maintenance_cost = [300, 500, 700, 400]
revenue = [900, 5000, 200, 100]
weakest_facility = []


def facility_profitability(facilityn, maintenance, rev, weakest):
    counter = 1
    while counter <= len(maintenance):
        facility = rev[counter - 1] - maintenance[counter - 1]
        weakest.append(facility)
        counter = counter + 1
    minimum_value = min(weakest)
    position = weakest.index(min(weakest))

    print(facilityn[position], 'has the lowest revenue at', minimum_value, 'dollars')
    return


facility_profitability(facility_name, maintenance_cost, revenue, weakest_facility)

# part C

# c)	Write a function that takes as input a person’s name, city, state, zip code, and address, where the address is
# either one string (one line) or two strings (two lines), and prints the person’s information like a mailing label.
#  Show that the routine works regardless of whether it is called with one address line or two address lines.
def address():

    name = input('what is your name?')
    city = input('what is your city?')
    state = input("what is your state?")
    zip = input('what is your zip code?')
    address1 = input('what is your address?')
    address2 = input('what is your secondary address?(enter none if no secondary address)')
    if address2 == 'none':
        print('   ', name, '\n', address1, '\n', city+str(','), state+str(','), zip)
    if address2 != 'none':
        print('   ', name, '\n', address1, '\n', address2, '\n', city+str(','), state+str(','), zip)
    return
address()

# part D
import csv

name_of_file = input('Enter name of file: ')
csv_t = name_of_file + '.csv'


def file_converter(csvi):

    tabbed = name_of_file + '.tsv'
    with open(csvi, 'r') as my_file, open(tabbed, 'w') as other_file:
        for j in my_file:
            reader = my_file.readline()
            tsvout = csv.writer(my_file, delimiter='\t')
            for i in reader:
                other_file.write(i)
            other_file.write('\n')
    return


file_converter(csv_t)

# part E
#	Write a single function that takes in a list and returns the minimum, mean, and maximum value from the list.

def list_organizer():

    input_numbers = input("enter numbers separated by commas ie 2,5,8,9,10")
    their_list = list(map(float, input_numbers.split(',')))
    print('your minimum number is', min(their_list))
    print('your max number is', max(their_list))
    print('your mean number is', sum(their_list)/len(their_list))
    return


list_organizer()

# Part F

# do you want me to ask the user for an input of times and distances? I can do that but the
# problem, to me, didn't specify that so i did not do that.
times = []
distance = []
velocity_list = []


def distance_travelled(times, distance, velocity_list):

    while True:
        time_input = input("what is the time? input stop if done")
        if time_input == 'stop':
            break
        times.append(float(time_input))
        distance_input = input('what is the distance?')
        distance.append(float(distance_input))
    counter = 1
    while counter < len(times):
        velocity = (distance[counter] - distance[counter - 1]) / (times[counter] - times[counter - 1])
        velocity_list.append(velocity)
        counter = counter + 1

    print(velocity_list, ' is the velocity between your points')
    return


distance_travelled(times, distance, velocity_list)




