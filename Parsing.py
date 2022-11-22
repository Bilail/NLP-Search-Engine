


def parsing(file) :
    file = open(file)

    indexes = []
    titles = []
    authors = []
    abstracts = []
    references = []

    pre_line = ""
    authors_temp = []
    abstract_temp = ""

    """for i in range(len(file)):
        if line == ".I\n":
            while (file)"""

    for line in file:
      if pre_line == ".T\n":
        titles.append(line.replace("\n", ""))
      elif pre_line == ".W\n" and line != ".X\n":
        abstract_temp += line.replace("\n", " ")
        continue
      elif line == ".X\n":
        abstracts.append(abstract_temp)
        abstract_temp = ""
      pre_line = line

    file.close()

    return titles, abstracts

