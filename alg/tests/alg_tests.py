from nose.tools import *
import random
import week1.multiply
import week1.my_sort

def test_grade_school_simple():
    for i in range(10):
        for j in range(10):
            assert_equal(week1.multiply.grade_school(i,j),i*j)
def test_grade_school_hard():            
    for i in range(20):        
        A = random.randint(1,10000000)
        B = random.randint(1,10000000)
        assert_equal(week1.multiply.grade_school(A,B),A*B)
        
def test_sort():
    a = [i for i in xrange(100000)]
    random.shuffle(a)
    b = [i for i in xrange(900)]
    random.shuffle(b)
    assert_equal(week1.my_sort.insert_sort(b),sorted(b))
    assert_equal(week1.my_sort.merge_sort(a),sorted(a))       
  
