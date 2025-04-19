import java.util.HashMap;
import java.util.Map;

public class maps {
    public static void main(String[] args) {
        // Very very similar to ArrayLists and Lists
        Map<Integer, String> baseTwo = new HashMap<Integer, String>();
        // or HashMap start

        baseTwo.put(1, "Two");
        baseTwo.put(2, "Four");
        baseTwo.put(2, "Nope"); // replace
        baseTwo.put(3, "Eight");

        System.out.println("Two to the Two is " + baseTwo.get(2));
    }
}
