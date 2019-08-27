import pandas as pd
import os
import re

column_names = ["Name", "RandomForest", "MLPClassifier", "DTExtract", "DTExtract Relative", "DTTrained", "CORELS", "CORELSRELRF", "CORELRELMLP", "sklearn-expertsys", "sklearn-expertsys-relrf", "sklearn-expertsys-relmlp"]

def readlogs():
    df = pd.DataFrame(columns=column_names, index=None)

    cwd = os.getcwd()

    #Need to change this around if you want to read the logs into a csv
    corel_logs = os.path.join(cwd, 'corelsrel')
    dtextract_logs = os.path.join(cwd, 'dtextractrelmlp')
    expertsys_logs = os.path.join(cwd, 'expertsysrel')

    for filename in os.listdir(dtextract_logs):
        searchfile = open(dtextract_logs + '/' + filename, 'r')
        dict = {"Name": filename}
        for line in searchfile:
            if "Averaged over 10 trials: " in line:
                if "test" in line.lower():
                    print line
                    score = re.findall('\d*\.?\d+', line)[1]

                    if "rf" in line.lower():
                        dict["RandomForest"] = score

                    if "mlp" in line.lower():
                        dict["MLPClassifier"] = score

                    if "extracted dt" in line.lower():
                        dict["DTExtract"] = score

                    if "trained dt" in line.lower():
                        dict["DTTrained"] = score

                    if "dtextractrel" in line.lower():
                        dict["DTExtract Relative"] = score

        df = df.append(dict, ignore_index=True)

    print df

    for filename in os.listdir(corel_logs):
        searchfile = open(corel_logs + '/' + filename, 'r')
        dict = {"Name": filename}
        for line in searchfile:
            if "Averaged over 10 trials: " in line:
                if "test" in line.lower():
                    if "expertsys relative mlp" in line:
                        score = re.findall('\d*\.?\d+', line)[1]
                        df.loc[df["Name"] == filename, "CORELSRELMLP"] = score
                    if "expertsys relative rf" in line:
                        score = re.findall('\d*\.?\d+', line)[1]
                        df.loc[df["Name"] == filename, "CORELSRELRF"] = score
                    if "corels test score" in line:
                        score = re.findall('\d*\.?\d+', line)[1]
                        df.loc[df["Name"] == filename, "CORELS"] = score


    for filename in os.listdir(expertsys_logs):
        searchfile = open(expertsys_logs + '/' + filename, 'r')
        dict = {"Name": filename}
        for line in searchfile:
            if "Averaged over 10 trials: " in line:
                if "test" in line.lower():
                    if "expertsys relative mlp" in line:
                        score = re.findall('\d*\.?\d+', line)[1]
                        df.loc[df["Name"] == filename, "sklearn-expertsys-relmlp"] = score
                    if "expertsys relative rf" in line:
                        score = re.findall('\d*\.?\d+', line)[1]
                        df.loc[df["Name"] == filename, "sklearn-expertsys-relrf"] = score
                    if "expertsys test score" in line:
                        score = re.findall('\d*\.?\d+', line)[1]
                        df.loc[df["Name"] == filename, "sklearn-expertsys"] = score



    df = df.sort_values(by = "Name")
    print df

    #csv name change this so things don't get overwritten
    df.to_csv(cwd + "/" + "accuracyrel.csv", index=None)
if __name__ == "__main__":
    readlogs()
