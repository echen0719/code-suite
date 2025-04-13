public class bin {
    public static void main(String[] args) {
        System.out.println(binToInt("1111111111111111111111111111111"));
        System.out.println(binToInt("10000000000000000000000000000000")); // overflow

        System.out.println(intToBin(64)); // 1000000
        System.out.println(intToBin(100)); // 1100100

    }

    public static int binToInt (String bin) {
        int deci = 0;
        for (int i = 0; i < bin.length(); i++) {
            deci <<= 1; // moves all bits over left (doubling)
            if (bin.charAt(i) == '1') {
                deci |= 1; // bit wise OR
            }
        } // found on StackOverflow
        return deci;
    }

    public static String intToBin(int deci) {
        if (deci < 2) {
            return Integer.toString(deci); // have to convert
        }
        else {
            return intToBin(deci / 2) + (deci % 2); // recursive call
        }

        // borrowed from APCSA Unit 10 Progress Check #1

        /* Recursive example with 100:

        100 < 2 | + 0
        ->  50 < 2 | + 0
        ->  25 < 2 | + 1
        -> 12 < 2 | + 0
        -> 6 < 2 | + 0
        -> 3 < 2 | + 1
        -> 1 < 2 | return 1

        "1" + "1" + "0" + "0" + "1" + "0" + "0" = 1100100 */
    }
}