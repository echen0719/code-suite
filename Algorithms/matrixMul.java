public class matrixMul {
    public static void main(String[] args) {
        int[][] arr1 = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12} };
        int[][] arr2 = { {2, 4}, {6, 8}, {1, 3} };

        if (arr1[0].length != arr2.length) {
            System.out.println("Matrices cannot be multiplied");
            System.exit(0);
        }

        // new matrix has arr1's row length and arr2's column length
        int[][] arr3 = new int[arr1.length][arr2[0].length];

        // https://www.geeksforgeeks.org/java-program-to-multiply-two-matrices-of-any-size/
        for (int r = 0; r < arr1.length; r++) {
            for (int c = 0; c < arr2[0].length; c++) {
                for (int i = 0; i < arr1[0].length; i++) {
                    arr3[r][c] += arr1[r][i] * arr2[i][c];
                }
            }
        }

        for (int i = 0; i < arr3.length; i++) {
            for (int j = 0; j < arr3[0].length; j++) {
                System.out.print(arr3[i][j] + " ");
            }
            System.out.println();
        }
    }
}