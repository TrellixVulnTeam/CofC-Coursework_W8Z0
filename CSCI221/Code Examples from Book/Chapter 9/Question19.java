
import java.util.Scanner;

public class Question19
{
    public static void main(String[] args)
    {
		try
		{
			System.out.println("try block entered:");
			int number = 42;
			if (number > 0)
				throw new DoubleException("DoubleException thrown!");
			System.out.println("Leaving try block.");
		}
		catch(DoubleException exceptionObject) 
		{
			System.out.println(exceptionObject.getMessage( ));
		}
		System.out.println("End of code.");
    }
}
