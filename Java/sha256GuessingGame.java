import java.security.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class sha256GuessingGame {
    private static final String correct = "527aa9f431539da8e151d5434d1d5e611d973f601d8e970790882624554146b0";

    public static void main(String[] args) throws NoSuchAlgorithmException {
        Scanner wow = new Scanner(System.in);
        int count = 0;
        System.out.println("Guess the alphanumeric string (6 characters)!\n");
        guesser(Math.pow(62, 6), 6);
        while (true) {
            count++;
            System.out.print("Guess " + count + ": ");
            if (sha256hex(wow.nextLine()).equals(correct)) {
                System.out.println("\nCONGRATS! You are correct (in " + count + " guesses)!");
                System.exit(0);
            }
        }
    }
    
    public static String sha256hex(String input) throws NoSuchAlgorithmException {
        MessageDigest dig = MessageDigest.getInstance("SHA-256");
        byte[] bytes = dig.digest(input.getBytes(StandardCharsets.UTF_8));
        char[] hex = new char[bytes.length * 2];
        for (int i = 0; i < bytes.length; i++) { // found this on StackOverflow
            int v = bytes[i] & 0xFF;
            hex[i * 2] = Character.forDigit(v >>> 4, 16);
            hex[i * 2 + 1] = Character.forDigit(v & 0x0F, 16);
        } // char array is faster than SB
        return new String(hex);
    }

    public static void guesser(double guesses, int length) throws NoSuchAlgorithmException {
        final String alphaNumeral = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        final String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        final String numeral = "0123456789"
        final String upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        final String lower = "abcdefghijklmnopqrstuvwxyz"
        String guess = "";

        for (double i = 0; i < guesses; i++) {
            for (int j = 0; j < length; j++) {
                guess += alphaNumeral.charAt((int)(Math.random() * 62));
            }
            if (sha256hex(guess).equals(correct)) {
                System.out.println("The correct string is: " + guess + "\n");
                break;
            }
            guess = "";
        }
    }
}
