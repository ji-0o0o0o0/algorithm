import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class j03_문장속단어 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> list = new ArrayList<String>();
        String str =sc.nextLine();
        String[] test = str.split(" ");
        String max =test[0];
        for (String s : test) {
            if(s.length()>test[0].length()){
                max =s;
            }
        }
        System.out.println(max);
    }
}

//it is time to study