import java.util.*;

/**
 * Creates a random telephone number.  First three digits do not contain 8 or 9, second three are no 
 * greater than 742, and last four digits have no restricitons.  
 * 
 * @author Mike Davidovich
 * @version 8/15/2016
 */
public class PP3_3
{
   public static void main(String[] args)
   {
       
   Random rand = new Random();
   
   int num1, num2, num3;
   
   num1 = rand.nextInt(700)+100;
   num2 = rand.nextInt(643)+100;
   num3 = rand.nextInt(8999)+1000;

   System.out.println(num1 + "-" + num2 + "-" + num3);
   }
}
