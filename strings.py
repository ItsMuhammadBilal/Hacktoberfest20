#         012345678901234
parrot = "Norwegian Blue"

print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

# print()
# # negative Indexing
# #          -14            -1
# #parrot = "Norwegian Blue"
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

# print()

# print(parrot[3 - 14])
# print(parrot[4 - 14])
# print(parrot[9 - 14])
# print(parrot[3 - 14])
# print(parrot[6 - 14])
# print(parrot[8 - 14])


# print(parrot[0:6]) # Norweg
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])
# print(parrot[10:14])
# print(parrot[10:])
# print(parrot[:6])
# print(parrot[6:])
# print(parrot[:6] + parrot[6:])
# print(parrot[:])
#          01234567890123456789012345
# letters = "abcdefghijklmnopqrstuvwxyz"

# print(letters[16:20])
# print(letters[0:5])
# negative_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(negative_letters[-26:-21])







#print(len(negative_letters))

#step slicing

print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) # Nw

number = "9,223:372.036;954.775,839"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
