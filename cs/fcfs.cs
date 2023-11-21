using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
  class Process{
    string ProcessName;
    int ArrivalTime;
    int BurstTime;
    int execuationTime;
    int TimeEnd=0;
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
    public int getexecuationTime(){
      this.execuationTime=this.ArrivalTime+this.BurstTime;
      return this.execuationTime;
    }
    public int getEndTime(Process p){
      this.TimeEnd=p.getexecuationTime()+this.getBurstTime();
      return this.TimeEnd;
    }
  }
  public static void main(){
    
    int[] numbers=GiveMeNoRepateRandomArrayNumber(5,10);
    Process[] process= new Process[numbers.Length];
    Random number=new Random();
    for(int i=0;i<process.Length;i++){
      process[i]=new Process();
      process[i].setAll((i+1).ToString(),numbers[i],number.Next(numbers[i]));
    }
    Console.WriteLine("Before Execuation");
    for(int i=0;i<process.Length;i++){
        if(i-1<0){
          
        }
    }
    for(int i=0;i<process.Length;i++){
          for(int j=0;j<i;j++){
              if(process[j].getArravelTime()>process[i].getArravelTime()){
                Process temp=new Process();
                temp=process[j];
                process[j]=process[i];
                process[i]=temp;
              } 
          }
    }
    Console.WriteLine("Order of Execuation");
    foreach(Process i in process ){
        Console.WriteLine("Process-Name: {0}, Arrival-Time: {1}, Burst-Time: {2}, Execuation-Time: {3}",i.getProcessName(),i.getArravelTime(),i.getBurstTime(),i.getexecuationTime());
    }
  }



  static int[] GiveMeNoRepateRandomArrayNumber(int length,int maxRange){
      int[] arr =new int[length];
      Random numbers=new Random();
      for(int i=0;i<length;i++){
          int number=numbers.Next(maxRange);
          if(arr.Contains(number)==true){
              i-=1;
          }else{
            arr[i]=number;
          }
      }
      return arr;
  }
  
  
   
}

