public class runCalc {
    public static void main(String[] args) {
        System.out.println(timeToSec("00:05:57") + " seconds"); // 1600m PR
        System.out.println(timePer400for1600("00:05:52") + "s / 400");
    }
    
    public static int timeToSec(String time) { // xx:xx:xx
        int hr = Integer.parseInt(time.substring(0, 2));
        int min = Integer.parseInt(time.substring(3, 5));
        int sec = Integer.parseInt(time.substring(6, 8));
        
        return (hr * 3600) + (min * 60) + sec;
    }
    
    public static double timePer400for1600(String goal1600) {
        int goal1600Secs = timeToSec(goal1600);
        return goal1600Secs / 4.0;
    }
}
