using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  class School{
    private string FirstName;
    private string MiddleName;
    private string LastName;
    public School(){
      this.FirstName="Johne";
      this.MiddleName="Swith";
      this.lastName="Doe";
    }
    public School(string FirstName,string MiddleName,string LastName){
        this.FirstName=FirstName;
        this.MiddleName=MiddleName;
        this.LastName=LastName;
    }
    public School(string FirstName):this(){
        this.FirstName=FirstName;
    }
    public School(string FirstName,string MiddleName):this(){
        this.MiddleName=MiddleName;
    }
    public string firstName{
      get{return FirstName;}
      set{
        FirstName=value;
      }
    }
    public string middleName{
      get{return MiddleName;}
      set{
        MiddleName=value;
      }
    }
     public string lastName{
      get{return LastName;}
      set{
        LastName=value;
      }
    }

    
  }
  public static void Main()
  {
    School addi=new School("","Yabsera");
    Console.WriteLine(addi.firstName);
    Console.WriteLine(addi.lastName);
    Console.WriteLine(addi.middleName);
    
  }
}

