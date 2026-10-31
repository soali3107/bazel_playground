import java.time.LocalDate;
import java.time.temporal.WeekFields;
import java.util.Locale;

public class WeekInfo {
    public static void main(String[] args) {
        // Get current date
        LocalDate today = LocalDate.now();

        // Define week fields with Sunday as the first day of the week
        WeekFields weekFields = WeekFields.of(Locale.getDefault()); // Default locale (can be changed)
        
        // Get the week number
        int weekOfYear = today.get(weekFields.weekOfYear());

        // Find the total number of weeks in the current year
        LocalDate lastDayOfYear = LocalDate.of(today.getYear(), 12, 31);
        int totalWeeks = lastDayOfYear.get(weekFields.weekOfYear());

        // Print results
        System.out.println("Today: " + today);
        System.out.println("Week of the year: " + weekOfYear);
        System.out.println("Total weeks in the year: " + (totalWeeks - 1));
    }
}
