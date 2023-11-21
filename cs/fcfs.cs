using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  class Process{
    string ProcessName;
    int ArrivalTime;
    int BurstTime;
    public void setAll(string ProcessName,int ArrivalTime,int BurstTime){
        this.ProcessName=ProcessName;
        this.ArrivalTime=ArrivalTime;
        this.BurstTime=BurstTime;
    }
    public int getArravelTime(){
      return this.ArrivalTime;
    }
    public int getBurstTime(){
      return this.BurstTime;
    }
    public string getProcessName(){
      return this.ProcessName;
    }
  }
  public static void main(){
      Process[] processing=new Process[5];
      Random number=new Random();
      processing[0].setAll("p1",5,7);
      processing[1].setAll("p2",3,5);
      processing[2].setAll("p3",4,3);
      processing[3].setAll("p1",2,4);
      foreach(Process i in processing ){
          Console.WriteLine(i.getProcessName()+' '+i.getArravelTime()+ i.getBurstTime());
      }
  }
}

