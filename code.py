add(int a,int b,int div){
int count=0;
for(int i=a;i<=b;i++){
    if(i%div==0){
      count=count+1;
}
    else{
    coutinue;
}
}
return count;
}