import java.util.Scanner;
public class Sjecista
{
   public static int lineSum;
    public static int Lines(int vert)
    {
        if(vert==3)
        {
            return 0;
        }
        else
        {
            return (vert-2)+Lines(vert-1);
        }
    }
    public static int Inter(int lines, int num)
    {
      int counter = num - 1;
      if(lines ==0)
         return 0;
      if(lines ==2)
         return 1;
      else
         counter--;
      lineSum = Linesum(lines-counter, num-1);
      int numholder = num-1;
         return lineSum+numholder + Inter(lines-counter, num-1);
    }
    public static int Linesum(int lines, int num)
    {
    int total = 0;
    for(int i = num; i>4;i--)
     {
      total += Lines(i);
     }
     return total;
    }
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int line = Lines(num);
        int answer = Inter(line, num);
        System.out.println(answer);
    }
}
