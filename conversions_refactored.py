#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""converts temperature and distances"""

from __future__ import division


class ConversionNotPossible(Exception):
    """can not convert exception"""
    pass

def convert(fromUnit, toUnit, value):
    """convert from one unit to another"""
    from_entered = fromUnit.lower()
    to_entered = toUnit.lower()
    temps = ['celcius', 'kelvin', 'farhenheit']
    distance = ['yards', 'meters', 'miles']

    if from_entered == to_entered:
        return value

    if from_entered and to_entered in temps:
        if from_entered == 'celcius':
            if to_entered == 'kelvin':
                result = value + 273.15
                kelvin = float("{0:.2f}".format(result))
                return kelvin
            if to_entered == 'farhenheit':
                result = (value) * (9/5) + 32
                farhenheit = float("{0:.2f}".format(result))
                return farhenheit

        if from_entered == 'farhenheit':
            if to_entered == 'celcius':
                result = (value - 32) * (5/9)
                celcius = float("{0:.2f}".format(result))
                return celcius
            if to_entered == 'kelvin':
                result = (value + 459.67) * (5/9)
                kelvin = float("{0:.2f}".format(result))
                return kelvin

        if from_entered == 'kelvin':
            if to_entered == 'farhenheit':
                result = value * (9/5) - 459.67
                farhenheit = float("{0:.2f}".format(result))
                return farhenheit
            if to_entered == 'celcius':
                result = value - 273.15
                celcius = float("{0:.2f}".format(result))
                return celcius

        else:
            raise ConversionNotPossible("Cannot convert {} to {}.".format(fromUnit, toUnit))

    if from_entered and to_entered in distance:
        if from_entered == 'yards':
            if to_entered == 'meters':
                results = value * .9144
                meters = float("{0:.2f}".format(results))
                return meters
            if to_entered == 'miles':
                results = value / 1760.0
                miles = float("{0:.2f}".format(results))
                return miles

        if from_entered == 'meters':
            if to_entered == 'yards':
                results = value / .9144
                yards = float("{0:.2f}".format(results))
                return yards
            if to_entered == 'miles':
                results = value / 1609.34
                miles = float("{0:.2f}".format(results))
                return miles

        if from_entered == 'miles':
            if to_entered == 'yards':
                results = value * 1760.0
                yards = float("{0:.2f}".format(results))
                return yards
            if to_entered == 'meters':
                results = value * 1609.344
                meters = float("{0:.2f}".format(results))
                return meters
        else:
            raise ConversionNotPossible("Cannot convert {} to {}.".format(fromUnit, toUnit))
