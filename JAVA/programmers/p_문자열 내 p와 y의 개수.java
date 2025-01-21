public class p_문자열내p와y의개수 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("pPoooyY"));
    }
}

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        //대문자로 변경
        s= s.toUpperCase();

        int p_num=0;
        int y_num=0;
        char[] chars = s.toCharArray(); // 문자열을 char 배열로 변환
        for (char ch : chars) {
            p_num += ('P'==ch)?1:0;
            y_num += ('Y'==ch)?1:0;
        }
        answer = (p_num==y_num)?true:false;
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

        return answer;
    }
}
