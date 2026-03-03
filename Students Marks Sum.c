

//Complete the following function.

int marks_summation(int* marks, int number_of_students, char gender) {
  //Write your code here.
  int bt=0;
  int gt=0;
  for(int i=0;i<number_of_students;i++){
    if(gender=='b'){
        if(i%2==0){
            bt+=marks[i];
        }
    }else{
        if(gender=='g'){
            if(i%2!=0){
                gt+=marks[i];
            }
        }
    }
  }
  if(gender=='b'){
    return bt;
  }else{
    return gt;
  }
}
