#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:41:25 2020

@author: mjmacarty
"""

from user import User

class SuperUser(User):
    
    def __init__(self, username, password, email, birthday, role):
        self.role = role
        super().__init__(username, password, email, birthday)

        
    def __str__(self):
        return super().__str__() + f"\nRole: {self.role}"
    