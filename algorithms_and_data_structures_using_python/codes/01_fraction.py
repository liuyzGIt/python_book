class Fraction:
    
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        
    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
        
    def gcd(self):
        m = self.num
        n = self.den
        while m % n != 0:
            m, n = n, m % n
        return n
        
    def show(self):
        print(self.num, '/', self.den)
    
    def __str__(self):
        return str(self.num) + ' / ' + str(self.den)
        
    def __eq__(self, other):
        return self.num * other.den == self.den * other.num
        
    
if __name__ == "__main__":
    f1 = Fraction(3, 5)
    f2 = Fraction(35, 45)
    f3 = Fraction(3, 5)
    print(f1 == f3)
    
    # print(f2.gcd())
