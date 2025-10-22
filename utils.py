def decode(lists: list): # from bytes to numbers
    result = []
    for i in range(len(lists)):
        if (lists[i] != 0):
            result.append(lists[i] * (i + 1))

    return result


class Sets:
    def __init__(self, lists):
        self.lists = sorted(lists)
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > len(self.lists):
            raise StopIteration
        else:
            item = self.lists[self.index]
            self.index += 1
            return item
        
    U = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # universum set
    U_bite = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # universum set in bites

    def bite_scale(self):
        bite_scale = []
        j = 0 # iter for universum set
        while j < len(Sets.U):
            if (self.index < len(self.lists)):
                if Sets.U[j] == self.lists[self.index]:
                    bite_scale.append(1)
                    self.index += 1
                    j += 1
                else:
                    bite_scale.append(0)
                    j += 1
            else:
                bite_scale.append(0)
                j += 1

        

        # print(f'bite scale of A = {self.lists} is {bite_scale}')
        return bite_scale 
    
    def union(self, other):
        bite_A = self.bite_scale()
        bite_B = other.bite_scale()

        result = [0] * len(bite_B)

        for i in range(len(bite_B)):
            if (bite_A[i] == 0 and bite_B[i] == 0):
                result[i] = 0
            else:
                result[i] = 1

        print(f'result of union A = {self.lists} and B = {other.lists} is {decode(result)}')
        return
    
    def intersect(self, other):
        bite_A = self.bite_scale()
        bite_B = other.bite_scale()

        result = [0] * len(bite_B)
        for i in range(len(bite_B)):
            if (bite_A[i] == 1 and bite_B[i] == 1):
                result[i] = 1
            else: 
                result[i] = 0

        is_empty = True
        for bit in result:
            if bit == 1:
                is_empty = False
                break
        if is_empty:
            print(f'result of intersect A = {self.lists} and B = {other.lists} is empty')
            return
        else:
            print(f'result of intersect A = {self.lists} and B = {other.lists} is {decode(result)}')
            return

    def substract(self, other):
        bite_A = self.bite_scale()
        bite_B = other.bite_scale()

        result = [0] * len(bite_A)
        for i in range(len(bite_A)):
            if bite_B[i] == 1:
                result[i] = 0
            else:
                result[i] = bite_A[i]
        
            
            
        is_empty = True
        for bit in result:
            if bit == 1:
                is_empty = False
                break
        if is_empty:
            print(f'result of intersect A = {self.lists} and B = {other.lists} is empty')
            return
        else:
            print(f'result of intersect A = {self.lists} and B = {other.lists} is {decode(result)}')
            return
        
    def addition(self):
        bite_A = self.bite_scale()
        result = [0] * len(bite_A)

        for i in range(len(bite_A)):
            if bite_A[i] == 0:
                result[i] = 1

        is_empty = True
        for bit in result:
            if bit == 1:
                is_empty = False
                break
        if is_empty:
            print(f'A is universum')
            return
        else:
            print(f'result of addition A = {self.lists} is {decode(result)}')
            return
        



                
                
