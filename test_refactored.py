#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""test for the conversion_refactored module"""

import unittest
import conversions_refactored



class Testconversion(unittest.TestCase):
    """tests the conversion_refactored file"""
    knownC_F_K = ((0.0, 32.0, 273.15), (100.0, 212.0, 373.15),
                  (-200.0, -328.0, 73.15), (500.0, 932.0, 773.15),
                  (20.0, 68.0, 293.15))
    knownY_ME_MI = ((2640.0, 2414.02, 1.5), (35200.0, 32186.88, 20.0),
                    (8800.0, 8046.72, 5.0), (440.0, 402.34,.25),
                    (1478.4, 1351.85, .84))

    def testk_to_c(self):
        """test kelvin to celcius"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            results = conversions_refactored.convert('kelvin', 'celcius', deg_K)
            self.assertEqual(deg_C, results)
    def testk_to_f(self):
        """test kelvin to farhenheit"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            results = conversions_refactored.convert('kelvin', 'farhenheit', deg_K)
            self.assertEqual(deg_F, results)
    def testf_to_k(self):
        """test farhenheit to kelvin"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            results = conversions_refactored.convert('farhenheit', 'kelvin', deg_F)
            self.assertEqual(deg_K, results)
    def testf_to_c(self):
        """test farhenheit to celcius"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            results = conversions_refactored.convert('farhenheit', 'celcius', deg_F)
            self.assertEqual(deg_C, results)
    def testc_to_k(self):
        """test celsius to kelvin"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            results = conversions_refactored.convert('celcius', 'kelvin', deg_C)
            self.assertEqual(deg_K, results)
    def testc_to_f(self):
        """test celcius to farhenhiet"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            results = conversions_refactored.convert('celcius', 'farhenheit', deg_C)
            self.assertEqual(deg_F, results)

    def testsameunit(self):
        """test is same unit is entered for both inputs"""
        for item in ['kelvin', 'celcius', 'farhenheit', 'yards', 'miles', 'meters']:
            results = conversions_refactored.convert(item, item, 213.0)
            self.assertEqual(213.0, results)

    def testnotpossble(self):
        """test what happens if conversion not possible"""
        for item in (('miles', 'kelvin'), ('farhenheit', 'meters'), ('celcius', 'yards'),
                     ('kelvin', 'yards'), ('miles', 'celcius')):
            self.assertRaises(conversions_refactored.ConversionNotPossible,
                              conversions_refactored.convert, item[0], item[1], 200.00)

#mi=miles me=meters y=yards

    def testy_to_me(self):
        """test yards to meters"""
        for di_Y, di_ME, di_MI in self.knownY_ME_MI:
            results = conversions_refactored.convert('yards', 'meters', di_Y)
            self.assertEqual(di_ME, results)
    def testy_to_mi(self):
        """test yards to miles"""
        for di_Y, di_ME, di_MI in self.knownY_ME_MI:
            results = conversions_refactored.convert('yards', 'miles', di_Y)
            self.assertEqual(di_MI, results)
    def testme_to_y(self):
        """test meters to yards"""
        for di_Y, di_ME, di_MI in self.knownY_ME_MI:
            results = conversions_refactored.convert('meters', 'yards', di_ME)
            self.assertEqual(di_Y, results)
    def testme_to_mi(self):
        """test meter to miles"""
        for di_Y, di_ME, di_MI in self.knownY_ME_MI:
            results = conversions_refactored.convert('meters', 'miles', di_ME)
            self.assertEqual(di_MI, results)
    def testmi_to_y(self):
        """test miles to yards"""
        for di_Y, di_ME, di_MI in self.knownY_ME_MI:
            results = conversions_refactored.convert('miles', 'yards', di_MI)
            self.assertEqual(di_Y, results)
    def testmi_to_me(self):
        """ test miles to meters"""
        for di_Y, di_ME, di_MI in self.knownY_ME_MI:
            results = conversions_refactored.convert('miles', 'meters', di_MI)
            self.assertEqual(di_ME, results)

if __name__ == "__main__":
    unittest.main()
