from flask import Flask, render_template, request
import pandas
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv("data.csv")
first = data.drop(columns="result")
selected = data["result"]

model = DecisionTreeClassifier()
model.fit(first.values, selected)

app = Flask(__name__,template_folder='template')

@app.route("/", methods=["POST","GET"])
def flask():
    try:
        if request.method == "POST":
            genre1 = float(request.form["genre1"])
            genre2 = float(request.form["genre2"])
            prediction = model.predict([[genre1, genre2]])
            genre = [prediction[0]]
            print(genre)
            print(genre_list(genre))
            # predictionLength = len(prediction)
            lenn = len(genre_list(genre))
            return render_template("Flask.html", result=genre_list(genre))
    except Exception as e:
        return render_template("Flask.html", result=genre_list("Default"))

    return render_template("Flask.html", result=genre_list("default"))


def genre_list(result):
    results = []
    ss = ["ss (2).jpeg","ss.jpeg","ss (3).jpeg","ss (4).jpeg","ss (5).jpeg","ss (6).jpeg","ss (7).jpeg","ss (8).jpeg","ss (9).jpeg","ss (10).jpeg"]#SCI-FI
    sa = ["sa.jpeg","sa (2).jpeg","sa (3).jpeg","sa (4).jpeg","sa (5).jpeg","as.jpeg","sa (6).jpeg","sa (7).jpeg","sa (8).jpeg","sa (9).jpeg","sa (10).jpeg"]#SCI-Action
    sc= ["sc (2).jpeg","sc.jpeg","sc (3).jpeg","sc (4).jpeg","sc (5).jpeg","sc (6).jpeg","sc (7).jpeg","sc (8).jpeg","sc (9).jpeg","sc (10).jpeg"]#SCI-Comedy
    sh= ["nRS.jpg","nRS (2).jpg","nRS (3).jpg","nRS (4).jpg","nRS (5).jpg","nRS (6).jpg","sh.jpeg","sh (2).jpeg","sh (3).jpeg","sh (4).jpeg","sh (5).jpeg","sh (6).jpeg","hs.jpeg","hs (2).jpeg"]#Sci-Horror C
    aa= ["nA.jpg","nA (2).jpg","nA (3).jpg","nA (4).jpg","nA (5).jpg","nA (6).jpg","aa.jpeg","aa (2).jpeg","aa (3).jpeg","aa (4).jpeg","aa (5).jpeg","aa (6).jpeg"]#Action C
    ar= ["nAR.jpg","nAR (2).jpg","nAR (3).jpg","nAR (4).jpg","nAR (5).jpg","nAR (6).jpg","ar.jpeg","ar (2).jpeg","ar1.jpeg","ar2.jpeg","ar3.jpeg","ra.jpeg","ra (2).jpeg"]#Action -Romance  C
    ac= ["nAC.jpg","nAC (2).jpg","nAC (3).jpg","nAC (4).jpg","nAC (5).jpg","ac.jpeg","ac (2).jpeg","ac (3).jpeg","ac (4).jpeg","ac1.jpeg","ac2.jpeg","ca.jpeg","ca (2).jpeg"]#Action - Comedy C
    ah= ["nAC (6).jpg","nAC (7).jpg","nAC (8).jpg","nAC (9).jpg","nAC (10).jpg","nAC (11).jpg","ah1.jpeg","ah2.jpeg","ha (2).jpeg","ha (3).jpeg","ha (4).jpeg"]#Action - Horror C
    rs= ["nRS.jpg","nRS (2).jpg","nRS (3).jpg","nRS (4).jpg","nRS (5).jpg","nRS (6).jpg","sr.jpeg","sr (2).jpeg","sr (3).jpeg","sr (4).jpeg","sr (5).jpeg","sr (6).jpeg"]#Romance - SciFi C
    rr= ["nRR.jpeg","nRR (2).jpeg","nRR (3).jpeg","nRR (4).jpeg","nRR (5).jpeg","nRR (6).jpeg","nRR (7).jpeg","rr.jpeg","rr (2).jpeg","rr (3).jpeg","rr (4).jpeg","rr (5).jpeg","rr (6).jpeg","rr (7).jpeg","rr (8).jpeg"]#Romance
    rc= ["rc (3).jpeg","rc (2).jpeg","rc.jpeg","rc (4).jpeg","rc (5).jpeg","rc (6).jpeg","rc (7).jpeg","rc (8).jpeg","rc (9).jpeg","rc (10).jpeg"]#Romance - Comedy
    rh= ["nHR.jpg","nHR (2).jpg","nHR (3).jpg","nHR (4).jpg","nHR (5).jpg","nHR (6).jpg","nHR (7).jpg","nHR (8).jpg","nHR (9).jpg","hr1.jpeg","rh2.jpeg","hr.jpeg"]#Romance - Horror C
    cc= ["nC (6).jpg","nC (7).jpg","nC (8).jpg","nC (9).jpg","nC (10).jpg","nC (11).jpg","nC.jpeg","nC.png","nC (2).jpeg","nC (3).jpeg","nC (4).jpeg","nC (5).jpeg","cc.jpeg","cc (2).jpeg","cc (3).jpeg"]#Comedy C
    ch= ["nHC.jpg","nHC (2).jpg","nHC (3).jpg","nHC (4).jpg","nHC (5).jpg","nHC (6).jpg","nHC (7).jpg","nHC (8).jpg","hc.jpeg","hc (2).jpeg","hc (3).jpeg","ch.jpeg"]#Comedy - Horror  C
    hh= ["nH.jpg","nH (2).jpg","nH (3).jpg","nH (4).jpg","hh.jpeg","hh (2).jpeg","hh (3).jpeg","hh (4).jpeg","hh (5).jpeg","hh (6).jpeg","hh (7).jpeg","hh (8).jpeg"]#Horror
    default = ["received_326447557069583.jpeg","received_1445885139355055.jpeg","received_1109243816992349.jpeg","received_978006453840890.jpeg","received_963979548579535.jpeg","received_954055462950058.jpeg","received_911103237425586.jpeg","received_888277896641955.jpeg","received_789147453075886.jpeg","received_728022436177279.jpeg","received_712797224362168.jpeg","received_663679755820293.jpeg","received_439439401941740.jpeg","received_394699100186387.jpeg","received_382611321291951.jpeg","received_379505898393749.jpeg","received_372255648970147.jpeg","received_349307147459000.jpeg","received_347314104374034.jpeg","received_329847056759007.jpeg",]

    if result[0] == "ss":
        for i in ss:
            results.append(i)
    elif result[0] == "sa" or result[0] == "sas":
        for i in sa:
            results.append(i)
    elif result[0] == "sc" or result[0] == "cs":
        for i in sc:
            results.append(i)
    elif result[0] == "sh" or result[0] == "hs":
        for i in sh:
            results.append(i)
    elif result[0] == "aa":
        for i in aa:
            results.append(i)
    elif result[0] == "ar" or result[0] == "ra":
        for i in ar:
            results.append(i)
    elif result[0] == "ac" or result[0] == "ca":
        for i in ac:
            results.append(i)
    elif result[0] == "ah" or result[0] == "ha":
        for i in ah:
            results.append(i)
    elif result[0] == "rs" or result[0] == "sr":
        for i in rs:
            results.append(i)
    elif result[0] == "rr":
        for i in rr:
            results.append(i)
    elif result[0] == "rc" or result[0] == "cr":
        for i in rc:
            results.append(i)
    elif result[0] == "rh" or result[0] == "hr":
        for i in rh:
            results.append(i)
    elif result[0] == "cc":
        for i in cc:
            results.append(i)
    elif result[0] == "ch" or result[0] == "hc":
        for i in ch:
            results.append(i)
    elif result[0] == "hh":
        for i in hh:
            results.append(i)
    else:
        for i in default:
            results.append(i)

    return results


if __name__ == "__main__":
    app.run(debug=True)

