#include <stdio.h>

//void myprint(void);

void myprint(){
    printf("hello world\n");
}

int mynum(){
  printf("you accessed mynum!\n");
  return 33;
}

int myadd(int x, int y){
  return x+y;
}

int * myarray(int *a){
  /*doesn't seem to work so well :( */
  printf("a[0] was: %d\n",a[0]); 
  a[0]++;
  printf("a[1] was: %d\n", a[1]);
  a[1]--;
  return a;
}



