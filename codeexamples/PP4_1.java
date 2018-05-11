import java.util.*;

/**
 * User inputs a year greater thatn 1581 and the program will determine if the year is a leap year.
 * 
 * @author Mike Davidovich
 * @version 1.0
 */
public class PP4_1
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int year;
        
        System.out.print("What is the year you'd like to check (0 to end)? ");
        year = scan.nextInt();
        
        while (year != 0)
        {
            if (year < 1582)
            {
                System.out.print("Please enter a year greater than 1581.\n");
            }
            else if (year % 4.0 == 0 && year % 100.0 == 0 && year % 400.0 > 0)
            {
                System.out.print(year + " is a not a leap year.\n");
            }
            else if (year % 4.0 == 0)
            {
               System.out.print(year + " is a leap year.\n");
            } 
             else if (year % 4.0 > 0)
            {
               System.out.print(year + " is a not a leap year.\n");
            } 
            System.out.print("What is the year you'd like to check (0 to end)? ");
            year = scan.nextInt();
        }
        
    }
}
