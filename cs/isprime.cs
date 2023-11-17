public static void Main(string[] args)
    {
        int number=5;
        int sum=0;
        bool three=true;
        int[] arr=giveFive(number,out sum,ref three);
        foreach(int i in arr){
            Console.WriteLine("Number: {0}",i);
        }
    }
    static int[]giveFive(int number,out int sum,ref bool three){
        int[] a=new int[5];
        bool stop=false;
        int i=1;
        int k=0;
        
        sum=0;
        while(stop!=true){
            int isnumber=number+i;
			bool isprime=true;
            if(isnumber==0 || isnumber==1){
                isprime=false;
                i+=1;
				continue;
            } else if(isnumber%2==0){
				isprime=false;
				i+=1;
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
				
                for(int j=2;j<isnumber;j++){
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
            i+=1;
        }
        three=sum%3==0;
        return a;
        
    }
