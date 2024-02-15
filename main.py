from colorama import Fore

string = "...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t" 
'''
You need change the variable "string" if you have other secuences of dead ants
'''

counter_ants_dead = 0
length_string = len(string)



for i in range(0, length_string,1):
   if string[i] == "t":
       
       if string[i-1] != "n":
           counter_ants_dead = counter_ants_dead + 1
           
       
print  (Fore.RED + "The number of ants that died is: " , counter_ants_dead)