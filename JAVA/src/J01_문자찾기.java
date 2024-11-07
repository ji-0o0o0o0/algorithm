import java.util.Scanner;

public class J01_문자찾기 {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        String input1 = in.next();
        String input2 = in.next();

        int sum = 0;

        for(char a : input1.toLowerCase().toCharArray()){
            if(a==input2.toLowerCase().charAt(0))
                sum++;
        }

        System.out.println(sum);
    }
}

