using System; 

namespace learningCSharp
{
    class Line
    {
        // similar to Java's main method 
        static void Main(string[] agrs)
        {  
            // similar to Python's print or Java's System.out.println
            Console.WriteLine("Hello, World! Everyone starts off with this smh.");
            Console.WriteLine("This is so much like Java I am terrified."); 
            
            int num = 400; 
            Console.WriteLine("Here is an integer: " + num); 

            int num2 = 200; 
            Console.WriteLine("Their total is: " + (num + num2)); 

            // identical to for loops in Java 
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("The current value of i is: " + i); 
            }

            string name = "Chrystopher"; 
            for (int index = 0; index < name.Length; index ++)
            {
                char c = name[index]; 
                Console.WriteLine("The current character is: " + c); 
            }

            long bigNum = 12345678976543210; 
            int smallNum = 0; 
            bool truthy = true;
            
            if (bigNum > smallNum)
            {
                Console.WriteLine(truthy); 
            }

            
            // Waits for user input before closing window 
            Console.ReadLine(); 


        }
    }
}
