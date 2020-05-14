#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:12:41 2020

@author: mjmacarty
"""

from superuser import SuperUser


superuser = SuperUser("jon", "password", "jon@some.com", "12/24/1999", "admin")

print(superuser)
print()
print(repr(superuser))