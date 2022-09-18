
# calculating fictorial
fic = 1
for i in range(1,100):
    if (i == 10 or i ==100 or i == 2 or i == 5 or i == 20 or i == 50):
        pass
    else:
        fic = fic*i


text_fact = str(fic)

# Initialize empty list for every letter of factorial string 
summ = []
for letter in text_fact:
    summ.append(int(letter)) # append each number to array

# print sum of array (numbers)
print(sum(summ))