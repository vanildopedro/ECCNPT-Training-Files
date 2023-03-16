#####Operators

5 > 5
5 < 5
7 => 5
7 =< 5
7 == 7
7 != 8

AND & OR

test_and = (7 > 5) and (7 > 5) # this will be TRUE
test_and = (7 > 5) and (5 > 7) # this will be FALSE

test_or = (7 > 5) or (5 > 7)# this will be TRUE
test_or = (5 > 7) or (7 > 5)# this will be TRUE
test_or = (5 > 7) or (7 < 5)# this will be FALSE

test_not = not True
test_not = not False
