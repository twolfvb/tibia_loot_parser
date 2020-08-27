from django.test import TestCase
import os
from loot_parser import parser

# Create your tests here.
#from myapp.models import Animal

class ParserTestCase(TestCase):
    def setUp(self):
        example1_filename = "example1.txt"
        self.example1_file = open(os.path.join(os.path.dirname(__file__), example1_filename))

    def test_parse_original_loot(self):
        """Animals that can speak are correctly identified"""
        highest_net_worth = "Zeta the Bird"
        transfer1 = (121145, "Don Hams")
        transfer2 = (94096, "Gusa Class")
        transfer3 = (61251, "Pescao Apanao")
        answer = parser.parse_hunt_data(self.example1_file.read())
        self.assertEqual(answer, (highest_net_worth, transfer1, transfer2, transfer3))
