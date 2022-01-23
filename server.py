from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'coding dojo is awesome'

locations = [
    {"id": 1, "name": "Chicago"},
    {"id": 2, "name": "Seattle"},
    {"id": 3, "name": "Online"},
    {"id": 4, "name": "Burbank"},
    {"id": 5, "name": "Bellevue"}
]

languages = [
    {"id": 1, "name": "HTML"},
    {"id": 2, "name": "CSS"},
    {"id": 3, "name": "JavaScript"},
    {"id": 4, "name": "Python"},
    {"id": 5, "name": "C#"}
]

def findLocationName(id):
    for location in locations:
        if location["id"] == id:
            return location["name"]

def findLanguageName(id):
    for language in languages:
        if language["id"] == id:
            return language["name"]

@app.route('/', methods=['GET'])
def index():

    if not 'surveys' in session:
        session['surveys'] = []
    else:
        print(session['surveys'])

    return render_template("survey.html", locations=locations, languages=languages)

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        print(request.form)
        
        fullname = request.form['fullname']
        location = request.form['location']
        language = request.form['language']
        comments = request.form['comments']

        survey = {
            "fullname": fullname,
            "location": location,
            "language": language,
            "comments": comments
        }

        surveys = session['surveys']
        surveys.append(survey)
        session['surveys'] = surveys

        return redirect('/result')


@app.route('/result', methods=['GET'])
def result():
    if 'surveys' in session:
        if len(session['surveys']) != 0:
            lastSurvey = session['surveys'][-1]

            lastSurvey['location'] = findLocationName(int(lastSurvey['location']))
            lastSurvey['language'] = findLanguageName(int(lastSurvey['language']))

    else:
        lastSurvey = []

    return render_template("result.html", survey = lastSurvey)

@app.route('/all', methods=['GET'])
def all():
    surveysList = []

    if not 'surveys' in session:
        session['surveys'] = surveysList
    else:
        print(session['surveys'])
        surveysList = session['surveys']
        
        for survey in surveysList:
            survey["location"] = findLocationName(int(survey['location']))
            survey["language"] = findLanguageName(int(survey['language']))

    return render_template("all.html", surveys = surveysList)


if __name__ == "__main__":
    app.run(port = 5000, debug = True)
