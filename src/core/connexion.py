import pandas as pd
import os

class Connexion :

    filename_csv: str
    filename_video: str

    def __init__(self, filename_video, filename_csv):
        self.filename_video = filename_video
        self.filename_csv = filename_csv
        self.checkAndLoadPandasFile()
        self.checkAndLoadVideoFile()


    def checkAndLoadPandasFile(self):
        print("Searching the CSV file...")
        if os.path.exists(self.filename_csv) :
            print("File CSV successfully founded")
            print("Loading the CSV file...")
            if self.filename_csv.endswith(".csv"):
                self.data_csv = pd.read_csv(self.filename_csv)
                print("File CSV successfully loaded")
                return
            if self.filename_csv.endswith(".xls") or self.filename_csv.endswith(".xlsx"):
                self.data_csv = pd.read_excel(self.filename_csv)
                print("File EXCEL successfully loaded")
                return
            print("Illegal Format for the CSV file or format not supported")
        else :
            print("Couldn't open " + self.filename_csv + ": no such file or directory")
        exit(1)


    # check if the Video file source exists and if its format is supported
    def checkAndLoadVideoFile(self):
        print("Searching the video file...")
        if os.path.exists(self.filename_video):
            print("Video successfully founded")
            print("Loading the video file...")
            if self.filename_video.endswith(".mp4") or self.filename_video.endswith(".mov") \
                    or self.filename_video.endswith(".wmv") or self.filename_video.endswith(".flv") \
                    or self.filename_video.endswith(".avi") or self.filename_video.endswith(".mkv") \
                    or self.filename_video.endswith(".mpeg") or self.filename_video.endswith(".asf") \
                    or self.filename_video.endswith(".qt") or self.filename_video.endswith(".m4v") :
                print("Video successfully loaded")
                # self.data_video = vd.Video(self.filename_video)
                return
            print("Illegal Format for the video or format not supported")
        else :
            print("Couldn't open " + self.filename_video + ": no such file or directory")
        exit(1)

    # getter for the filename_video and filename_csv file
    def getterFilenames(self):
        return self.filename_video, self.filename_csv, self.data_csv
