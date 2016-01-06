import csv #for reading in file

#splitts the data on the ';'.
class SKV(csv.excel):
    delimiter = ","

csv.register_dialect("SKV", SKV)

def getData(dataFile):
    x = []
    y = []
    with open(dataFile, "rU") as csvfile:
        reader = csv.reader(csvfile, "SKV")
        for row in reader:
            aspects = row
            break
        j = 0
        # for aspect in aspects:
        #     print j, aspect
        #     j += 1
        # j = 0
        # f = open("naam.csv", 'w')

        merken = dict()

        for row in reader:
            

        # for row in reader:
        #     # hole = False
        #     j += 1
        #     i = 0
        #     for aspect in row:
        #         #if aspect == "" and i == 12:# and i == 13 and row[2] != "":
        #         if i == 12:
        #             if aspect in merken:
        #                 merken[aspect] += 1
        #             else:
        #                 merken[aspect] = 1
        #             # if aspect not in merken:
        #                 # merken.append(aspect)
        #                 # print aspect
        #                 #print j, ":", aspects[i]
        #             #print j, row[2]
        #             # hole = True
        #         i += 1
        # print len(merken)
        # for merk in merken:
        #     print merk, merken[merk]
        #print(merken)
            # if not hole:
            #     f.write(str(row))
            #     f.write("\n")
        # f.close()
        # for row in reader:
        #     for aspect in row:
        #         if aspect == ""

            #x.append((map(str, row[0:-1])))
            #y.append(map(int, row[-1]))
            #y.append(map(str, row[-1]))
        #print row[5]
    return (x, y)

if __name__ == '__main__':
    #getData("Voertuig Open Data-KENT_VRTG_O_DAT.csv")
    getData("nieuw.csv")