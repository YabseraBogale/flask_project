// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        
    }
    static int[]giveFive(int number,out int sum,ref bool three){
        int[] array=new int[5];
        bool stop=false;
        int i=1;
        int k=0;
        bool isprime=true;
        sum=0;
        while(stop!=true){
            int isnumber=number+i;
            if(isnumber==0 || isnumber==1){
                continue;
            } else if(isnumber==2){
                if(k<5){
                    a[k]=isnumber;
                    sum+=isnumber;
                    k+=1;
                    if(k==5){
                        stop=true;
                    }
                }
            } else if(isnumber%2!=0){
                for(int j=2;j<(int)Math.Sqrt(isnumber);j++){
                    if(isnumber%j==0){
                        isprime=false;
                        break;
                    }
                }
            }
            if(isprime==true){
                if(k<5){
                    a[k]=isnumber;
                    sum+=a[k];
                    k+=1;
                    if(k==5){
                        stop=true;
                    }
                }
            }
            
        }
        three=sum%3==0;
        return array;
        
    }
}
