import java.util.Arrays;

public class binSearch {
    public static void main(String[] args) {
        int[] array = {18, 39, 12, 28, 17, 19, 1, 44, 31, 7, 49, 23, 40, 34, 30, 29, 25, 3, 47, 43, 27, 6, 38, 48, 21, 9, 32, 4, 11, 26, 15, 20};
        Arrays.sort(array);
        for (int i = 0; i < array.length; i++) {
            int hi = binSearch(array, array[i]);
            System.out.println(hi + 1 + ". " + array[hi]);
        }
    }

    public static int binSearch(int[] array, int target) {
        int start = 0;
        int end = array.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (array[mid] == target) {
                return mid;
            }
            else if (array[mid] < target) {
                start = mid + 1;
            }
            else {
                end = mid - 1;
            }
        }
        return -1;
    }
}