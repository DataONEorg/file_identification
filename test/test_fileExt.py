import unittest
from pythonFiles.fileExt import getFileExt
from os import walk, listdir


class TestFileExt(unittest.TestCase):

    def setUp(self):
        self.func = getFileExt("examples/")

    def test_eml_200(self):
        for fileName in listdir("examples/eml-200/"):
            self.assertEqual(getFileExt("examples/eml-200/"+fileName), 'formatid="eml://ecoinformatics.org/eml-2.0.0"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_eml_201(self):
        for fileName in listdir("examples/eml-201/"):
            self.assertEqual(getFileExt("examples/eml-201/"+fileName), 'formatid="eml://ecoinformatics.org/eml-2.0.1"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_eml_210(self):
        for fileName in listdir("examples/eml-210/"):
            self.assertEqual(getFileExt("examples/eml-210/"+ fileName), 'formatid="eml://ecoinformatics.org/eml-2.1.0"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_eml_211(self):
        for fileName in listdir("examples/eml-211/"):
            self.assertEqual(getFileExt("examples/eml-211/"+fileName), 'formatid="eml://ecoinformatics.org/eml-2.1.1"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_dryad(self):
        for fileName in listdir("examples/dryad-31/"):
            self.assertEqual(getFileExt("examples/dryad-31/"+fileName), 'formatid="http://datadryad.org/profile/v3.1"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_fgdc1998(self):
        for fileName in listdir("examples/fgdc-1998/"):
            self.assertEqual(getFileExt("examples/fgdc-1998/"+fileName), 'formatid="FGDC-STD-001-1998"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_fgdc1999(self):
        for fileName in listdir("examples/fgdc-1999/"):
            self.assertEqual(getFileExt("examples/fgdc-1999/"+fileName), 'formatid="FGDC-STD-001-1999"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_mercury(self):
        for fileName in listdir("examples/mercury/"):
            self.assertEqual(getFileExt("examples/mercury/"+fileName), 'formatid="http://purl.org/ornl/schema/mercury/terms/v1.0"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_onedcx(self):
        for fileName in listdir("examples/onedcx/"):
            self.assertEqual(getFileExt("examples/onedcx/"+fileName), 'formatid="http://ns.dataone.org/metadata/schema/onedcx/v1.0"', "Incorrect File extension for file: {0}" .format(fileName))


    def test_isotc211(self):
        for fileName in listdir("examples/isotc211/"):
            self.assertEqual(getFileExt("examples/isotc211/"+fileName), 'formatid="http://www.isotc211.org/2005/gmd"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_isotc211_noaa(self):
        for fileName in listdir("examples/isotc211-noaa/"):
            self.assertEqual(getFileExt("examples/isotc211-noaa/"+fileName), 'formatid="http://www.isotc211.org/2005/gmd-noaa"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_isotc211_pangaea(self):
        for fileName in listdir("examples/isotc211-pangaea/"):
            self.assertEqual(getFileExt("examples/isotc211-pangaea/"+fileName), 'formatid="http://www.isotc211.org/2005/gmd-pangaea"', "Incorrect File extension for file: {0}" .format(fileName))

    def test_resourcemap(self):
        for fileName in listdir("examples/resourcemap/"):
            self.assertEqual(getFileExt("examples/resourcemap/"+fileName), 'formatid="http://www.openarchives.org/ore/terms"', "Incorrect File extension for file: {0}" .format(fileName))

if __name__ == '__main__':
    unittest.main()
