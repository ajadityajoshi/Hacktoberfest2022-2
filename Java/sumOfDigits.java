public class Main {
    public static void main(String[] args) {
        System.out.println(sumDigits(125));
        System.out.println(sumDigits(1));
        System.out.println(sumDigits(32123));
    }

    public static int sumDigits(int num){
        if (num < 10){
            return -1;
        } else {

            // converting the integer value to string
            // then using the string method to find length

            int len = String.valueOf(num).length();
            int i = 0;
            int sum = 0;
            while (i < len){                // or while ( num > 0){     // 1 / 10 = 0
                int last_digit = num % 10;  // 125 % 10 = 5, 12 % 10 = 2
                num /= 10;                  // 125 / 10 = 12, num = 12/10 = 1
                sum += last_digit;          // 5 + 2
                i++;
            }
            return sum;
        }
    }
}