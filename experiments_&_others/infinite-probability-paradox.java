/*
 * Interesting experiment that shows how the probability behaves on a infinitely 
 * improbable sequence on a infinity number of attempts generating numbers almost ramdom 
 */

 import java.util.Random;

public class main {
   public static void main(String[] args) {
      Random rand = new Random();
      int count = 0;
      int bound = 10;
      while(true){
         int randNum1 = rand.nextInt(bound + 1);
         int randNum2 = rand.nextInt(bound + 1);
         count++;
         if(randNum1 == randNum2){
            System.out.println(count);
            break;
         }else{
            bound += 10;
         }
      }      
   }
}
