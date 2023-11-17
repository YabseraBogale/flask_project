// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        Console.WriteLine ("Hello Mono World");
    }
    static int[]giveFive(int number,out int sum,ref bool three){
        int[] array=new int[5];
        bool stop=false;
        int i=1;
        int k=0;
        sum=0;
        while(stop!=true){
            int isnumber=number+i;
            if(isnumber==0 || isnumber==1){
                continue;
            } else if(isnumber==2){
                if(k<5){
                    a[k]=isnumber;
                    k+=1;
                    if(k==5){
                        stop=true;
                    }
                }
            } else if(isnumber%2!=0){
                bool isprime=true;
                for(int j=2;j<(int)Math.Sqrt(isnumber);j++){
                    if(isnumber%j==0){
                        isprime=false;
                    }
                }
            }
            
        }
        
        
    }
}
