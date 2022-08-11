def check_id_valid(id_number):
    '''Function for check validation of given ID number
    summing up all the number is ID numbers,
    if the position in ID number is odd,
    the number stays the same, 
    if the position of the number is even, we multiply the number by 2
    if the number is > than 9, we sum up the digits
    summing up everything and checking if the number given can be divided by 10
    :param base : id_number value
    :type base: int
     '''
    sum2 = 0
    # Sum of all the numbers in id number
    for num in str(id_number)[1::2]:
        # For even position in id number
        k = int(num) * 2
        # Variable for saving the number * 2
        if int(k) > 9:
            sum = 0
            # Saving the sum of digits
            for digit in str(k):
                sum += int(digit)
            sum2 += sum
            # Joining the sum of digits to the general sum
        else:
            sum2 += k
        k = 0
        # Zero the variable
    for num1 in str(id_number)[::2]:
        # For odd position in id number
        num1 * 1
        sum2 += int(num1)
    # Sum up
    if sum2 % 10 == 0:
        return (True)
    else:
        return (False)
    # Checking if sum of id numbers can be divisioned by 10


class IDIterator:
    #Class used for creating new valid ID numbers
    def __init__(self, id):
        self.id = id

    def __iter__(self):
        return self

    def __next__(self):
        # The paramaters of next value in iterator
        self.id += 1
        if self.id >= 999999999:
            raise StopIteration
        if len(input) > 9 or len(input) < 9:
            print("Invalid input")
            raise ValueError
        if check_id_valid(self.id):
            return(self.id)
        else:
            return self.__next__()


def id_generator(id):
    # Generator for replacing the Class iterator method(ID creation)
    gen = (num for num in range(id, 999999999))
    for g in gen:
        if check_id_valid(g):
            yield g


if __name__ == "__main__":
    question = input("gen/it? ").lower()
    if question == "gen":
        g = id_generator(123456782)
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))

    elif question == "it":
        input = input("Enter ID: ")
        iditer = IDIterator(int(input))
        print(next(iditer))
        print(next(iditer))
        print(next(iditer))
        print(next(iditer))
        print(next(iditer))
        print(next(iditer))
        print(next(iditer))
        print(next(iditer))
        print(next(iditer))
        print(next(iditer))
    else:
        print("Invalid input")

