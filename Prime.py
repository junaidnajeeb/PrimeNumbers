__author__ = 'junaid'

import numbers
import math


class Prime:
    prime_range = 0

    def __init__(self):
        prime_range = 0

    @staticmethod
    def isPrime(input_number):
        if isinstance(input_number, numbers.Integral):

            #print 'Input is integer'

            if input_number < 2:
                return False

            # 2 is the only prime which is even
            elif input_number == 2:
                return True

            # even numbers are not prime
            elif input_number % 2 == 0:
                return False

            # No prime number greater than 5 ends in a 5
            input_number_str = str(input_number)
            if input_number_str[-1:] == 5:
                return False

            divider = 3
            limit = int(math.sqrt(input_number))
            print "limit : " + str(limit)

            while_counter = 0
            while divider <= limit:
                if input_number % divider == 0:
                    return False

                divider += 1
                while_counter += 1


        else:
            return False

        print "while_counter : " + str(while_counter)
        return True

