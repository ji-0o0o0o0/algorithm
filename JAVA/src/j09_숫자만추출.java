import java.util.Scanner;

public class j09_숫자만추출 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String result ="";
        for(char c : s.toCharArray()){
            if(!Character.isAlphabetic(c)) result += c;
        }
        System.out.println(Integer.parseInt(result));
    }
}
