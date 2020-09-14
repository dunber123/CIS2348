#Rhahan Sarwar
#1818962
#Homework 5.19

serv_list = {"-": 0, "Oil change" : 35, "Tire rotation" : 19, "Car wash" : 7, "Car wax": 12}
f_service = ""
s_service = ""
total = 0

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print("")

f_service = input("Select first service:\n")
s_service = input("Select second service:\n")
print("")

print("Davy's auto shop invoice")
print("")

if(f_service == "-"):
  print("Service 1: No service")
else:
  print("Service 1: %s, $%d" % (f_service, serv_list.get(f_service)))
  
if(s_service == "-"):
  print("Service 2: No service")
else:
  print("Service 2: %s, $%d" % (s_service, serv_list.get(s_service)))

total = serv_list.get(f_service) + serv_list.get(s_service)
print("")
print("Total: $%d" % (total))