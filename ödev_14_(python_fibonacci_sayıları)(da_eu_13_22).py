# -*- coding: utf-8 -*-
"""Ödev-14 (Python - Fibonacci Sayıları)(DA EU 13/22)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YWZMfttksJcAGwzrhw__5_QaWEbShg-R
"""

sayı=int(input("bir sayı giriniz :")) # Burada bir sayı girilmesi istenmektedir 
a = 0
b = 1     # Bu konuda kendinden önceki sayıyı toplaması için yapılmıştır.
for i in range(sayı):
  c=a
  a=a+b
  b=c
  print(b, end=",")













