import java.util.*;

public class sort {
    private static final int[] unsort = {18, 39, 12, 28, 17, 19, 1, 44, 31, 7, 49, 23, 40, 34, 30, 29, 25, 3, 47, 43, 27, 6, 38, 48, 21, 9, 32, 4, 11, 26, 15, 20};
    public static void main(String[] args) {
        for (int i : selectMin()) {
            System.out.print(i + " ");
        }
    }

    public static int[] selectMin() {
        int[] sort = unsort;
        for (int i = 0; i < sort.length - 1; i++) {
            int min = i;
            for (int j = i + 1; j < sort.length; j++) {
                if (sort[j] < sort[min])
                    min = j;
            }
            int temp = sort[min];
            sort[min] = sort[i];
            sort[i] = temp;
        }
        return sort;
    }
}