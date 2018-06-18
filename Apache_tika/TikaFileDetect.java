/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package check_mime;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import org.apache.tika.Tika;
import org.apache.tika.mime.MimeTypes;


public class TikaFileDetect {

    private final Tika tika = new Tika();

    public TikaFileDetect() {
        super();
    }

    public String probeContentType(Path path) throws IOException {

        // Check contents first
        String fileContentDetect = tika.detect(path.toFile());
        if (!fileContentDetect.equals(MimeTypes.OCTET_STREAM)) {
            return fileContentDetect;
        }

        // Try file name only if content search was not successful
        String fileNameDetect = tika.detect(path.toString());
        if (!fileNameDetect.equals(MimeTypes.OCTET_STREAM)) {
            return fileNameDetect;
        }

        return null;
    }

    public static void main(String[] args) throws IOException {

        Tika tika = new Tika();

        if (args.length != 1) {
            printUsage();
            return;
        }
        Path path = Paths.get(args[0]);

        TikaFileTypeDetector detector = new TikaFileTypeDetector();

        String contentType = detector.probeContentType(path);

        System.out.println("File is of type - " + contentType);
    }

    public static void printUsage() {
        System.out.print("Usage: java -classpath ... "
                + TikaFileTypeDetector.class.getName()
                + " ");
    }
}
