def arith_geo(array):
    if len(array)!=0:
        d = array[1]-array[0]
        r = array[1]/array[0]
        for n in range(1, len(array)):
            if array[n]-array[n-1]==d:
                result='Arithmetic'
            elif array[n]/array[n-1]==r:
                result='Geometric'
            else:
                result=-1

        return result
    else:
        return 0