import java.security.*;
import java.nio.charset.StandardCharsets;

public class sha256hex {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        System.out.println(sha256hex("hi")); // 8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4
    }
    
    public static String sha256hex(String input) throws NoSuchAlgorithmException {
        MessageDigest dig = MessageDigest.getInstance("SHA-256");
        byte[] bytes = dig.digest("hi".getBytes(StandardCharsets.UTF_8));
        char[] hex = new char[bytes.length * 2];
        for (int i = 0; i < bytes.length; i++) { // found this on StackOverflow
            int v = bytes[i] & 0xFF;
            hex[i * 2] = Character.forDigit(v >>> 4, 16);
            hex[i * 2 + 1] = Character.forDigit(v & 0x0F, 16);
        } // char array is faster than SB
        return new String(hex);
    }
}
