package hackerrank;
import java.util.Scanner;

public class funnystring {
	
	static String funny(String s) {
		String r = (new StringBuffer(s)).reverse().toString();
		for (int i = 1; i < s.length(); i++) {
			if (Math.abs(((int)s.charAt(i)) - ((int)s.charAt(i-1))) != Math.abs(((int)r.charAt(i)) - ((int)r.charAt(i-1)))) {
				return "Not Funny";
			}
		}
		return "Funny";
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int q = in.nextInt();
		for(int i = 0; i < q; i++) {
			String s = in.next();
			String ans = funny(s);
			System.out.println(ans);
		}
	}
}
