using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  class Result{
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
    public void ViewResult(){
      Console.WriteLine("test-exam: {0}\nmid-exam: {1}\nfinal-exam:{2}\ntotal-result:{3}",Test,Mid,Final,this.CaluclateTotal());
    }
  }
  class Course:Result{
    public string cid{get;set;}
    public string name{get;set;}
    public void AddCourse(string cid,string name,float t,float m,float f){
        this.cid=cid;
        this.name=name;
        this.Test=t;
        this.Mid=m;
        this.Final=f;
    }
    public void Displaly(){
      Console.WriteLine("Course Name: {0}\nCourse Id: {1}",name,cid);
      this.ViewResult();
    }

  }
  public static void Main()
  {
      Course test1=new Course();
      Course test2=new Course();
      Console.WriteLine("Test 1");
      test1.AddCourse("cs3093","RAD",5,4,10.2F);
      test1.Displaly();
      Console.WriteLine("Test 2");
      test2.AddCourse("cs3094","Introduction To AI",9,5,11.2F);
      test2.Displaly();

  }
}

