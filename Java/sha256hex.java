import java.security.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class sha256hex {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        Scanner wow = new Scanner(System.in);
        int count = 0;
        String input = "";
        System.out.println("Guess the 9 character alphanumeric string!\n");
        while (true) {
            count++;
            System.out.print("Guess " + count + ": ");
            input = wow.nextLine();
            if (sha256hex(input).equals("35e42b24631bcad0ae668efad72a54389902cd7a48b387aefbc64662ce1f6b5f")) {
                System.out.println("\nCONGRATS! You are correct!");
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
}
