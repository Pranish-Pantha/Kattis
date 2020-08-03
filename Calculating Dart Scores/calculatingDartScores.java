import java.util.Scanner;
public class calculatingDartScores
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int input = in.nextInt();
        int num1 = 0;
        int num2 = 0;
        int num3 = 0;
        String s1 = null;
        String s2 = null;
        String s3 = null;
        int numOfShots = 0;
        
        if(input<=20)
        {
        num1 = input;
        s1 = "Single ";
        numOfShots = 1;
        }
        else if(input<=40)
        {
        num1 = 20; num2 = input-20;
        s1 = "Single "; s2 = "Single ";
        numOfShots = 2;
        }
        else if(input <=60)
        {
        num1 = 20; num2 = 20; num3 = input - 40;
        s1 = "Single "; s2 = "Single "; s3 = "Single ";
        numOfShots = 3;
        }
        else if(input <=80)
        {
        num1 = 20; num2 = input - 60;
        s1 = "Triple ";  s2 = "Single ";
        numOfShots = 2;
        }
        else if(input <=100)
        {
        num1 = 20; num2 = 20; num3 = input - 80;
        s1 = "Triple "; s2 = "Single "; s3 = "Single ";
        numOfShots = 3;
        }
        else if(input <=120)
        {
        num1 = 20; num2 = 20; num3 = input - 100;
        s1 = "Triple "; s2 = "Double "; s3 = "Single ";
        numOfShots = 3;
        }
        else if(input<=140)
        {
        num1 = 20; num2 = 20; num3 = input - 120;
        s1 = "Triple "; s2 = "Triple "; s3 = "Single ";
        numOfShots = 3;
        }
        else if (input <=160)
        {
        if((input - 120)%3==0)
         {
         num1 = 20; num2 = 20; num3 = (input - 120)/3;
            s1 = "Triple "; s2 = "Triple "; s3 = "Triple ";
            numOfShots = 3;
         }
        else if(input%2!=0)
         {
            if((input-117)%2==0)
            {
            num1 = 20; num2 = 19; num3 = (input - 117)/2;
            s1 = "Triple "; s2 = "Triple "; s3 = "Double ";
            numOfShots = 3;
            }
            else
            {numOfShots = 4;}
         }
         
         else
         {
            num1 = 20; num2 = 20; num3 = (input - 120)/2;
            s1 = "Triple "; s2 = "Triple "; s3 = "Double ";
            numOfShots = 3;
         }
        }
        else if(input <=180)
        {
        if((input - 120)%3==0)
         {
         num1 = 20; num2 = 20; num3 = (input - 120)/3;
            s1 = "Triple "; s2 = "Triple "; s3 = "Triple ";
            numOfShots = 3;
         }
        else if(input%2!=0||(input-120)/2>20)
         {
            numOfShots = 4;
         }
         else
         {
            num1 = 20; num2 = 20; num3 = (input - 120)/2;
            s1 = "Triple "; s2 = "Triple "; s3 = "Double ";
            numOfShots = 3;
         }

        }
        if(numOfShots==1)
        {
        System.out.println(s1 + num1);
        }
        else if(numOfShots==2)
        {
         System.out.println(s1 + num1);
         System.out.println(s2 + num2);
        }
        else if(numOfShots == 3)
        {
        System.out.println(s1 + num1);
        System.out.println(s2 + num2);
        System.out.println(s3 + num3);
        }
        else
        {
        System.out.println("impossible");
        }
    }

}