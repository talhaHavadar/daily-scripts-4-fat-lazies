public class SegregateArray {
    /*
    This problem was asked by Google.
    Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs
    come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

    Do this in linear time and in-place.

    For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
     */

    private static void swap(char[] arr, int i, int j) {
        char temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }

    private static void segregateArray(char[] arr) {
        if (arr.length == 0) return;

        int rIndex = 0;
        int bIndex = arr.length - 1;

        for (int i = 0; i <= bIndex; i++) {
            if (arr[i] == 'R' && i != rIndex) {
                swap(arr, rIndex, i);
                rIndex++;
                i--;
            } else if (arr[i] == 'B' && i != bIndex) {
                swap(arr, bIndex, i);
                bIndex--;
                i--;
            }
        }

    }

    public static void solution() {
        char[] arr = new char[] {'R', 'B', 'R', 'R', 'B', 'R', 'G'};
        segregateArray(arr);
        for (char c : arr) {
            System.out.print(c + ", ");
        }
    }
}
