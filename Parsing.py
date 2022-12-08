import Prepocessing

def parseAll(file) :
    file = open(file)

    pre_line = ""
    abstracts = []
    abstract_temp = ""
    for line in file:
      if pre_line == ".W\n" and line != ".X\n":
        abstract_temp += line.replace("\n", " ")
        continue
      elif line == ".X\n":
        abstracts.append(abstract_temp)
        abstract_temp = ""
      pre_line = line
    file.close()
    return abstracts


def parseQueries(file):
    file = open(file)
    abstracts = []
    pre_line = ""
    abstract_temp = ""
    for line in file:
      if pre_line == ".W\n" and not line.startswith(".I "):
        abstract_temp += line.replace("\n", " ")
        continue
      elif line.startswith(".I ") and len(pre_line) > 0:
        abstracts.append(abstract_temp)
        abstract_temp = ""
      pre_line = line
    else:
      if len(abstract_temp) > 0:
        abstracts.append(abstract_temp)
    file.close()
    return abstracts

