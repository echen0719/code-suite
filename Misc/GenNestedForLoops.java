public class GenNestedForLoops {
    public static void main(String[] args) {
        System.out.println(generateNestedForLoops(10, 10));
    }

    public static String generateNestedForLoops(int n, int x) {
        String nests = "long count = 0;\n\n";

        for (int i = 1; i <= n; i++) {
            nests += "for (int i" + i + " = 0; i" + i + " < " + x + "; i" + i + "++) {\n";
        }

        nests += "count++;\n";

        for (int i = 0; i < n; i++) {
            nests += "}\n";
        }
        
        return nests;
    }
}
