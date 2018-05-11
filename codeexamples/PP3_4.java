import java.util.*;
import java.lang.*;
import java.text.*;

/**
 * Write a description of class PP3_4 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class PP3_4
{
   public static void main(String[] args)
   {
    String coord1, coord2; 
    double x1, y1, x2, y2;
    double result;
    
    Scanner scan = new Scanner(System.in);
    DecimalFormat fmt = new DecimalFormat("0.##");
    
    System.out.println("Input cooredinates in the format (x,y)");
    
    System.out.print("What is the first coordinate? ");
    coord1 = scan.next();
    System.out.print("What is the second coordinate? ");
    coord2 = scan.next();
    
    String[] xy1 = coord1.split(",");
    x1 = Double.valueOf((xy1[0].trim().substring(1).trim()));
    y1 = Double.valueOf((xy1[1].trim().substring(0, xy1[1].trim().length() -1).trim()));
    
    String[] xy2 = coord2.split(",");
    x2 = Double.valueOf((xy2[0].trim().substring(1).trim()));
    y2 = Double.valueOf((xy2[1].trim().substring(0, xy2[1].trim().length() -1).trim()));
   
    result = Math.sqrt((Math.pow(x2-x1,2)+Math.pow(y2-y1,2)));
    
    System.out.println("The distance between " + coord1 + " and " + coord2 + " is " +fmt.format(result) + ".");
   }
    
}
