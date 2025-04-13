import java.math.*;

public class eQUTs {
    public static void main(String[] args) {
            System.out.println(pow(2, 1000));
    }
    public static BigInteger pow(int base, int expo) {
        BigInteger result = BigInteger.ONE;
        BigInteger base2 = BigInteger.valueOf(base);
        for (double i = 0; i < expo; i++) {
            result = result.multiply(base2);
        }
        return result;
    }
}