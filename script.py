import glob
import os
from pydicom.filereader import dcmread

path_my = os.getcwd()
directory = 'src'

for path in glob.iglob(f'{directory}/*.dcm'):

    dataset = dcmread(path)
    first_lay = str(dataset.StudyInstanceUID)
    second_lay = str(dataset.SeriesInstanceUID)
    abspath = path_my + "/" + first_lay + "/" + second_lay
    name = str(dataset.SOPInstanceUID)

    if not os.path.exists(abspath):
        os.makedirs(abspath)

    if hasattr(dataset, "PatientName"):
        dataset.PatientName = "anonymous"
    else:
        print("This file", path, "has no Attribute PatientName")

    dataset.save_as(abspath + "/" + name + ".dcm")

    with open("all_path.txt", "a+") as file:
        file.write(path + " => " + first_lay + "/" + second_lay + "/" + name + ".dcm \n")
