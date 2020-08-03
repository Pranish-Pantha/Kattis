import java.util.Scanner;
public class maximumRent
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        String[] data1 = in.nextLine().split("\\s+");
        String[] data2 = in.nextLine().split("\\s+");
        int[] check = new int[data1.length];
        int[] check2 = new int[data2.length];
        int answer = 0;
        for(int i = 0; i < data1.length; i++)
         {
            String clone = data1[i];
            check[i] = Integer.parseInt(clone);
         }
         for(int j = 0; j <data2.length; j++)
            {
               String clone2 = data2[j];
               check2[j] = Integer.parseInt(clone2);
            } 
            int xmin = check2[1] - check2[0];
            int xmax = check2[0] - 1;
            int ymin = 1;
            int ymax = (2*check2[0]) - check2[1];
            int max = -1;
            if(xmin<1)
               {xmin = 1;
               ymax = check2[0] - 1;}
            if(ymax > check2[0] -1)
               {
               ymax = check2[0] -1;
               xmin = 1;
               }
            int pos1 = check[0]*xmin + check[1]*ymax;
            int pos2 = check[0]*xmax + check[1]*ymin;
            if(pos1>pos2)
               {
                  max = pos1;
               }
             else
               {
                  max = pos2;
               }
            System.out.println(max);          
    }
}
