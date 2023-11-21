using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  
  public class Process{
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
    string ProcessName;
    public Process(){

    }

    public Process(int ProcessName,int ArrivalTime,int StartTime=0,int BurstTime=0,int Priority=0,int TimeSlot=0,int StopTime=0){
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
    
    public void SetRemain(int StopTime){
        this.Remain=this.BurstTime-StopTime;
    }

    public int GetStopTime(){ return this.StopTime; }

    public int GetBurstTime(){ return this.BurstTime; }

    public int GetArrivalTime(){ return this.ArrivalTime; }
    
    public int GetWaitingTime(){ return this.WaitingTime; }
    
    public int GetStartTime(){ return this.StartTime; }
    
    public int GetPositionAtTheSequnce(){ return PositionAtTheSequnce; }

    public bool GetDone(){ return this.Done; }

    public string GetProcessName(){ return this.ProcessName; }

    public int GetPriority(){ return this.Priority; }
  
    public int GetRemain(){ return this.Remain; }

    public void SeeArrivalAndBurstTime(){
        Console.WriteLine("Process Name: {0}, Arrival-Time: {1}, Burst-Time: {1}",this.ProcessName,this.ArrivalTime,this.BurstTime);    
    }
    public void SeeArrivalAndBurstTime(Process P){
        Console.WriteLine("Process Name: {0}, Arrival-Time: {1}, Burst-Time: {1}",P.GetProcessName(),P.GetArrivalTime(),P.GetBurstTime());    
    }
    public void SeeArrivalAndBurstTime(Process[] P){
      foreach(Process p in P){
          p.SeeArrivalAndBurstTime();
      }      
    }
    
     
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

public static int[] GetRepeateRandomNumber(int LengthOfRandomNumber,bool Repeat=false,int MaxRange=10){
      int[] RandomNumbers=new int[LengthOfRandomNumber];
      Random numbers=new Random();
      for(int i=0;i<LengthOfRandomNumber;i++){
          int number=numbers.Next(MaxRange);
          if(Repeat==false){
              if(RandomNumbers.Contains(number)==false){
                RandomNumbers[i]=number;
              } else{
                i-=1;
              }
          } else{
            RandomNumbers[i]=number;
          }
      }
      return RandomNumbers;
    }
  public static Process[] GetRandomMadeProcess(int NumberOfProcess,bool Repeat=false){

    Process[] p= new Process[NumberOfProcess];
    Process temp=new Process();
    int[] RandomArrivalTime=GetRepeateRandomNumber(NumberOfProcess,Repeat,10);
    int[] RandomBurstTime=GetRepeateRandomNumber(NumberOfProcess,Repeat,10);
    for(int i=0;i<NumberOfProcess;i++){
        p[i]= new Process(i,RandomArrivalTime[i],0,RandomBurstTime[i],0,0);
    }
    temp.SeeArrivalAndBurstTime(p);
    return p;
  }

  public static void Main()
  {
    Process[] p=GetRandomMadeProcess(5,true);
    
  }


}

