import java.util.Scanner;

public class j02_대소문자변환 {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        String input1 = in.next();
        StringBuilder result = new StringBuilder();
        for (char a : input1.toCharArray()) {
            if(Character.isLowerCase(a)){
                result.append(Character.toUpperCase(a));
            }else{
                result.append(Character.toLowerCase(a));
            }
        }

        System.out.println(result);
    }
}
