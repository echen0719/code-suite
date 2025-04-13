public class runCalc {
    public static void main(String[] args) {
        System.out.println("PR in 1600m: " + timeToSec("00:05:57") + " seconds"); // current 1600m PR
        System.out.println("\n5:52 1600m calcs: ");
        System.out.println(timePer400For1600("00:05:52") + "s / 400"+ " OR " + secToTime(timePer400For1600("00:05:52")) + " / 400");
        System.out.println(timePer800For1600("00:05:52") + "s / 800"+ " OR " + secToTime(timePer800For1600("00:05:52")) + " / 800");
        System.out.println("\n21:30 5K calcs: ");
        System.out.println(timePer1000For5000("00:21:30") + " / 1000");
        System.out.println(timePerMileFor5000("00:21:30") + " / mile");
    }
    
    public static int timeToSec(String time) { // xx:xx:xx
        int hr = Integer.parseInt(time.substring(0, 2));
        int min = Integer.parseInt(time.substring(3, 5));
        int sec = Integer.parseInt(time.substring(6, 8));
        
        return (hr * 3600) + (min * 60) + sec;
    }
    
    public static String secToTime(double sec) { // xx:xx:xx
        int hr = (int) sec / 3600;
        int min = (int) (sec % 3600) / 60;
        int secInt = (int) (sec % 60);
        
        return String.format("%02d:%02d:%02d", hr, min, secInt);
        // seems .format works well for this
    }
    
    public static double timePer400For1600(String goal1600) {
        int goal1600Secs = timeToSec(goal1600);
        return goal1600Secs / 4.0;
    }
    
    public static double timePer800For1600(String goal1600) {
        int goal1600Secs = timeToSec(goal1600);
        return goal1600Secs / 2.0;
    }
    
    // I don't think people want seconds for 1K or mile
    public static String timePer1000For5000(String goal5000) {
        int goal5000Secs = timeToSec(goal5000);
        return secToTime(goal5000Secs / 5.0);
    }
    
    // I think using colon time format is good enough
    public static String timePerMileFor5000(String goal5000) {
        int goal5000Secs = timeToSec(goal5000);
        return secToTime(goal5000Secs / 3.107);
    }
}
