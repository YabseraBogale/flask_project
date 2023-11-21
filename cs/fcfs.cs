using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  class Process{
    string ProcessId;
    int ArrivalTime;
    int BurstTime;
    public void setAll(string ProcessId,int ArrivalTime,int BurstTime){
        this.ProcessId=ProcessId;
        this.ArrivalTime=ArrivalTime;
        this.BurstTime=BurstTime;
    }
    public int getArravelTime(){
      return this.ArrivalTime;
    }
    public int getBurstTime(){
      return this.BurstTime;
    }
  }
  public static void main(){

  }
}

