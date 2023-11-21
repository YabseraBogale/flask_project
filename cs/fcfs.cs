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
    
    int[] numbers=GiveMeNoRepateRandomArrayNumber(5,10);
    Process[] process= new Process[numbers.Length];
    Random number=new Random();
    for(int i=0;i<process.Length;i++){
      process[i]=new Process();
      process[i].setAll(i.ToString(),numbers[i],numbers[i]*number.Next(numbers[i]));
    }
    foreach(Process i in process ){
        Console.WriteLine("Process-Name: {0}, Arrival-Time: {1}, Burst-Time: {2}",i.getProcessName(),i.getArravelTime(),i.getBurstTime());
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
  static int[] getTimeSorted(Process[] p){
      int [] sortedTime=new int[p.Length];
      
      return sortedTime;
  }
   
}

