import unittest
import various_excercises as vx

class VariousExcercisesTester(unittest.TestCase):

    def check_sorting(self, sorting_function):
        self.assertListEqual(sorting_function([1, 8, 4, 5, 3, 5, 2]), [1, 2, 3, 4, 5, 5, 8])
        self.assertListEqual(sorting_function([1,2,2,1]), [1, 1, 2, 2])
        self.assertListEqual(sorting_function([0]), [0])
        self.assertListEqual(sorting_function([5,3,3]), [3, 3, 5])
    
    def test_insertion_sort(self):
        self.check_sorting(vx.insertion_sort) 

    def test_quick_sort(self):
        self.check_sorting(vx.quick_sort) 

    def test_selection_sort(self):
        self.check_sorting(vx.selection_sort) 

    def test_bucket_sort(self):
        self.check_sorting(vx.bucket_sort) 

    def test_merge_sort(self):
        self.check_sorting(vx.merge_sort)

    def test_add_vectors(self):
        self.assertListEqual(vx.add_vectors([1,2,3,4,5,6], [7,8]), [8, 10, 10, 12, 12, 14])

    def test_prime_true(self):
        self.assertTrue(vx.is_prime(13))

    def test_prime_false(self):
        self.assertFalse(vx.is_prime(46))

    def test_erasthotenes_sieve(self):
        self.assertListEqual(vx.erasthotenes_sieve(36), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

    def test_primes_count(self):
        self.assertEqual(vx.primes_count(12, 31), 6)

    def test_primes_count_zero(self):
        self.assertEqual(vx.primes_count(14, 16), 0)

    def test_find_least(self):
        result = vx.find_least_elements([1, 8, 4, 5, 3, 5, 2], 3)
        self.assertTrue(set(result) == {1, 2, 3})

    def test_binary_search_true(self):
        self.assertTrue(vx.binary_search(5, [1, 1, 2, 3, 4, 5, 5, 8]))

    def test_binary_search_false(self):
        self.assertFalse(vx.binary_search(6, [1, 1, 2, 3, 4, 5, 5, 8]))

    def test_binary_search_false_outside(self):
        self.assertFalse(vx.binary_search(11, [1, 1, 2, 3, 4, 5, 5, 8]))

    def test_union(self):
        self.assertListEqual(vx.union([1, 3, 4, 5, 8, 9], [0, 5, 6, 7, 9, 11, 12]), [0, 1, 3, 4, 5, 6, 7, 8, 9, 11, 12])

    def test_intersection(self):
        self.assertListEqual(vx.intersection([1, 3, 4, 5, 8, 9], [0, 5, 6, 7, 9, 11, 12]), [5, 9])

    def test_intersection_empty(self):
        self.assertListEqual(vx.intersection([1, 3, 4, 5, 8, 9], [0, 11, 12]), [])

    def test_split(self):
        x = [3, 5, 11, 2, 2, 5, 8, 9, 5, 9, 0, 12]        
        vx.split(8, x)
        max_index = max([x.index(element) for element in x if element <= 8])
        self.assertTrue( min(x[max_index + 1:]) > 8)
    
    def test_k_quick_sort(self):        
        self.assertEqual(vx.k_quick_sort(4, [3, 5, 11, 2, 2, 5, 8, 9, 5, 9, 0, 12]), 3)

    def test_partial_quick_sort(self):  
        x = list(range(10, -1, -2)) + list(range(10))
        res = vx.partial_quick_sort(5, x)        
        self.assertListEqual(res[:5], [0, 0, 1, 2, 2])

    def test_bridge_proble(self):
        self.assertTrue(vx.BridgeProblemSolution().solve() < 19) 

    def test_fibonacci(self):
        self.assertEqual(vx.fibonacci(6), 8)

if __name__ == '__main__':
    unittest.main()

