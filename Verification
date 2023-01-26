import java.awt.*;
import java.io.*;
import java.net.*;
import java.util.*;
import java.util.List;

public class Verification {

    private static String coreURL;
    private static String extensionURL;
    private static String filePath;
    private static List<URL> urlList = new ArrayList<>();

    /**
     * Parses the IDs and sends them to be processed
     *
     * @param file = input file of IDs submitted by the user
     * @throws Exception
     */
    public static void parse(String file) throws Exception {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(file)))) {
            String id;
            while ((id = br.readLine()) != null) {
                process(id);
            }
        }

    }

    /**
     * Gets each ID from the file and converts the string to a URL
     *
     * @param id = User ID to be verified
     * @throws MalformedURLException
     */
    public static void process(String id) throws MalformedURLException {
        String[] urls = id.split("\n");
        for (String url : urls) {
            url = coreURL + url + extensionURL;
            URL newUrl = new URL(url);
            addUrlToList(newUrl);
        }
    }

    /**
     * Adds the URL to the <b><urlList/b> ArrayList
     *
     * @param url = URL created from <i>process</i> method
     */
    public static void addUrlToList(URL url) {
        urlList.add(url);
    }

    /**
     * Sends GET request for each URL in <b>urlList</b> array
     * Gets response from request
     *
     * @throws IOException
     */
    public static void sendGetRequest(List<URL> list) throws IOException {
        for (URL url : list) {
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");
            int responseCode = con.getResponseCode();
            if ((responseCode > 0) && (responseCode < 299)) {
                System.out.println("Success");
                System.out.println("User: " + url + " Response: " + responseCode);
            } else if ((responseCode > 300) && (responseCode < 399)) {
                System.out.println("Likely success");
                System.out.println("User: " + url + " Response: " + responseCode);
            } else if ((responseCode > 400) && (responseCode < 499)) {
                System.out.println("Likely failure");
                System.out.println("User: " + url + " Response: " + responseCode);
            } else
                System.out.println("User: " + url + " Response: " + responseCode);
        }
    }

    public static void openInBrowser(List<URL> list) throws URISyntaxException, IOException {
        for (URL url : list) {
            Desktop desk = Desktop.getDesktop();
            desk.browse(new URI(url.toString()));
        }
    }

    public static void main(String[] args) throws Exception {
        new Verification().parse(filePath);
        openInBrowser(urlList);
        //sendGetRequest(urlList);
        /**
         * Getting 200 ok, should be getting 302.
         * Need to figure out auth
         */
    }
}
