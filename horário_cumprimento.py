#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:45:07 2021

@author: Vagner Luis Zanin
"""
#solicitando o horário
hora = input('Digite o horário no seguinte formato. (hh:mm): ')

#separando a string 'hora' em ma lista de dois termos onde h = 'hh' e m = 'mm'.
x = hora.split(':')

h = x[0]
m = x[1]

'''
verificar se o horário digitado está no formato correto, os termos 'h' e 'm'
foram convertidos para inteiros assim a relação de desigualdade funcionará.
'''
if (int(h) < 0 or int(h) > 24) or (int(m) < 0 or int(m) > 59):
    print(f'O horário digitado {hora} está em formato incorreto.')

#verificando a partir da hora 'h' se é de manhã, tarde ou noite.
else:
    if int(h) >= 0 and int(h) <= 11:
        print('Bom dia')
    elif int(h) >= 12 and int(h) <=17:
        print('Boa tarde')
    else:
        print('Boa noite')
        





