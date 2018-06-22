""" Solve in logN time"""
import sys
sys.setrecursionlimit(1500)
def power(a,b):

    if b==0:
        return 1

    res = power(a,b/2)
    res*=res

    if b%2!=0:
        res*=a

    return res


print(power(2,3))

"""
c++
#include<iostream>

int power(int a,int b)
{
  if b==0}{ return 1;}
  int res = power(a,b/2);
  res*=res;
  
  if (b%2!=0)
  {
    res=res*a;
  }
  
  return res
}

int main() {
  
  cin>>a;
  cin>>b
  
  cout<<(power(a,b))
  
  
	return 0;
}"""
