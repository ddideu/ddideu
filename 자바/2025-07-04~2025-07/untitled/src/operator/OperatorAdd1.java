package operator;

public class OperatorAdd1 {

    public static void main(String[] args) {
        int a = 0;

        a = a + 1;
        System.out.println("a = " + a); //1

        a = a + 1;
        System.out.println("a = " + a); // 2

        // 위에꺼 불편해! 증감 연산자가 필요하다!
        ++a; // a = a + 1
        System.out.println("a = " + a); // 3
        ++a;
        System.out.println("a = " + a); // 4

        --a;
        System.out.println("a = " + a); // 3
    }
}
