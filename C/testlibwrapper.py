import ctypes

testlib = ctypes.CDLL('/home/chuphay/python/C/testlib.so')
testlib.myprint()
