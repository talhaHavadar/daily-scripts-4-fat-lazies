import java.util.ArrayList;

public class RunningMedian {

    /* Space and time O(1) */
    private static double getMedian(ArrayList<Integer> list) {
        if (list.size() == 0) return -1;
        int midIndex = list.size() / 2;
        if (list.size() % 2 == 0) {
            return (list.get(midIndex) + list.get(midIndex - 1)) / 2.0;
        }
        return list.get(midIndex);
    }

    
    /*
        Max. size of the list will be 3
        So we can assume time complexity is O(1) for this function
        Since we are also doing the changes inplace space complexity will be O(1)
    * */
    private static void updateMedianList(ArrayList<Integer> list, int newNumber) {

        double currMedian = getMedian(list);
        int midIndex = list.size() / 2;
        if (newNumber >= currMedian)
        {
            for (int i = midIndex; i < list.size(); i++) {
                int n = list.get(i);
                if (n >= newNumber) {
                    list.add(i, newNumber);
                    break;
                } else if (i == list.size() - 1) {
                    list.add(newNumber);
                    break;
                }
            }
            if (list.size() > 3) {
                list.remove(0);
            }
        } else {
            for (int i = midIndex; i >= 0; i--) {
                int n = list.get(i);
                if (n <= newNumber) {
                    list.add(i, newNumber);
                    break;
                } else if (i == 0) {
                    list.add(i, newNumber);
                    break;
                }
            }
            if (list.size() > 3) {
                list.remove(list.size() - 1);
            }
        }

    }

    /* Time complexity is O(n) and n is length of the arr/stream. Space also O(1) */
    private static void runningMedian(int[] arr) {

        if (arr.length == 0) return;

        ArrayList<Integer> medianList = new ArrayList<>();

        medianList.add(arr[0]);

        System.out.println(getMedian(medianList)); /* O(1) */
        int currentSize = 1;

        for (int i = 1; i < arr.length; i++) {
            currentSize++;
            int newNumber = arr[i];
            double lastMedian = getMedian(medianList); /* O(1) */
            updateMedianList(medianList, newNumber); /* O(1) */

            if (currentSize % 2 == 0) {
                if (medianList.size() < 3) {
                    System.out.println(getMedian(medianList)); /* O(1) */
                } else {
                    System.out.println((lastMedian + getMedian(medianList)) / 2.0); /* O(1) */
                }
            } else {
                System.out.println(getMedian(medianList)); /* O(1) */
            }

        }
    }

    public static void solution() {
        runningMedian(new int[] {2,1,5,7,2,0,5});
    }

}
