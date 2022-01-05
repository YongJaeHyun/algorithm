import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] ch = br.readLine().toCharArray();
		for (int i = 0; i < 26; i++) {
			for (int j = 0; j < ch.length; j++) {
				if (ch[j] == (char) i + 97) {
					System.out.print(j+" ");
					break;				
				}
				if (j == ch.length-1) {
					System.out.print(-1+" ");
				}
			}
		}
	}
}