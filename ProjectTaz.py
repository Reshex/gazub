def check_id_valid(id_number):
    sum2 = 0
    for num in str(id_number)[1::2]:
        k = int(num) * 2
        if int(k) > 9:
            sum = 0
            for digit in str(k):
                sum += int(digit)
            sum2 += sum
        else:
            sum2 += k
        k = 0
    for num1 in str(id_number)[::2]:
        num1 * 1
        sum2 += int(num1)
    if sum2 % 10 == 0:
        return (True)
    else:
        return (False)


class IDIterator:
    def __init__(self, id):
        self.id = id

    def __iter__(self):
        return self

    def __next__(self):
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
    gen = (num for num in range(id, 999999999))
    for g in gen:
        if check_id_valid(g):
            yield g


if __name__ == "__main__":
    que = input("gen/it? ")
    if que == "gen":
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

    if que == "it":
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
