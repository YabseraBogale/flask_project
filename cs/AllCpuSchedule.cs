using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  class Process{
    int ArrivalTime;
    int WaitingTime;
    int BurstTime;
    int StartTime;
    int Priority;
    int Remain;
    int TimeSlot;
    int StopTime;
    Random numbers;
    string ProcessName;
    int [] RandomNumbers;
    
    public Process(){

    }

    Process(string ProcessName,int ArrivalTime,int StartTime,int BurstTime,int Priority=0,int TimeSlot=0,int StopTime=0){
        this.ArrivalTime=ArrivalTime;
        this.BurstTime=BurstTime;
        this.StartTime=StartTime;
        this.WaitingTime=StartTime-ArrivalTime;
        this.ProcessName=ProcessName;
        this.Priority=Priority;
        this.TimeSlot=TimeSlot;
        this.StopTime=StopTime;
    }

    public void SetStopTime(int StopTime){
        this.StopTime=StopTime;
    }
    
    public int[] GivingRepeateRandomNumber(int LengthOfRandomNumber,int MaxRange=10,bool Repeat=false){
      this.RandomNumbers=new int[LengthOfRandomNumber];
      for(int i=0;i<LengthOfRandomNumber;i++){
          int number=this.numbers.Next(MaxRange);
          if(Repeat==false){
              if(this.RandomNumbers.Contains(number)==false){
                this.RandomNumbers[i]=number;
              } else{
                i-=1;
              }
          } else{
            this.RandomNumbers[i]=number;
          }
      }
      return this.RandomNumbers;
    }

    public void SetRemain(int StopTime){
        this.Remain=this.BurstTime-StopTime;
    }

    public int GetStopTime(){ return this.StopTime; }

    public int GetArrivalTime(){ return this.ArrivalTime; }
    
    public int GetWaitingTime(){ return this.WaitingTime; }
    
    public int GetStartTime(){ return this.StartTime; }
    
    public string GetProcessName(){ return this.ProcessName; }

    public int GetPriority(){ return this.Priority; }
  
    public int GetRemain(){ return this.Remain; }
  }

  void SortBasedOnArrivalTime(ref Process[] p){
    for(int i=0;i<p.Length;i++){
        for(int j=0;j<i;i++){
            if(p[i].GetArrivalTime()<p[j].GetArrivalTime()){
                Process temp=new Process();
                p[j]=p[i];
                p[i]=temp;
            }
        }
    }
  }

  public static void Main()
  {
  
  }


}

