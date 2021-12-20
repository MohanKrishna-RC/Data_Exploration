# import subprocess

# #now we will store the properties of the data in "data"  variable by
# #running the cmd using subprocess.check_output

# data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
# print(data)

# #now we will store the profile by converting them to list
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
# print("----------------------------------------------")
 
# #using the loop in python we are checking and prinitng the wifi passwords
# #if they are availble

# for i in profiles:
#     #checking passwords
#     results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')

#     #storing passwords after converting them to list
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

#     #printing the profiles with their passwords using try except

#     try:
#         print("{:<30}|  {:<}".format(i,results[0]))
#     except IndexError:
#         print("{:<30}|  {:<}".format(i,""))


#Commands in Ubuntu

import subprocess

#now we will store the properties of the data in "data"  variable by
#running the cmd using subprocess.check_output
path = "/etc/NetworkManager/system-connections/"
data = subprocess.check_output(['ls',path]).decode('utf-8').split('\n')
# print(data)

#now we will store the profile by converting them to list
profiles = [i.split(" ") for i in data]
print(profiles)
# print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
# print("----------------------------------------------")