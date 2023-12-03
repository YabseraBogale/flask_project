using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  public static void Main()
  {
    int num=0;
    int sum;
    what(ref num,out sum);
    // need to make ref decalred and have to use them
    Console.WriteLine($"sum is {sum} and num is {num}");
    nn(1,2,3,4,5);
  }
  static void nn(params int[] arr){
    foreach(int i in arr){
        Console.WriteLine(i);
    }
  }
  static void what(ref int num,out int sum){
      num=2;
      sum=10;
  }
}

