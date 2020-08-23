import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Test {

	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			int x = Integer.parseInt(reader.readLine());
			if(x==0) {
				break;
			}
			int[] answer = new int[32];
			for(int i =0;i<answer.length;i++) {
				answer[i] = -1;
			}
			for(int i = 0; i<x;i++) {
				String[] arr = reader.readLine().split(" ");
				if(arr[0].equals("CLEAR")) {
					answer[Integer.parseInt(arr[1])] = 0;
				}
				else if(arr[0].equals("SET")) {
					answer[Integer.parseInt(arr[1])] = 1;
				}
				else if (arr[0].equals("OR")) {
					int n1 = Integer.parseInt(arr[1]);
				int n2 = Integer.parseInt(arr[2]);

				if(answer[n1]==1 || answer[n2] == 1) {
					answer[n1] = 1;
				}
				else if(answer[n1] ==-1  || answer[n2] == -1) {
					answer[n1] = -1;
				}
			}
				else if (arr[0].equals("AND")) {
					int n1 = Integer.parseInt(arr[1]);
					int n2 = Integer.parseInt(arr[2]);

					if(answer[n1]==0 || answer[n2] == 0) {
						answer[n1] = 0;
					}
					else if(answer[n1] ==-1  || answer[n2] == -1) {
						answer[n1] = -1;
					}
				}
		
			}
		for(int i = answer.length-1;i>=0;i--) {
			if(answer[i]==-1) {
				System.out.print("?");
			}
			else {
				System.out.print(answer[i]);
			}
		}

		System.out.print("\n");
	}

}
}
