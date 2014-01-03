from nose.tools import *
import ch2.Aitken 
import ch2.aitken
import ch2.least_square as ls
import ch2.uniform_random as rdm
pnts_1 = [0.0,0.5,1.0]
fn_1 = [0.0,0.5,1.0]
pnts_2 = [0.0,0.5,1.0,1.5,2.0]
fn_2 = [1.0,0.938470,0.765198,0.511828,0.223891]
def test_Aitken_method():
    assert_equal(ch2.Aitken.method(0.9,pnts_1,fn_1),0.9)
    assert_equal(round(ch2.Aitken.method(0.9,pnts_2,fn_2),6),0.807473)
def test_aitken_method():
    assert_equal(ch2.aitken.method(0.9,pnts_1,fn_1),0.9)
    assert_equal(round(ch2.aitken.method(0.9,pnts_2,fn_2),6),0.807473)    
def test_aitken_upNdown():
    assert_equal(ch2.aitken.upNdown(0.9,pnts_1,fn_1),0.9)
    assert_equal(round(ch2.aitken.upNdown(0.9,pnts_2,fn_2),6),0.807473)  
def test_ls():
    x_in = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    dat = [6.558,8.206,9.88,11.5,13.14,14.82,16.4,18.04,19.68,21.32,22.96,24.6,26.24,27.88,29.52]
    u = ls.method(21,x_in,dat)
    n = len(dat)-1
    sum = 0
    for i in range(len(dat)):   
        sum += x_in[i]
    e = u[1][n+1]
    dq = u[0][n+1]-u[1][n+1]*sum/(n+1)
    assert_equal(round(e,2),1.64)  
    assert_equal(round(dq,2),0.03)  
def test_rdm():
    assert_equal(int(rdm.ranf()),0)
    seed = 1
    for i in xrange(10000):
        x = rdm.ranf(seed)
        seed = int(x*2147483647)   
    assert_equal(seed,1043618065)       
      
