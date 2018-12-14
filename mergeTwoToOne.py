import unittest

def merge_arrays(arr1, arr2):
    return sorted((set(arr1 + arr2)))


print (merge_arrays([6, 2, 3, 4], [5,5,5, 6, 7, 8]))


class testFucn(unittest.TestCase):

    def test_if_equal(self):
        self.assertEquals(merge_arrays([3,6,7,8],[3,4,5,7]),[3,4,5,6,7,8])
        self.assertEquals(merge_arrays([0,4,10,8],[7,4,30,7]),[0,4,7,8,10,30])



if __name__ == '__main__':
    unittest.main()
