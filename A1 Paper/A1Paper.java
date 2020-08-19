import java.util.Scanner;
public class Test {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		double needed = 2;
		double tape = 0;
		int index = 0;
		for(int i = 0; i<n-1;i++) {
			index = in.nextInt();
			tape += (Math.pow(2, (-3/4.0) - i/2.0) * (needed/2.0));
			needed = (needed - index) * 2;
			if (needed <= 0) {
				break;
			}
		}
		if(needed<1) {
			System.out.println(tape);
		}
		else {
			System.out.println("impossible");
		}
	}

}
