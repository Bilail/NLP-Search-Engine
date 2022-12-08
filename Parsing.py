import Prepocessing

def parseAll(file) :
    file = open(file)

    indexes = []
    titles = []
    authors = []
    abstracts = []
    references = []
    pre_line = ""
    authors_temp = []
    abstract_temp = ""
    for line in file:
      if pre_line == ".T\n":
        titles.append(line.replace("\n", ""))
      elif pre_line == ".W\n" and line != ".X\n":
        abstract_temp += line.replace("\n", " ")
        continue
      elif line == ".X\n":
        abstracts.append(Prepocessing.clean_sentence(abstract_temp))
        abstract_temp = ""
      pre_line = line
    file.close()
    return titles, abstracts


def parseQueries(file) :
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

