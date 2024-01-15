
// C# implementation for Priority Scheduling with 
// Different Arrival Time priority scheduling 
// 1. sort the processes according to arrival time 
// 2. if arrival time is same the acc to priority 
// 3. apply fcfs
using System;

class Program
{
  static int totalprocess = 5;
  static int[][] proc = new int[totalprocess][];
  static int[] arrivaltime = new int[] {1, 2, 3, 4, 5};
  static int[] bursttime = new int[] {3, 5, 1, 7, 4};
  static int[] priority = new int[] {3, 4, 1, 7, 8};


  // Driver code
  static void Main(string[] args)
  {
    for (int i = 0; i < totalprocess; i++)
    {
      proc[i] = new int[4];
      proc[i][0] = arrivaltime[i];
      proc[i][1] = bursttime[i];
      proc[i][2] = priority[i];
      proc[i][3] = i + 1;
    }

    Array.Sort(proc, (x, y) => x[2].CompareTo(y[2]));
    Array.Sort(proc, (x, y) => x[0].CompareTo(y[0]));
    Findgc();
  }
  
  // Using FCFS Algorithm to find Waiting time 
  static void GetWtTime(int[] wt)
  {
    
    // declaring service array that stores
    // cumulative burst time 
    int[] service = new int[totalprocess];
    
    // Initialising initial elements 
    // of the arrays
    service[0] = 0;
    wt[0] = 0;

    for (int i = 1; i < totalprocess; i++)
    {
      service[i] = proc[i - 1][1] + service[i - 1];
      wt[i] = service[i] - proc[i][0] + 1;

      // If waiting time is negative,
      // change it o zero 
      if (wt[i] < 0)
      {
        wt[i] = 0;
      }
    }
  }

  // Filling turnaroundtime array
  static void GetTatTime(int[] tat, int[] wt)
  {
    for (int i = 0; i < totalprocess; i++)
    {
      tat[i] = proc[i][1] + wt[i];
    }
  }

  static void Findgc()
  {
    
    // Declare waiting time and
    // turnaround time array 
    int[] wt = new int[totalprocess];
    int[] tat = new int[totalprocess];
    int wavg = 0;
    int tavg = 0;
    
    // Function call to find waiting time array 
    GetWtTime(wt);
    
    // Function call to find turnaround time
    GetTatTime(tat, wt);
    int[] stime = new int[totalprocess];
    int[] ctime = new int[totalprocess];
    stime[0] = 1;
    ctime[0] = stime[0] + tat[0];

    Console.WriteLine("Process_no\tStart_time\tComplete_time\tTurn_Around_Time\tWaiting_Time");

    // calculating starting and ending time
    for (int i = 0; i < totalprocess; i++)
    {
      wavg += wt[i];
      tavg += tat[i];
      Console.WriteLine(proc[i][3] + "\t\t" + stime[i] + "\t\t" + ctime[i] + "\t\t" + tat[i] + "\t\t\t" + wt[i]);
      
      
      // display the process details
      if (i != totalprocess - 1)
      {
        stime[i + 1] = ctime[i];
        ctime[i + 1] = stime[i + 1] + tat[i + 1] - wt[i + 1];
      }
    }

    // display the average waiting time 
    // and average turn around time
    Console.WriteLine("Average waiting time is: " + (double)wavg / totalprocess);
    Console.WriteLine("Average turnaround time is: " + (double)tavg / totalprocess);
  }
}

// This code is contributed by shiv1o43g
