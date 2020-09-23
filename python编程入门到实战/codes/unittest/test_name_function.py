import unittest

from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_list_reverse(self):
        pass
        
    def test_func3(self):
        print('hello world')
unittest.main()
