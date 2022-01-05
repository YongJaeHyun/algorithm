import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main{
    public static void main(String[] args) throws Exception{
        
        int sum = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[] ch = br.readLine().toCharArray();
        for (int i = 0; i < n; i++)
        {
            sum += Character.getNumericValue(ch[i]);
        }
        System.out.println(sum);
    }
 
}