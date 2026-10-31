import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class MetadataBatchProcessing {

    public static void main(String[] args) {
        // Specify the directory containing the original files and metadata files
        String sourceDirectoryPath = "/Users/sohail/Desktop/Naeema";
        String destinationDirectoryPath = "/Users/sohail/Desktop/output";

        try {
            // Get a list of files in the source directory
            File sourceDirectory = new File(sourceDirectoryPath);
            File[] files = sourceDirectory.listFiles();

            // Process each file in the source directory
            for (File file : files) {
                if (file.isFile()) {
                    // Process files of all types

                    // Check if the filename ends with ".json"
                    if (file.getName().toLowerCase().endsWith(".json")) {
                        // Read metadata from the JSON file
                        JSONObject jsonObject = readJsonFile(file);

                        // Get metadata from JSON
                        String metadata = (String) jsonObject.get("metadata");

                        // Determine the corresponding source file name
                        String sourceFileName = file.getName().replace(".json", "");

                        // Find the corresponding source file in the directory
                        File sourceFile = new File(sourceDirectoryPath + File.separator + sourceFileName);

                        // Apply metadata to the source file
                        File destinationFile = new File(destinationDirectoryPath + File.separator + sourceFileName);
                        applyMetadata(sourceFile, destinationFile, metadata);
                    }
                }
            }
        } catch (IOException | ParseException e) {
            e.printStackTrace();
        }
    }

    private static JSONObject readJsonFile(File file) throws IOException, ParseException {
        // Parse JSON content from file
        JSONParser parser = new JSONParser();
        try (FileReader reader = new FileReader(file)) {
            return (JSONObject) parser.parse(reader);
        }
    }

    private static void applyMetadata(File sourceFile, File destinationFile, String metadata) {
        // Apply metadata to the source file and save it to the destination directory
        System.out.println("Applying metadata to file: " + sourceFile.getName());
        // Your logic to apply metadata goes here

        try {
            // Copy the source file to the destination directory
            Files.copy(sourceFile.toPath(), destinationFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("File saved to: " + destinationFile.getAbsolutePath());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
