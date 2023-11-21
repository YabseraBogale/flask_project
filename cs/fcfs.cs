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
    Console.Write("Enter Number of Process: ");
    int NumberOfProcess=int.Parse(Console.ReadLine());
     Process[] process= new Process[NumberOfProcess];
      Random numbers=new Random();
      for(int i=0;i<NumberOfProcess;i++){
          process[i]=new Process();
          process[i].setAll((i+1).ToString(),numbers.Next(30),numbers.Next(10));
      }
    
  }
   
}

