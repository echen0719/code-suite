// curated from online resources

public class MersennePrime {
    public static void main(String[] args) {
        int lim = (int)(Math.pow(10, 9));
        String primes = "Mersenne Primes: ";

        for (int n = 2; n <= lim; n++) {
            int msr = (int) Math.pow(2, n) - 1; // 2^n - 1
            boolean isPrime = true;

            for (int i = 2; i <= Math.sqrt(msr); i++) {
                if (msr % i == 0) { // sees if a divisor from 2 to sqrt(msr) exists
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) {
                if (primes.length() > 17) {
                    primes += ", "; // adds to a string
                }
                primes += msr;
            }
        }

        System.out.println(primes);
    }
}