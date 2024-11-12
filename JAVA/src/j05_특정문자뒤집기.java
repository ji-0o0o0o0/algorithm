import java.util.Scanner;

public class j05_특정문자뒤집기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        StringBuffer sb = new StringBuffer(str.replaceAll("[^A-z]", ""));
        String rev = sb.reverse().toString();
        for(int i = 0;i<str.length();i++){
            if (Character.isAlphabetic(str.charAt(i))) {
                System.out.print(rev.charAt(0));
                rev = rev.substring(1);
            } else {
                System.out.print(str.charAt(i));
            }
        }
    }
}
