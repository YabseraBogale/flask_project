using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  public static void Main()
  {
    int p=1;
    int i=hello(p);

    
  }
  static int hello(int p){
      int sum=0;
      p+=1;
      sum+=p;
      return sum;
  }

  
}

