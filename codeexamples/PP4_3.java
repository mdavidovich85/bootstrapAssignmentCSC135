import java.util.*;

/**
 * Takes a user input that is greater than or euqal to 2 and is not a float and prints the sum of all
 * even integers between 2 and the input value.  
 * 
 * @author Mike Davidovich 
 * @version 1.0
 */
public class PP4_3
{
   public static void main(String[] args)
   {
   
   Scanner scan = new Scanner(System.in);
   int input;
   int sum = 0;
   
   System.out.print("What is the number? ");
   input = scan.nextInt();
  
   if (input > 1 && input % 1 == 0)
   {
       for (int i = 2; i < input+1; i++)
            {
                if (i%2 == 0)
                {
                    sum += i;
                }
            }
       System.out.println(sum);
   }
}
}
