#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""test for the conversion module"""

import unittest
import conversions


class Testknowndegree(unittest.TestCase):
    """test the conversions file"""
    knownC_F_K = ((0.0, 32.0, 273.15), (100.0, 212.0, 373.15),
                  (-200.0, -328.0, 73.15), (500.0, 932.0, 773.15),
                  (20.0, 68.0, 293.15))

    def testc_to_f(self):
        """test celcius to farhenheit"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            result = conversions.convertcelsiustofarhenheit(deg_C)
            self.assertEqual(deg_F, result)

    def testc_to_k(self):
        """test celcius to kelvin"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            result = conversions.convertcelsiustokelvin(deg_C)
            self.assertEqual(deg_K, result)

    def testf_to_c(self):
        """test farhenheit to celcius"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            result = conversions.convertfarhenheittocelcius(deg_F)
            self.assertEqual(deg_C, result)

    def testf_to_k(self):
        """test farhenheit to kelvin"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            result = conversions.convertfarhenheittokelvin(deg_F)
            self.assertEqual(deg_K, result)

    def testk_to_f(self):
        """test kelvin to farhenheit"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            result = conversions.convertkelvintofarhenheit(deg_K)
            self.assertEqual(deg_F, result)

    def testk_to_c(self):
        """test kelvin to celcius"""
        for deg_C, deg_F, deg_K in self.knownC_F_K:
            result = conversions.convertkelvintocelcius(deg_K)
            self.assertEqual(deg_C, result)

if __name__ == "__main__":
    unittest.main()
