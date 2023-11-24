using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  public class Hello{
      int a;
      int b;
      public Hello(){ }
      public Hello(int a=10){
        this.a=a;
      }
      public Hello(int b=10){
        this.b=b;
      }
      
      public int seea(){ return this.a;}
      public int seeb(){ return this.b;}

  }
  public static void Main()
  {
    // no argument then it calls the default parameter.
    Hello hi=new Hello();
    Console.WriteLine("Value hi at a {0}.\nValue hi at b {1}.",hi.seea(),hi.seeb()); 

    
  }

 
}

