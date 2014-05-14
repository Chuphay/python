from nose.tools import *
import random
import week1.multiply
import week1.my_sort, week1.tp9
import week1.inversions
import week1.merge_sort2

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
    
def test_merge_sort2():
    a = [i for i in xrange(100000)]
    random.shuffle(a)
    assert_equal(week1.merge_sort2.merge_sort(a),sorted(a))     
    
def test_tp9():
    a = [i for i in xrange(100000)]
    random.shuffle(a)
    assert_equal(week1.tp9.merge_sort(a),sorted(a))          
  
def test_inversions_simple():
    num1 = [1,3,5,2,4,6]
    num2 = [7,6,5,4,3,2,1]
    assert_equal(week1.inversions.method(num1),3)
    assert_equal(week1.inversions.method(num2),21)

def test_inversions_hard():
    for i in range(20): 
        l = [i for i in xrange(1000)]
        a = [i for i in xrange(998)]
        random.shuffle(a)
        a = a[:100]
        week1.inversions.invert_this(l,a)
        assert_equal(week1.inversions.method(l),100)        
