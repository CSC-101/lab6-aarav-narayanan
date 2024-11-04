import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)




    # Part 1
    def test_selection_books(self):
        books=[data.Book(["Orwell"],"1984"),
               data.Book(["Bob Kane"],"Batman"),
               data.Book(["Rowling"],"Harry Potter")]
        result=lab6.selection_sort_nooks(books)
        expected=[data.Book(["Orwell"],"1984"),
               data.Book(["Bob Kane"],"Batman"),
               data.Book(["Rowling"],"Harry Potter")]
        self.assertEqual(result,expected)

    def test_selection_books2(self):
        books=[data.Book(["Bob Kane"],"Batman"),
               data.Book(["Stephen King"],"The Shining"),
               data.Book(["Tolkein"],"The Hobbit")]
        result=lab6.selection_sort_nooks(books)
        expected=[data.Book(["Bob Kane"],"Batman"),
                   data.Book(["Tolkein"], "The Hobbit"),
               data.Book(["Stephen King"],"The Shining")]
        self.assertEqual(result,expected)

#Part2
#Part 2
    def test_swap_case(self):
        letters="hrtsydyJ"
        result=lab6.swap_case(letters)
        expected="HRTSYDYj"
        self.assertEqual(result,expected)
    def test_swap_case2(self):
        letters="fjekf$%JFK"
        result=lab6.swap_case(letters)
        expected="FJEKF$%jfk"
        self.assertEqual(result,expected)

    # Part 3
    def test_str_translate(self):
        letters="abcdcba"
        result=lab6.str_translate(letters,"a","x")
        self.assertEqual(result, "xbcdcbx")

    def test_str_translate2(self):
        letters="whywhywhywhy"
        result=lab6.str_translate(letters,"y","e")
        self.assertEqual(result, "whewhewhewhe")

    # Part 4
    def test_histogram(self):
        words = "Here I am I am at the place"
        result = lab6.histogram(words)
        expected = {"Here": 1, "I": 2, "am": 2, "at": 1, "the": 1, "place": 1}
        self.assertEqual(result, expected)
    def test_histogram2(self):
        words = "Words are words and they are all over the place"
        result = lab6.histogram(words)
        expected = {"words": 2, "are": 2, "and": 1, "they": 1, "all": 1,"over":1, "the":1, "place": 1}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
