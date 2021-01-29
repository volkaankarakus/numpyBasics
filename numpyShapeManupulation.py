# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 01:15:23 2021

@author: VolkanKarakuş
"""
import numpy as np
array=np.array([[1,2,3],[4,5,6],[7,8,9]])

#convert the matrix from 3x3 to 1x9
a=array.ravel()

#undo
array2=a.reshape(3,3)

#array transpose
arrayTranspose=array2.T

# reshape ve resize arasindaki fark
# reshape yapinca asil matris degismez
# resize yapinca asil matris degisir.
# reshape yapiliyorsa bunu baska bir matrise esitlememiz gerekir kısaca.

#Stacking Arrays
array1=np.array([[1,2],[3,4]])
array2=np.array([[-1,-5],[-6,-23]])

#vertical stack
array3=np.vstack((array1,array2)) # 1  2 
                                  # 3  4
                                  #-1 -5
                                  #-6 -23
        
#horizontal stack
array4=np.hstack((array1,array2)) # 1 2 -1 -5
                                # 3 4 -6 -23
                                
#Convert list between array
liste5=[1,2,3,4,5] #list
array=np.array(liste5) # now it is an array.

arraytoList=list(array) # now it is a list.

#ONEMLI NOT
# a,b,c ayni arrayler olsun. b'yi degistirirsek a da degisir. memoryde ayni yerde tutulduklari icin.
a=np.array([5,8,9])
b=a
c=a
a[0]=20
#suanda a=[20,8,9], b=[20,8,9],c=[20,8,9]
#bunu duzeltmek icin

d=a.copy() #Copy yaparak farkli bir alan yarattik.
e=a.copy()
f=a.copy()
d[0]=57 # d'deki degisiklikten e ve f etkilenmez.


