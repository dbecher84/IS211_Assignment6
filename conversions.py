#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""convert celcius to kelvin and fahrenheit"""

from __future__ import division

def convertcelsiustokelvin(degree):
    """converts celcius to kelvin"""
    result = degree + 273.15
    kelvin = float("{0:.2f}".format(result))
    return kelvin


def convertcelsiustofarhenheit(degree):
    """converts celsius to farhenheit"""
    result = (degree) * (9/5) + 32
    farhenheit = float("{0:.2f}".format(result))
    return farhenheit


def convertfarhenheittocelcius(degree):
    """converts farhenheit to celcius"""
    result = (degree - 32) * (5/9)
    celcius = float("{0:.2f}".format(result))
    return celcius


def convertfarhenheittokelvin(degree):
    """converts farhenheit to kelvin"""
    result = (degree + 459.67) * (5/9)
    kelvin = float("{0:.2f}".format(result))
    return kelvin


def convertkelvintofarhenheit(degree):
    """converts kelvin to farhenheit"""
    result = degree * (9/5) - 459.67
    farhenheit = float("{0:.2f}".format(result))
    return farhenheit


def convertkelvintocelcius(degree):
    """converts kelvin to celcius"""
    result = degree - 273.15
    celcius = float("{0:.2f}".format(result))
    return celcius
