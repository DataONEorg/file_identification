# Enabling identification of specific metadata formats with command line tools

## Using Apache Tika for identifying the DataONE file formats

* [Purpose](#purpose):
* [Apache Tika](#apache-tika)
* [Installing and Executing Tika](#installing-and-executing-tika)
  * [Building Tika using maven](#building-tika-using-maven)
  * [Executing Tika CLI](#executing-tika-cli)
* [Creation of Custom-mimetypes](#creation-of-custom-mimetypes)
  * [Custom Mimetypes XML file](#custom-mimetypes-xml-file)
  * [Compiling the custom mimetypes](#compiling-the-custom-mimetypes)
* [Using Custom Mimetypes for File Detection](#using-custom-mimetypes-for-file-detection)
* [Installing and Using dataone magic file](#installing-and-using-dataone-magic-file)

* [References](#References)


------------------


## Purpose:

This readme describe how we can use Apache Tika, for determining the different DataONE file formats by reading the metadata for the files.

This is in continuation with the magic file developed for the `file` command for identifying the DataONE file formats.


## [Apache Tika](https://tika.apache.org/index.html):
The Apache Tika™ toolkit detects and extracts metadata and text from over a thousand different file types (such as PPT, XLS, and PDF). All of these file types can be parsed through a single interface, making Tika useful for search engine indexing, content analysis, translation, and much more

* [Content Detection](https://tika.apache.org/1.1/detection.html) with Apache Tika
* https://www.tutorialspoint.com/tika/tika_architecture.htm
* http://brewformulas.org/Tika

#### Extraction supported by Tika:
1. Document
2. Content
3. Language
4. Metadata


## Installing and Executing Tika:
The source and jar file for the apache tika can be downloaded using the below location for Ubuntu system.
- [apache tika-1.18  src](http://www.apache.org/dyn/closer.cgi/tika/tika-1.18-src.zip)
- [tika-app_1.18.jar ](http://www.apache.org/dyn/closer.cgi/tika/tika-app-1.18.jar)

###  Building Tika using maven:
- installed mvn using `sudo apt-get install maven`
- compiled files using `mvn compile `
- build tika using `mvn install`

The jar files for local build we will created in the ' target ' folder for the respective projects.
For ex:
* The `tika-core-1.18.jar` will be `tika/tika-1.18/tika-core/target` and for the `tika-app-1.18.jar` will be `tika/tika-1.18/tika-app/target`.

### Executing Tika CLI

* Use the below command for executing tika-app from command line. It list the default mime types supported by Tika.

  `java -classpath tika-app-1.18.jar org.apache.tika.cli.TikaCLI --list-supported-types`

* Detecting Mime type of a Readme file using Tika.
  ```shell
  $ java -classpath target/tika-app-1.18.jar org.apache.tika.cli.TikaCLI -d ~/github_repos/file_identification/examples/README.md

  text/x-web-markdown
  ```

## Creation of Custom-mimetypes

Tika provides the ability to users for creating their own mimetypes for the new file formats. The default mimetypes of tika are stored in an xml at [`org/apache/tika/mime/tika-mimetypes.xml`](https://github.com/apache/tika/blob/master/tika-core/src/main/resources/org/apache/tika/mime/tika-mimetypes.xml)

### Custom Mimetypes XML file:
The custom mimetypes for new file formats needs to be defined in the custom-mimetypes.xml file.It is stored in the package ***"org.apache.tika.mime"*** The custom-mimetypes.xml file allows the users to use the  `<glob>` and `<magic>` tags for identification of the files. The `<glob>` pattern uses the file extension i.e. the characters after the '.' in the filename for identifying and assigning the mime types. The `<magic>` tags works just like the magic numbers of the `file command `. Below is the snippet of the [custom-mimetypes.xml](https://github.com/DataONEorg/file_identification/blob/master/Apache_tika/org/apache/tika/mime/custom-mimetypes.xml)


```shell

<?xml version="1.0" encoding="UTF-8"?>
<mime-info>
 <mime-type type="text/xml;formatid=eml://ecoinformatics.org/eml-2.0.0">
  <comment>Example file type </comment>
    <magic priority="60">
      <match value="eml://ecoinformatics.org/eml-2.0.0" type="string" offset="50:4096"/>
    </magic>
  </mime-type>
<mime-info>

```
### Compiling the custom mimetypes:
The [custom-mimetypes.xml](ttps://github.com/DataONEorg/file_identification/blob/master/Apache_tika/org/apache/tika/mime/custom-mimetypes.xml) file needs to be compiled as jar and included in the class path for using with Tika.
The below command generates the [custom-mimetypes.jar](https://github.com/DataONEorg/file_identification/blob/master/Apache_tika/custom-mimetypes.jar)
  `jar cf custom-mimetypes.jar org/apache/tika/mime/custom-mimetypes.xml`

## Using Custom Mimetypes for File Detection:

Once we have the custom-mimetypes.jar file, we can include it in the classpath as below and can use it for detecting the mimetypes.


```shell
$ java -cp tika-app-1.18.jar:custom-mimetypes.jar org.apache.tika.cli.TikaCLI -d ../examples/eml-211/00_eml-211.xml

text/xml; formatid="eml\:\/\/ecoinformatics.org\/eml-2.1.1"
```
