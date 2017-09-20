#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(ord('A'))

print(ord('中'))

print(chr(66))

print('\u4e2d\u6587')



print(b'ABC')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))



print('hellow, %s'%'word')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))