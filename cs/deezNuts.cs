using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  public static void Main()
  {
    int a = 123;
    int[] c=new int[]{1,2,3};
    System.Int32 b = 123;
    bool same=a.GetType().Name==b.GetType().Name;
    Console.WriteLine("the same or not is {0} for a {1} is {2} and b {3} is {4}",same,a,a.GetType().Name,b,b.GetType().Name);
  }
}

