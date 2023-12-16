using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  class Course{
    float test;
    float mid;
    float final;
    protected float Test{
      get{return test;}
      set{
        if(value>=0||value<=20){
            test=value;
        }
        else{
          Console.WriteLine("Enter The correct Value");
          test=-1;
        }
      }
    }
    protected float Mid{
      get{return mid;}
      set{
        if(value>=0 || value<=30){
          mid=value;
        }else{
          Console.WriteLine("Enter The correct Value");
          mid=-1;
        }
      }
    }
    protected float Final{
      get{return final;}
      set{
        if(value>=0 || value<=50){
            final=value;
        }
        else{
          Console.WriteLine("Enter The correct Value");
          final=-1;
        }
      }
    }
    public void InsertValue(float t, float m,float f){
      Test=t;
      Mid=m;
      Final=f;
    }
    public float CaluclateTotal(){
      return Test+Mid+Final;
    }
    public void ViewResult(string courseName){
      Console.WriteLine("test-exam: {0}\nmid-exam: {1}\nfinal-exam:{2}\ntotal-result:{3}");
    }


  }
  public static void Main()
  {
  
  }
}

