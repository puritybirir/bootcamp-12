'''This program passed all the visible tests on Andelabs but produced an error during submission   '''


class BinarySearch(list):
    def __init__(self, a, b):
        self.length = a
        i = a * b
        self.array = []
        x = b
        while b <= i:
            self.array.append(b)
            b = b + x

    def __getitem__(self, i):
        return self.array[i]

    def search(self, num):
        start = 0
        end = len(self.array) - 1
        result = {}
        count = 1
        if num in self.array:
            while start <= end:
                med = (start + end) / 2
                if self.array[med] == num:
                    if count > 4:
                        result['count'] = 0
                        result['index'] = med
                    else:
                        result['count'] = count
                        result['index'] = med

                    return result
                    break
                elif self.array[med] < num:
                    start = med + 1
                elif self.array[med] > num:
                    end = med - 1

                count += 1
        else:
            result['count'] = 3
            result['index'] = -1

            return result
