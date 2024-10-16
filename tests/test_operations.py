from src.math_operations import add, sub

def test_add():
  assert add(4,1)==5
  assert add(-1,1)==0

def test_sub():
  assert sub(-1,-1)==0
  assert sub(4,2)==2
  assert sub(5,4)==1