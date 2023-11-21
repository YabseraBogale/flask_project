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
    int PositionAtTheSequnce;
    int TimeSlot;
    int StopTime;
    bool Done=false;
    Random numbers;
    string ProcessName;
    int [] RandomNumbers;
    
    public Process(){

    }

    public Process(int ProcessName,int ArrivalTime,int StartTime,int BurstTime,int Priority=0,int TimeSlot=0,int StopTime=0){
        this.ArrivalTime=ArrivalTime;
        this.BurstTime=BurstTime;
        this.StartTime=StartTime;
        this.WaitingTime=StartTime-ArrivalTime;
        this.ProcessName="P"+ProcessName.ToString();
        this.Priority=Priority;
        this.TimeSlot=TimeSlot;
        this.StopTime=StopTime;
    }

    public void SetStopTime(int StopTime){
        this.StopTime=StopTime;
    }
    
    public void SetPositionAtTheSequnce(int PositionAtTheSequnce){
        this.PositionAtTheSequnce=PositionAtTheSequnce;
    }

    public void SetDone(bool Done){
        this.Done=Done;
    }

    public int[] GetRepeateRandomNumber(int LengthOfRandomNumber,int MaxRange=10,bool Repeat=false){
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

    public int[] GetRepeateRandomNumber(int LengthOfRandomNumber,bool Repeat=false,int MaxRange=10){
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
    
    public int GetPositionAtTheSequnce(){ return PositionAtTheSequnce; }

    public bool GetDone(){ return this.Done; }

    public string GetProcessName(){ return this.ProcessName; }

    public int GetPriority(){ return this.Priority; }
  
    public int GetRemain(){ return this.Remain; }
  }

  void SortBasedOnArrivalTime(ref Process[] p){
    for(int i=0;i<p.Length;i++){
        for(int j=0;j<i;i++){
            if(p[i].GetArrivalTime()<p[j].GetArrivalTime()){
                Process temp=new Process();
                temp=p[j];
                p[j]=p[i];
                p[i]=temp;
            }
        }
    }
  }

  void SortBasedOnPriority(ref Process[] p){
    for(int i=0;i<p.Length;i++){
        for(int j=0;j<i;i++){
            if(p[i].GetPriority()<p[j].GetPriority()){
                Process temp=new Process();
                temp=p[j];
                p[j]=p[i];
                p[i]=temp;
            }
        }
    }
  }

  Process[] MakeProcess(int NumberOfProcess,bool Repeat=false){
      Process[] p= new Process[NumberOfProcess];
      Process temp=new Process();
      int[] RandomArrivalTime=temp.GetRepeateRandomNumber(NumberOfProcess,Repeat);
      int[] RandomBurstTime=temp.GetRepeateRandomNumber(NumberOfProcess);
      return p;

  }

  public static void Main()
  {
    
  }


}

