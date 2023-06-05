class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return (self.x)**2 +(self.y)**2 + (self.z)**2
    

obj1 = Point(1, 3, 5)
result = obj1.sqSum()
print('Sample Input: 1, 3, 5')
print('Sample Output:', result)