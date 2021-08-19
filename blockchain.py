# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:58:57 2021

@author: levas
"""

import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create__block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
         block = {'index': len(self.chain) + 1, 
                  'timestamp': str(datetime.datetime.now()),
                  'proof': proof,
                  'previous_hash': previous_hash}
         self.chain.append(block)
         return block