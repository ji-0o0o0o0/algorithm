import java.util.Scanner;

public class j04_단어뒤집기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i <n ; i++) {
            StringBuffer sb = new StringBuffer(sc.nextLine());
            System.out.println(sb.reverse());
        }
    }
}
