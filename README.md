# Enabling identification of specific metadata formats with command line tools

* [Purpose](#purpose):
  * [File Command](#file-command)
  * [Libmagic](#Libmagic)
  * [DataONE File Formats](#dataone-file-formats)

* [Creating and Using custom magic file](Creating-and-Using-custom-magic-file)
  * [Magic File format](#magic-file-format)
  * [dataone magic file](#dataone-magic-file)
  * [Compiling magic files](#compiling-magic-files)
  * [Using custom magic files:](#using-custom-magic-files:)

* [Installing and Using dataone magic file](#Installing-and-Using-dataone-magic-file:)
  * [On Linux](#linux)
  * [On Mac](#Mac)
* [Unittest](#Unittest)
* [References](#References)


------------------


## Purpose
  The goal of this project is to extend the capabilities of the Linux (or equivalents on OS X and Windows) file command to allow automatic identification of common science metadata and data formats.

  ### File & Libmagic:
  File is part of most Unix/Linux distributions. The `file` identifies the type of the file based on the format signature and not based on file extension. The format signature in case of the file are called as magic numbers which are stored in the magic directory.
  The locations of these files are as:

  * /usr/share/file
  * /etc/magic:/usr/share/misc/


The file uses a compiled version of the magic numbers named as magic.mgc file, and we can also override it using a "-m" option with a custom magic file.
``` shell
file -m dataone.mgc example/eml-200/*
```
  ### DataONE file formats:  
  * https://cn.dataone.org/cn/v2/formats
  * http://ns.dataone.org/metadata/schema/onedcx/v1.0
  * http://datadryad.org/profile/v3.1
  * FGDC-STD-001-1998
  * FGDC-STD-001.1999
  * http://purl.org/ornl/schema/mercury/terms/v1.0
  * http://www.isotc211.org/2005/gmd
  * http://www.isotc211.org/2005/gmd-pangaea
  * http://www.isotc211.org/2005/gmd-noaa
  * eml://ecoinformatics.org/eml-2.1.1
  * eml://ecoinformatics.org/eml-2.1.0
  * eml://ecoinformatics.org/eml-2.0.1
  * eml://ecoinformatics.org/eml-2.0.0
  * http://www.openarchives.org/ore/terms

## Creating and Using custom magic file:

### Magic File format
The magic files consist of multiple lines where each line in the file specifies a test. Each test is made up of 4 items, which are separated by one or more whitespace characters:

  ***offset*** – specifies the offset, in bytes, into the file of the data which is to be tested.
  ***type*** – the type of the data to be tested (see here for a list of all possible values) .
  ***test*** – the value to be compared with the value from the file.
  ***message*** – the message to be printed if the comparison succeeds

  For more details about the  magic source format can be found in [man pages](http://manpages.ubuntu.com/manpages/precise/en/man5/magic.5.html).

### dataone magic file

The [dataone.mgc](https://github.com/DataONEorg/file_identification/blob/master/magic_files/dataONE) file is created for testing 13 different scientific file formats using string and regex . This is a compiled version containing only the magic numbers for the DataONE file formats. Below is a snapshot of the file:

```
0	string <?xml
>&0	regex (eml)-[0-9].[0-9].[0-9]+ eml://ecoinformatics.org/%s
```

In the first line the, a string containing the xml tag is searched, if it matches, than it searches for pattern the (eml)-[0-9].[0-9].[0-9] in the string using regex. If the pattern is found than it prints the message **eml://ecoinformatics.org/%s** followed by the version from the matched pattern.

### Compiling magic files:

```
  file -C -m dataone
```
### Using custom magic files:

```
file -m dataone.mgc example/eml-200/*
```

## Installing and Using magic file:

### On Linux:
The file 3.4 version and above will contain the latest changes but for using the dataone magic file with earlier versions on Linux system, kindly follow the below steps:

1. Clone the [file](https://github.com/file/file) github repository.
2. Remove the earlier magic files from the system using below command
  `sudo apt-get purge libmagic1 file`
3. Follow the below steps for compiling and installing the new magic files.
  * autoconf
  * ./configure make
  * make check -no errors
  * make install
  * make installcheck - no errors

### On Mac :

On Mac, the replacing and compiling of the libmagic file may be tedious. Hence, you may use the below hack for using the dataone magic file on Mac with earlier version of file.
1. Copy the compiled [magic.mgc](https://github.com/DataONEorg/file_identification/blob/master/magic_files/magic.mgc) file to local system.
2. Create an alias as below or use "-m" option.
  ```
   alias blah="file -m magic_files/magic.mgc"
   blah examples/eml-200/*
   examples/eml-200/00_eml-200.xml: eml://ecoinformatics.org/eml-2.0.0
  examples/eml-200/01_eml-200.xml: eml://ecoinformatics.org/eml-2.0.0
  examples/eml-200/03_eml-200.xml: eml://ecoinformatics.org/eml-2.0.0
  ```

  ```
  $ file -m magic_files/magic.mgc examples/eml-200/*
    examples/eml-200/00_eml-200.xml: eml://ecoinformatics.org/eml-2.0.0
    examples/eml-200/01_eml-200.xml: eml://ecoinformatics.org/eml-2.0.0
    examples/eml-200/02_eml-200.xml: eml://ecoinformatics.org/eml-2.0.0
  ```

## Python Unittest:
A unittest is also developed for testing the custom magic file for identifying the correct file types from the examples provided.
This test can be executed after cloning the repository and installing the `filemagic` using the below command.

***$ pip install filemagic ***
***$ python -m unittest discover -v***
The output of the unittest is as below. The test will fail for FGDC-STD-001-1999 as we are still working on that file format.
```

test_dryad (test.test_fileExt.TestFileExt) ... ok
test_eml_200 (test.test_fileExt.TestFileExt) ... ok
test_eml_201 (test.test_fileExt.TestFileExt) ... ok
test_eml_210 (test.test_fileExt.TestFileExt) ... ok
test_eml_211 (test.test_fileExt.TestFileExt) ... ok
test_fgdc1998 (test.test_fileExt.TestFileExt) ... ok
test_fgdc1999 (test.test_fileExt.TestFileExt) ... FAIL
test_isotc211 (test.test_fileExt.TestFileExt) ... ok
test_isotc211_noaa (test.test_fileExt.TestFileExt) ... ok
test_isotc211_pangaea (test.test_fileExt.TestFileExt) ... ok
test_mercury (test.test_fileExt.TestFileExt) ... ok
test_onedcx (test.test_fileExt.TestFileExt) ... ok
test_resourcemap (test.test_fileExt.TestFileExt) ... ok

======================================================================
FAIL: test_fgdc1999 (test.test_fileExt.TestFileExt)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/pratikshrivastava/Desktop/OneDrive - University of Illinois - Urbana/Box/GitHub/DataONE/internship2018/file_identification/test/test_fileExt.py", line 37, in test_fgdc1999
    self.assertEqual(getFileExt("examples/fgdc-1999/"+fileName), 'FGDC-STD-001-1999', "Incorrect File extension for file: {0}" .format(fileName))
AssertionError: 'ASCII text, with very long lines' != 'FGDC-STD-001-1999'
- ASCII text, with very long lines
+ FGDC-STD-001-1999
 : Incorrect File extension for file: 09_fgdc-1999.xml

----------------------------------------------------------------------
Ran 13 tests in 0.221s

FAILED (failures=1)
```


## References:
  * https://github.com/file/file
  * http://openpreservation.org/blog/2012/08/09/magic-editing-and-creation-primer
  * https://linux.die.net/man/1/file
  * https://filemagic.readthedocs.io/en/latest/guide.html
  * http://pythontesting.net/framework/unittest/unittest-introduction/
  * http://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/
