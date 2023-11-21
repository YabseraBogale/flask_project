
/*
Online Java - IDE, Code Editor, Compiler

Online Java is a quick and easy tool that helps you to build, compile, test your programs online.
*/

public class Main
{
    public static void main(String[] args) {
        Process process=new Process()[5];
    }
    
public class Process{
    String ProcessName;
    int ArrivalTime;
    int BurstTime;
    public void setAll(String ProcessName,int ArrivalTime,int BurstTime){
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
    public String getProcessName(){
      return this.ProcessName;
    }
  }

}

