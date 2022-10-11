package com.tutorialspoint.advancedsort;

import java.util.Arrays;

public class ShellSortDemo {
     
   public static void main(String[] args){
      int[] sourceArray = {4,6,3,2,1,9,7};
      System.out.println("Input Array: " +Arrays.toString(sourceArray));
      printline(50);
      System.out.println("Output Array: " 
      + Arrays.toString(shellSort(sourceArray)));
      printline(50);        
   }    

   public static void printline(int count){
      for(int i=0;i <count-1;i++){
         System.out.print("=");
      }
      System.out.println("=");
   }

   public static int[] shellSort(int[] intArray){
      int inner, outer;
      int valueToInsert;
      int interval = 1;
      int elements = intArray.length;
      int i=0;
      while(interval <= elements/3){
         interval = interval*3 +1;                   
      }

      while(interval > 0){
         System.out.println("iteration "+(i) +"#: " 
         +Arrays.toString(intArray));
         for(outer = interval; outer < elements; outer++){
            valueToInsert= intArray[outer];
            inner = outer;
            while(inner > interval -1 && 
               intArray[inner - interval] >= valueToInsert){
               intArray[inner] = intArray[inner - interval];
               inner -=interval;
               System.out.println(" item moved :" + intArray[inner]);
            }
            intArray[inner] = valueToInsert;
            System.out.println(" item inserted :" 
            + valueToInsert +", at position :" + inner);
         }
         interval = (interval -1) /3;           
         i++;
      }     
      return intArray;        
   }
}
