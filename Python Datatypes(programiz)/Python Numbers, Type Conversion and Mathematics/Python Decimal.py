import decimal

# Output: 0.1
print(0.1)

# Output: Decimal('0.1000000000000000055511151231257827021181583404541015625')
print(decimal.Decimal(0.1))








#This module is used when we want to carry out decimal calculations like we learned in school.

#It also preserves significance.
# We know 25.50 kg is more accurate than 25.5 kg as it has two significant decimal places compared to one.



from decimal import Decimal as D
# Output: Decimal('3.3')
print(D('1.1') + D('2.2'))

# Output: Decimal('3.000')
print(D('1.2') * D('2.50'))