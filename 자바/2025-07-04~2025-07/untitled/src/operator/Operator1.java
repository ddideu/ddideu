package operator;

public class Operator1 {
    public static void main(String[] args) {
        int a = 5;
        int b = 2;

        // 덧셈
        int sum = a + b;
        System.out.println("a + b = " + sum); // 출력  a + b = 7

        // 뺄셈
        int diff = a - b;
        System.out.println("a - b = " + diff); // 출력 a - b = 7

        // 곱셈
        int mul = a * b;
        System.out.println("a * b = " + mul); // 출력 a * b = 10

        // 나눗셈
        int div = a / b;
        System.out.println("a / b = " + div); // 출력  a / b = 2

        // 나머지
        int mod = a % b;
        System.out.println("a % b = " + mod); // 나머지 a% b = 1

        int err = 10 / 0;
    }

    public static class Operator2 {
    }
}
