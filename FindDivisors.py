
import unittest


def divisors(n):
    mylist=[]
    myFuntion=lambda (x) : n % x == 0
    for i in range(1,n+1):
        mylist.append(i)
    ans =filter(myFuntion,mylist)
    return len(ans)

#test for function
class TestDivisors(unittest.TestCase):

    def test_divisors(self):
        self.assertEquals(divisors(10),4)
        self.assertEquals(divisors(5),2)

if __name__ == '__main__':
    unittest.main()
