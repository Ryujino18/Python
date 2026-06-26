# a ="Ryujino"
# a ='Ryujino'
# a = '''Ryujino'''

name = "Ryujino"
nameshort = name[0] #index for the R-0 , y-1 , u-2, j-3, i-4, n-5, o-6
print (nameshort)

#indicing

name_sl = name[0:3] # o- first index is included and 3- last index is excluded
print(name_sl) # Ryu

name_rsl = name[-3:-2] # # neagtive slicing : where R= -7, .......... o = -1
print (name_rsl) # i 
print (name[4:5]) # i
print (name[1:5]) #yuji
print(name[1:]) #yujino
print(name[:]) #Ryujino



#skip 
num = "0123456789"
print (num[1:5:2]) #13