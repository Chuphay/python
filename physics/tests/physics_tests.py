from nose.tools import *
import physics.Aitken 
import physics.up_and_down
pnts_1 = [0.0,0.5,1.0]
fn_1 = [0.0,0.5,1.0]
pnts_2 = [0.0,0.5,1.0,1.5,2.0]
fn_2 = [1.0,0.938470,0.765198,0.511828,0.223891]
def test_Aitken_method():
    assert_equal(physics.Aitken.method(0.9,pnts_1,fn_1),0.9)
    assert_equal(round(physics.Aitken.method(0.9,pnts_2,fn_2),6),0.807473)
def test_up_and_down():
    assert_equal(round(physics.up_and_down.aitken(0.9,pnts_2,fn_2,(4,0)),6),0.807473) 
