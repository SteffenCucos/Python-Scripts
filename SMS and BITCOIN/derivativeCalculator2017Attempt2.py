



class term():

    def __init__(self,term):
        self.term=term
        self.coef=self.coef()
        self.exponent=self.exponent()
        self.sign=self.find_sign()
        self.isNum=self.isNum()
    def find_sign(self):
        if self.term[0]=="-":
            self.sign="-1"
        else:
            self.sign="1"
    def isNum(self):
        for n in self.term:
            if n=="x":
                return True
        return False
    def coef(self):
        num=""
        if self.term[0]=="x":
            self.coef="1"
            return
        nums=self.term.split('x')[0]
        if "/" in nums:
            self.coef = float(float(nums.split("/")[0])/float(nums.split("/")[1]))
        else:
            self.coef = float(nums)
    def exponent(self):
        num=""

        if "^" not in self.term:
            self.exponent=1
            return
        exp=self.term.split("^")[-1]
        if "/" in exp:
            self.exponent = float(float(nums.split("/")[0])/float(nums.split("/")[1]))
        else:
            self.exponent=float(exp)

    def __str__(self):

        strng=""
        strng+=self.sign
        if self.coeffecient!="1":
            strng+=self.coefficient
        if not self.isNum:
            strng+="x"
        if self.coefficient !="1":
            strng+="^"
            strng+=self.coefficient
        return strng 
        











        
