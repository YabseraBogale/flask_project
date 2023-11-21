using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  class Process{
    int ArrivalTime;
    int WaitingTime;
    int StartTime;
    int Remain;
    Random numbers;
    string ProcessName;
    int BurstTime;
    int [] RandomNonNumbers;
    Process(int ArrivalTime,int StartTime,int BurstTime,string ProcessName){
        this.ArrivalTime=ArrivalTime;
        this.BurstTime=BurstTime;
        this.StartTime=StartTime;
        this.WaitingTime=StartTime-ArrivalTime;
        this.ProcessName=ProcessName;
    }
    public int[] GivingNonRepeateRandomNumber(int LengthOfRandomNumber,int MaxRange=10){
      this.RandomNonNumbers=new int[LengthOfRandomNumber];
      for(int i=0;i<LengthOfRandomNumber;i++){
          int number=this.numbers.Next(MaxRange);
          if(this.RandomNonNumbers.Contains(number)==false){
              this.RandomNonNumbers[i]=number;
          } else{
              i-=1;
          }
      }
      return this.RandomNonNumbers;
    }
    public int GetArrivalTime(){ return this.ArrivalTime; }
    public int GetWaitingTime(){ return this.WaitingTime; }
    public int GetStartTime(){ return this.StartTime; }
    public string GetProcessName(){ return this.ProcessName; }
  }

  public static void Main()
  {
    
  }


}

