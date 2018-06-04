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

NUM_DOCS = 10  #Number of examples to retrieve
CN_BASEURL = "https://cn.dataone.org/cn/v2"

def getDocument(fn_dest, pid):
  '''
  '''
  url = CN_BASEURL + "/object/" + quote(pid)
  logging.debug("Downloading: %s", url)
  request = requests.get(url)
  if request.status_code == 200:
    logging.debug("Writing to file %s", fn_dest)
    with open(fn_dest, "wb") as f_dest:
      f_dest.write(request.content)
      return True
  return False


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
    cmd = ["d1listobjects", "-I", "-C", "100", "-F", formatid]
    try:
      pids = subprocess.check_output(cmd).decode().split("\n")
      identifiers = []
      counter = 0
      for pid in pids:
        logging.info("pid: %s", pid)
        pid = pid.strip()
        if len(pid) > 2:
          filename = "{:02d}_{}.xml".format(counter, folder)
          fn_dest = os.path.join(folder, filename)
          if getDocument(fn_dest, pid):
            entry = {"pid": pid,
                     "filename": filename}
            identifiers.append(entry)
            counter +=1
        if counter >= NUM_DOCS:
          break
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
    counter = 0
    for identifier in example["identifiers"]:
      filename = "{:02d}_{}.xml".format(counter, folder)
      dest_fn = os.path.join(folder, filename)
      url = CN_BASEURL + "/object/" + quote(identifier["pid"])
      logging.debug("Downloading: %s", url)
      request = requests.get(url)
      if request.status_code == 200:
        logging.debug("Writing to file %s", dest_fn)
        with open(dest_fn, "w", encoding="utf-8") as f_dest:
          f_dest.write(request.text)
          identifier["filename"] = filename
          counter += 1
      if counter >= NUM_DOCS:
        break
    #clean up unused identifiers
    identifiers_used = []
    for identifier in example["identifiers"]:
      if "filename" in identifier:
        identifiers_used.append(identifier)
    example["identifiers"] = identifiers_used


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
  #getExamples(catalog)


if __name__ == "__main__":
  main()
