#prime checker function 
number = 29
factor_counter = 0

for i in range(1, number+1):
    if number % i == 0:
        factor_counter += 1
    
if factor_counter == 2:
    print('Prime')
else:
    print('Not Prime')