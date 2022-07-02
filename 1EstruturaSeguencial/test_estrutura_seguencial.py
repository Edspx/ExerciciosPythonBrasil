import unittest
import random
from faker import Faker 

from ex1_5 import converter_metros_para_centimetro
from ex1_3 import soma
from ex1_4 import media




class TestStringMethods(unittest.TestCase):

    def test_mc(self):
        '''Exercicio 1.5 de conversão de Metros para Centrimetros'''
        self.assertEqual(converter_metros_para_centimetro(1), 100)

    def test_soma(self):
        '''3.Faça um Programa que peça dois números e imprima a soma.'''
        x = random.randint(1,100)
        y = random.randint(1,100)
        r = x + y
        self.assertEqual(soma(x, y), r)

    def test_media(self):
        '''4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''
        a = random.randint(1,100)
        b = random.randint(1,100)
        c = random.randint(1,100)
        d = random.randint(1,100)
        r = (a+b+c+d)/4
        self.assertEqual(media(a,b,c,d),  r)


