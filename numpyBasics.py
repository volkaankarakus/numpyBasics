# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:36:48 2021

@author: VolkanKarakuş
"""
#%%
import numpy as np

array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(array.shape)

a=array.reshape(3,5)
print('shape :',a.shape)
print('dimension :',a.ndim)
print('data type :',a.dtype)
print('size :',a.size)
print('type :',type(a))

array1=np.array([[1,2,3,4],[5,6,7,8],[9,3,-1,-12]])

#ALLOCATION (YER AYIRTMA)
#data cok buyukse liste.append() yapmak programi cok yavaslatir.
# bunun yerine 0lardan olusan bir matris olusturup, guncelleme yapariz.
zeros=np.zeros((3,4))
zeros[0,0]=5

#ayni mantigi 1'lerle yapabiliriz.
ones=np.ones((3,4))

#ayni mantigi bos elemanlarla da yapabiliriz.
empty=np.empty((3,4)) # aslinda bos degil, cokcok kücük bir sayi

#aralikli sayi yazdirma
a=np.arange(10,50,5) # 10 inclusive,50 exclusive

# aralik verip, 20 eleman olsun derse
b=np.linspace(10,50,20) # 10'dan 50'ye kadar 20 eleman. linspace'de 50 inclusive

#%%
import numpy as np
list1=np.array([1,2,3,4,5])
list2=np.array([5,10,2,11,20])
print(list1+list2)
print(list1-list2)
print(list1**2)
print(np.sin(list1)) # sinus alir.
print(list1<3) # boolean doner.

#element wise product
print(list1*list2)
#transpose
list2=list2.T
#matrix product
matrixProduct=list1.dot(list2)
#exponential
exponential=np.exp(list1)
#random
randomList=np.random.random((5,5))
#sum
summation=randomList.sum()
randomMax=randomList.max()
randomMin=randomList.min()

#satir satir, sutun sutun toplama 
array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(array.shape)
a=array.reshape(3,5)
columnSum=a.sum(axis=0)
rowSum=a.sum(axis=1)

#square and squareroot
squareroot=np.sqrt(randomList)
square=np.square(randomList)

#adding List
addingList=np.add(list1,list2)

#reverse Array
reverseArray=array[::-1]

#satirlarin hepsini al, sutunlardan 0 ve 1 i al.
demanded=a[:,1]
#son satiri al, butun sutunlari al
demanded2=a[-1,:]
