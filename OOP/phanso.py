# Tạo class Fraction (phân số)

# Hàm khởi tạo nhận 2 giá trị nr (tử số) và dr (mẫu số)
# Nếu dr âm, chuyển dấu cho nr (VD: 1/-2 => -1/2)
# Triển khai phương thức phù hợp để in ra phân số (VD: print(fr) => -1/2)
# Viết hàm hcf tìm ước chung lớn nhất của nr và dr
# Thêm phương thức reduce rút gọn phân số (gọi trong __init__)
# Nếu nr == 0, chỉ in ra 0
# Nếu dr == 0, raise ZeroDevisonError
# Nếu dr == 1, chỉ in ra nr
# Triển khai các phương thức phù hợp cho phép +-*/ với 2 Fraction hoặc 1 Fraction với 1 số (int hoặc float), kết quả trả về 1 Fraction mới

class Fraction:
    def __init__(self, nr, dr) -> None:
        self.set_nr_dr(nr, dr)
        re = self.doReduce(nr, dr)
        self.set_nr_dr(re[0], re[1])

    def set_nr_dr(self, nr, dr):
        self.set_nr(nr)
        self.set_dr(dr)

    def set_nr(self, nr):
        self._nr = nr

    def get_nr(self):
        return self._nr

    def set_dr(self, dr):
        if dr < 0:
            self.set_nr(self.get_nr()-2*self.get_nr())
        self._dr = abs(dr)

    def get_dr(self):
        return self._dr

    def hcfnaive(self, a, b):
        if(b == 0):
            return a
        else:
            return self.hcfnaive(b, a % b)

    def doReduce(self, nr, dr):
        if dr == 0:
            print('ZeroDevisonError')
            return
        hcf = self.hcfnaive(nr, dr)
        return (int(nr/hcf), int(dr/hcf))

    def display(self, nr=None, dr=None):
        if nr == None or dr == None:
            nr = self._nr
            dr = self._dr
        fr = self.getFrac(nr, dr)
        if type(fr) is tuple:
            print(f'{fr[0]}/{fr[1]}')
        else:
            print(fr)

    def getFrac(self, nr=None, dr=None):
        if nr == None or dr == None:
            nr = self._nr
            dr = self._dr
        if nr == 0:
            return 0
        if dr == 1:
            return nr
        if dr == 0:
            return 'ZeroDevisonError'
        if nr % dr == 0:
            return int(nr/dr)
        return f'{nr}/{dr}'

    def add(self, number):
        if number == 0:
            return self.display()
        # 5/4 + 2 = 5/4 + 8/4
        new_nr = self._dr*number + self._nr
        self.displayResult(new_nr,self._dr,'+',number)
        # print(f'{self._nr}/{self._dr} + {number} = {new_nr}/{self._dr}')

    def sub(self, number):
        if number == 0:
            return self.display()
        new_nr = self._dr*number - self._nr
        self.displayResult(new_nr,self._dr,'-',number)
        # print(f'{self._nr}/{self._dr} - {number} = {new_nr}/{self._dr}')

    def multi(self, number):
        new_nr = number * self._nr
        rd = self.doReduce(new_nr, self._dr)
        self.displayResult(rd[0],rd[1],'*',number)

    def div(self, number):
        if number == 0:
            return 'ZeroDevisonError'
        new_dr = number * self._dr
        rd = self.doReduce(self._nr, new_dr)
        self.displayResult(rd[0],rd[1],'/',number)

    def displayResult(self,nr,dr,operator,number):
        resultFrac = self.getFrac(nr, dr)
        resultStr = resultFrac
        if type(resultFrac) is tuple:
            resultStr = f'{fr[0]}{operator}{fr[1]}'
        print(f'{self.getFrac(self._nr,self._dr)} {operator} {number} = {resultStr}')
        pass

# run
fr = Fraction(-3, 4)
# fr.display()
fr.add(1)
# fr.multi(4)
# fr.div(4)
# print()
