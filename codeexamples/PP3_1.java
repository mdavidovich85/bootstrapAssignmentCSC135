import java.util.*;

/**
 * Creates a user name using the first letter of a person's first name, the first five letters of the 
 * user's last name and a random number between 10 and 99.  User's last name must be at least 5 characters
 * long or out of range error will occur.  
 * 
 * @author Mike Davidovich
 * @version 8/16/2016
 */
public class PP3_1
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        
        System.out.print("What is your first name? ");
        String first_name = scan.nextLine();
        
        System.out.print("What is your last name? ");
        String last_name = scan.nextLine();
        
        String user_name = first_name.charAt(0) + last_name.substring(0,5) + (rand.nextInt(90)+10);
        System.out.println(user_name);
    }
    
}
