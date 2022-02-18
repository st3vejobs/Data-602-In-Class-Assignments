# Shane Hylton

# Question 1

## The original code only printed empty brackets.
## This can be remedied by removing using the index 0:5
numbers = [1,2,3,4,5]
print(numbers[0:5])

# Question 2

m = float(input("Enter Monday's sales: "))
t = float(input("Enter Tuesday's sales: "))
w = float(input("Enter Wednesday's sales: "))
r = float(input("Enter Thursday's sales: "))
f = float(input("Enter Friday's sales: "))
sat = float(input("Enter Saturday's sales: "))
sun = float(input("Enter Sunday's sales: "))

sales = [m,t,w,r,f,sat,sun]
tot_sales = 0
for i in sales:
  tot_sales += i 
  
print(f'Total sales for the week: {tot_sales}')


# Question 3

places = ['Tahiti', 'Home', 'Bed', 'Therapist', 'Montreal']
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)

# Question 4
courses = ('Herbology 101', 'Beasts 307', 'Potions 239', 'Muggle Studies 408')
rooms = {"Herbology 101" : "Greenhouse", "Beasts 307": "Forbidden Forest", "Potions 239": "Dungeons", "Muggle Studies 408": "Zoo"}
teachers = {"Herbology 101" : "Pomfrey", "Beasts 307": "Hagrid", "Potions 239": "Snape", "Muggle Studies 408": "Weasley"}
times = {"Herbology 101" : "7:30 AM", "Beasts 307": "11:00 AM", "Potions 239": "12:30 PM", "Muggle Studies 408": "2:00 PM"}
print()
print(f'Options: {courses}')
print()
course = str(input("Which course would you like to know about? "))
print()
print()
print(rooms[course])
print(teachers[course])
print(times[course])
print()

# Question 5

contacts = {"Hawking": "steve@hawk.com", "Asimov": "isaac@aol.com", "Mulder": "ibelieve@fbi.gov", "Bonds": "slugger@mlb.com", "Steve": "st3vejobs@apple.com"}

print(f'Original Contact List: {contacts}')
print()
# Lookup
print(f'Fox Mulder: {contacts["Mulder"]}')

#Add new
contacts["Steve Rogers"] = "cap@avengers.edu" 

# Change Address

contacts["Hawking"] = "posthumous_steve@hawk.com"

# Delete
del contacts["Bonds"]
print()
print(f'Final Contact List: {contacts}')
