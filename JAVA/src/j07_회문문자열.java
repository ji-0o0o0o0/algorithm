import java.util.Scanner;

public class j07_회문문자열 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().toLowerCase();
        String res = "YES";
        for (int i = 0; i <str.length()/2 ; i++) {
            if(str.charAt(i) != str.charAt(str.length()-i-1)){
                res = "NO";
                break;
            }
        }
        System.out.println(res);
    }
}
