#!/usr/bin/python

import sys
import os
import os.path
from os import path

class NoteAuto:
    fileName = ""
    pathFile = ""

    def createFile(self, filename):
        self.fileName = filename
        self.fileName = self.fileName + ".txt"
        self.pathFile = "/Users/ketterling/Documents/Notizen/" + self.fileName

        exists = os.path.isfile(self.pathFile)

        if exists:
            print("file exists")

        else:
            f = open(self.pathFile, "w")

        os.system("open " + self.pathFile)

if __name__ == "__main__":

    note = NoteAuto()

    filename = str(sys.argv[1])
    note.createFile(filename)
