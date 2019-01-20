from SuvApp import app,model
import json
from flask import render_template ,request,Response

#URL for chart of gender count and relationship count
@app.route('/chart', methods=['GET'])
def chart():
    return render_template('chart.html')

#URL for table
@app.route('/table', methods=['GET'])
def table():
    return render_template('table.html')


#api to get the gender and count
@app.route('/chartData', methods=['GET'])
def all_data():
     try:
        survaider = model.survaider.objects.all()
        sex_data = survaider.aggregate({
            '$group' : {
                '_id' : '$sex' ,
                'count' : {'$sum' : 1}
            }
        })

        relationship_data = survaider.aggregate({
            '$group': {
                '_id': '$relationship',
                'count': {'$sum': 1}
            }
        })
        chart1_data =[]
        for chart1_item in sex_data:
            chart1_data.append({'sex' : chart1_item.get('_id'),
                                'count' : chart1_item.get('count')
                                })
        chart2_data = []
        for chart2_item in relationship_data:
            chart2_data.append({'relationship': chart2_item.get('_id'),
                                'count': chart2_item.get('count')
                                })


        return Response(
            mimetype="application/json",
            response=json.dumps({"success" : True , "chart1_data" : chart1_data , "chart2_data" :chart2_data}),
            status=200
        )
     except Exception as e:
         print(e.args)
         return Response(
             mimetype="application/json",
             response=json.dumps({"success": True ,"data":"Error while getting data"}),
             status=400
         )

#API to search particular data
@app.route('/getdataByFilter', methods=['GET'])
def filter_data():
    try:
        req = request.args
        sex = req.get('sex')
        race = req.get('race')
        relationship = req.get('relationship')

        survaider = model.survaider.objects.all()

        if sex is not None:
            survaider = survaider(sex__iexact=sex)
        if race is not None:
            survaider = survaider(race__iexact=race)
        if relationship is not None:
            survaider = survaider(relationship__iexact=relationship)


        data = []
        for item in survaider:
            data.append({
                "age": item.age,
                "marital_status": item.marital_status,
                "education": item.education,
                "capital_gain": item.capital_gain,
                "fnlwgt": item.fnlwgt,
                "native_country": item.native_country,
                "race": item.race,
                "sex": item.sex,
                "education_num": item.education_num,
                "class_type": item.class_type,
                "hours_per_week": item.hours_per_week,
                "workclass": item.workclass,
                "occupation": item.occupation,
                "capital_loss": item.capital_loss,
                "relationship": item.relationship
            })

        return Response(
            mimetype="application/json",
            response=json.dumps({"success": True, "data": data}),
            status=200
        )
    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({"success": True, "data":"error while getting data"}),
            status=400
        )
