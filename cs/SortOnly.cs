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
