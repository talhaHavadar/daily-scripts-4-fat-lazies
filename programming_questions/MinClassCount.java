import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MinClassCount {
    /*
    This problem was asked by Snapchat.

    Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
    find the minimum number of rooms required.

    For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
    * */

    public static int minClassRoom(List<int[]> schedule) {
        if (schedule.size() == 0) return 0;
        if (schedule.size() == 1) return 1;

        Collections.sort(schedule, (int[] o1, int[] o2) -> o1[0] - o2[0]);

        int classCount = 1;
        int end = schedule.get(0)[1];
        for (int i = 1; i < schedule.size(); i++) {
            int currStart = schedule.get(i)[0];
            int currEnd = schedule.get(i)[1];
            if (currStart < end) {
                classCount++;
            }
            if (currEnd < end) {
                end = currEnd;
            }
        }

        return classCount;
    }

    public static void main(String[] args) {
        List<int[]> sch = new ArrayList<>();
        sch.add(new int[] {30, 75});
        sch.add(new int[] {0, 70});
        sch.add(new int[] {60, 150});
        System.out.println("Count: " + minClassRoom(sch));
    }
}
