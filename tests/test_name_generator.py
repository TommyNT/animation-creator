import unittest
from media.name_generator import generate_name
import re

class TestNameGenerator(unittest.TestCase):

	def test_generation_of_unique_name():
		n1 = generate_name('foo.jpg')
		n2 = generate_name('foo.jpg')
		regexp = re.compile(r'^uploads\/[0-9a-f-]{36}\/foo\.jpg$')
		
		assert n1 != n2
		assert regexp.search(n1)
