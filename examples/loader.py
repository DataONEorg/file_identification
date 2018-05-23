'''
Script to load metadata exampels from DataONE

Depends on availability of DataONE operations tools.
'''

import logging
import yaml
import subprocess
import os
import requests
from urllib.parse import quote

NUM_DOCS = 5  #Number of examples to retrieve
CN_BASEURL = "https://cn.dataone.org/cn/v2"


def getIdentifiers(catalog):
  '''
  Get a few identifiers for each type of metadata.

  Modifies the provided catalog object in-place.
  '''
  for example in catalog['examples']:
    formatid = example["formatId"]
    folder = example["folder"]
    logging.debug("Getting identifiers for formatId %s", formatid)
    if formatid.startswith("-"):
      formatid = "\\" + formatid
    cmd = ["d1listobjects", "-I", "-C", str(NUM_DOCS), "-F", formatid]
    try:
      pids = subprocess.check_output(cmd).decode().split("\n")
      identifiers = []
      counter = 0
      for pid in pids:
        logging.info("pid: %s", pid)
        pid = pid.strip()
        if len(pid) > 2:
          entry = {"pid": pid,
                   "filename": "{:02d}_{}.xml".format(counter, folder)}
          identifiers.append(entry)
          counter +=1 
      example["identifiers"] = identifiers
    except subprocess.CalledProcessError as e:
      logging.error(e)


def getExamples(catalog):
  '''Load the XML documents from the CNs

  Files are saved as specified in the catalog.
  '''
  for example in catalog['examples']:
    formatid = example["formatId"]
    folder = example["folder"]
    if not os.path.exists(folder):
      os.mkdir(folder)
    for identifier in example["identifiers"]:
      dest_fn = os.path.join(folder, identifier["filename"])
      url = CN_BASEURL + "/object/" + quote(identifier["pid"])
      logging.debug("Downloading: %s", url)
      request = requests.get(url)
      logging.debug("Writing to file %s", dest_fn)
      with open(dest_fn, "w", encoding="utf-8") as f_dest:
        f_dest.write(request.text)


def main():
  logging.basicConfig(level=logging.DEBUG)
  catalog_name = "catalog.yaml"
  yaml_text = open(catalog_name, "r").read()
  catalog = yaml.load(yaml_text)
  # Load the set of identifiers for each type of metadata
  getIdentifiers(catalog)
  # save the updated catalog to disk
  with open(catalog_name,"w") as yaml_file:
    yaml.dump(catalog, yaml_file, default_flow_style=False)
  # load the XML metadata documents
  getExamples(catalog)


if __name__ == "__main__":
  main()
