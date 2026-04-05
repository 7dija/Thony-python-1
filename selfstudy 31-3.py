total_width = 100
tail_width = 5

number_of_tails = total_width//tail_width
if number_of_tails%2 == 0:
    number_of_tails -=1


else:
 number_of_tails = number_of_tails
print("number of tails= " ,number_of_tails )
gap = (total_width - (number_of_tails * tail_width))/2
print(gap)
