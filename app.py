from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

'''
This module is responsible for calling 
home page.
'''


@app.route('/')
def home():
    return render_template('home.html')


'''
This module is responsible for calculating RPP based on the given features.
'''


@app.route('/rpp_Calculator', methods=['POST', 'GET'])
def rpp_Calculator():
    if request.method == "POST":
        print("This is evidence list:: ", request.form.getlist("feature"))
        evidences = request.form.getlist("feature")
        evidences.sort()
        rpp_df = pd.read_excel("FinalReport.xlsx")
        temp_Df = rpp_df.copy(deep=True)
        temp_Df.fillna("")
        result = []
        for index, row in temp_Df.iterrows():
            rowList = row.tolist()
            if all(evidence in rowList for evidence in evidences):
                rpps = [x for x in rowList if str(x) != 'nan']
                rpps = list(map(str, rpps))

                if len(rpps) - 1 == len(evidences):
                    result = rpps
                    print("Matching RPP set:: ", rpps)

    return render_template('Rpp_result.html', rpp=result)


if __name__ == '__main__':
    app.run(debug=True)
