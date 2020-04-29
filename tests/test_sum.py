from code.sum import sum

assert sum(2, 3) == 5, 'Should be 5'

assert sum(2, 3, 8) == 13, 'Should be 13'

assert sum(2, -1) == 1, 'Should be 1'

assert sum(2, 2, 2, 2, 2) == 10, 'Should be 10'

assert sum(1) == 1, 'Should be 1'