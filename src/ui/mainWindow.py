from src.core import video as vd
from src.core import label as ls
from src.ui.assets import videoUI as vdUI
from src.ui.assets import signalUI as sgUI
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec

class MainWindow:

    np.random.seed(19680801)

    def __init__(self, signals_selected=None, filename_video="C:/Users/cmartin-/Desktop/app-pycharm-edition/MobEyeQ3.avi", labels_entered=None):
        self.signals_selected = signals_selected
        #self.video = vd.Video(filename_video)
        self.graphic_video = vdUI.VideoUI(None, filename_video)
        self.labels_entered = labels_entered
        self.window = Tk()
        self.initWindow()
        self.loadAndPlaceMainLabels()

        self.loadAndPlaceSubLabelsHeader()
        self.__loadAndPlaceLabelFramesAndTime()

        self.loadAndPlaceSubLabelsBody()
        self.window.mainloop()


    def initWindow(self):
        self.window.title("Video app 1.0")
        self.window.state('zoomed')
        self.window.config(background="white")
        self.window.geometry("960x540")
        self.__loadIconWindow("src/ui/.images/icon.png")


    # Import an images and put it as icon window
    def __loadIconWindow(self, filePath):
        p1 = PhotoImage(file=filePath)
        self.window.iconphoto(False, p1)


    # Load header label
    def __loadHeader(self):
        self.header = Label(
            self.window,
            bg="black"
        )
        self.header.place(x=0, y=0, relwidth=1, relheight=.65)


    # Load body label
    def __loadBody(self):
        self.body = Label(
            self.window,
            bg="blue"
        )
        self.body.place(relx=0, rely=.65, relwidth=1, relheight=.35)


    # Load and place the main labels (header and body labels)
    def loadAndPlaceMainLabels(self):
        self.__loadHeader()
        self.__loadBody()


    def __loadSubLabelsHeader(self):
        self.video_label = Label(
            self.header,
            bg="yellow"
        )
        self.video_label.place(relx=0, rely=0, relheight=1, relwidth=.65)
        self.labels_label = Label(
            self.header,
            bg="green"
        )
        self.labels_label.place(relx=.65, rely=0, relheight=1, relwidth=.35)


    def loadAndPlaceSubLabelsHeader(self):
        self.__loadSubLabelsHeader()
        self.__loadAndPlaceVideoCanvas()
        self.__loadAndPlaceLabelsCanvas()


    def __loadAndPlaceVideoCanvas(self):
        self.video_canvas = Canvas(
            self.video_label,
            bg="white"
        )
        self.video_canvas.place(relx=0.05, rely=0.05, relwidth=0.905, relheight=0.9)


    def __loadAndPlaceLabelsCanvas(self):
        self.video_info = Label(
            self.labels_label,
            bg="brown"
        )
        self.video_info.place(relx=.05, rely=.05, relwidth=.905, relheight=.15)
        self.labels_canvas = Label(
            self.labels_label,
            bg="brown"
        )
        self.labels_canvas.place(relx=.05, rely=.25, relwidth=.905, relheight=.5)
        self.buttons_canvas = Label(
            self.labels_label,
            bg="brown"
        )
        self.buttons_canvas.place(relx=.05, rely=.8, relwidth=.905, relheight=.15)


    def loadAndPlaceSubLabelsBody (self) :
        self.__loadSignalsLabel()
        self.__loadSignalsScrollBar()
        self.__loadLabelsLabel()
        self.__loadScrollBarLabels()


    def __loadSignalsLabel (self) :
        self.signals_label = Label(
            self.body,
            bg="pink"
        )
        self.signals_label.place(relx=0, rely=0, relwidth=.98, relheight=1)
        self.sub_canvas = Canvas(
            self.signals_label,
            bg="light blue",
            highlightbackground="white"
        )
        self.sub_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.scrollbar_label = Label(
            self.body,
        )
        self.scrollbar_label.place(relx=.98, rely=0, relwidth=.02, relheight=1)


    def __loadSignalsScrollBar (self):
        self.scrollbar_signals = Scrollbar (
            self.scrollbar_label,
            orient=VERTICAL,
            command=self.sub_canvas.yview
        )
        self.sub_canvas.update()
        print(self.sub_canvas.winfo_width())
        self.scrollbar_signals.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.__configSubBodyWidget()
        self.second_frame = Frame(
            self.sub_canvas, bg="white", 
            height=350,
            highlightbackground="white",
            width=self.sub_canvas.winfo_width()
        )
        self.second_frame.place(relx=0, rely=0, relwidth=1)
        self.sub_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")


    #Config for the scrollbar
    def __configSubBodyWidget(self):
        self.sub_canvas.configure(yscrollcommand=self.scrollbar_signals.set)
        self.sub_canvas.bind('<Configure>', lambda e: self.sub_canvas.configure(scrollregion=self.sub_canvas.bbox("all")))


    def __loadLabelsLabel (self) :
        self.labels_label = Label(
            self.labels_canvas,
            bg="light blue"
        )
        self.labels_label.place(relx=0, rely=0, relwidth=.95, relheight=1)
        self.subLabels_canvas = Canvas (
            self.labels_label,
            bg="light blue",
            highlightbackground="white"
        )
        self.subLabels_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.scrollbarLabels_label = Label (
            self.labels_canvas,
            bg="light blue"
        )
        self.scrollbarLabels_label.place(relx=.95, rely=0, relwidth=.05, relheight=1)


    def __loadScrollBarLabels (self) :
        self.scrollbar_label = Scrollbar(
            self.scrollbarLabels_label,
            orient="vertical",
            command=self.subLabels_canvas.yview
        )
        self.scrollbar_label.place(relx=0, rely=0, relwidth=1, relheight=1)


    def __loadAndPlaceLabelFramesAndTime (self) :
        self.frame = Label (
            self.video_info,
            text="Total Frames: " + str(self.graphic_video.getTotalNumberFrames()),
            bg="blue"
        )
        self.frame.place(relx=0, rely=0, relwidth=.5, relheight=1)
        self.timer = Label (
            self.video_info,
            bg="black"
        )
        self.timer.place(relx=0.5, rely=0, relwidth=.5, relheight=1)


    def __loadBlockLabelForLabel (self, label) :
        label_grap = Label (
            self.labels_l
        )

    

