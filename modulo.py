import numpy as np
class ModuloField:
    def __init__(self, value) -> None:
        assert (isinstance(value, int)), 'Value should strictly be an int'
        np.set_printoptions(threshold=np.inf)
        self.value = value
        

    def computeMultiplicationTable(self):
        mod = np.vectorize(lambda x: x % self.value)
        keys = np.arange(0,self.value)
        result =  mod(np.outer(keys,keys))
        r,c = result.shape
        resultArray = np.ones((r+1,c+1),dtype=int)
        resultArray[1:,1:] = result
        resultArray[1:, 0] = keys
        resultArray[0, 1:] = keys
        resultArray[0,0] = -1
        

        return resultArray

    def computeAdditionTable(self):
        keys = np.arange(0,self.value)
        resultArray = np.ones((keys.shape[0]+1,)*2, dtype=int)
        resultArray[1:, 0] = keys
        resultArray[0, 1:] = keys
        resultArray[0,0] = -1


        for i in range(keys.shape[0]):
            for j in range(keys.shape[0]):
                resultArray[i+1, j+1] = (i + j) % self.value

        return resultArray





if __name__ == '__main__':
    print(ModuloField(6).computeMultiplicationTable())