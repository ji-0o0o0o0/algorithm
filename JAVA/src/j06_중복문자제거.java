import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;

public class j06_중복문자제거 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        StringBuffer sb = new StringBuffer();
        for(char c : str.toCharArray()) {
            if(sb.indexOf(String.valueOf(c))== -1){
                sb.append(c);
            }
        }
        System.out.println(sb.toString());
    }
}
