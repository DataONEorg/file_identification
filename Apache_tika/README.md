# Enabling identification of specific metadata formats with command line tools

## Using Apache Tika for identifying the DataONE file formats

* [Purpose](#purpose):
* [Apache Tika](#apache-tika)
* [Installing Executing Tika](#creating-and-using-custom-magic-file)
  * [Building Tika using maven](#Building-tika-using-maven)
  * [Executing Tika CLI](#executing-tika-cli)
* [Creation of Custom-mimetypes](#creation-of-custom-mimetypes)
  * [Custom-mimetypes.xml](#custom-mimetypes.xml)
  * [Compiling the custom-mimetypes.xml file](#compiling-the-custom-mimetypes.xml-file)
* [Using Custom Mimetypes for File Detection](#using-custom-mimetypes-for-file-detection)
* [Installing and Using dataone magic file](#installing-and-using-dataone-magic-file)

* [References](#References)


------------------


## Purpose

This readme describe how we can use Apache Tika, for determining the different DataONE file formats by reading the metadata for the files.

This is in continuation with the magic file developed for the `file` command for identifying the DataONE file formats.


## Apache Tika


## Installing Executing Tika
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

## [Creation of Custom-mimetypes](#creation-of-custom-mimetypes)

Tika provides the ability to users for creating their own mimetypes for the new file formats. The default mimetypes of tika are stored in an xml at [`org/apache/tika/mime/tika-mimetypes.xml`](https://github.com/apache/tika/blob/master/tika-core/src/main/resources/org/apache/tika/mime/tika-mimetypes.xml)

### Custom-mimetypes.xml
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
### Compiling the custom-mimetypes.xml file.
The [custom-mimetypes.xml](ttps://github.com/DataONEorg/file_identification/blob/master/Apache_tika/org/apache/tika/mime/custom-mimetypes.xml) file needs to be compiled as jar and included in the class path for using with Tika.
The below command generates the [custom-mimetypes.jar]()
  `jar cf custom-mimetypes.jar org/apache/tika/mime/custom-mimetypes.xml`

## Using Custom Mimetypes for File Detection

` java -cp tika-app-1.18.jar: org.apache.tika.cli.TikaCLI -d ../examples/*/*`




## References:
  * https://github.com/file/file
  * http://openpreservation.org/blog/2012/08/09/magic-editing-and-creation-primer
  * https://linux.die.net/man/1/file
  * https://filemagic.readthedocs.io/en/latest/guide.html
  * http://pythontesting.net/framework/unittest/unittest-introduction/
  * http://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/
