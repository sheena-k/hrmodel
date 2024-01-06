
import pickle

import numpy as np



from flask import Flask, request, render_template
#from flask_cors import cross_origin


app = Flask(__name__)  # initializing a flask app

model = pickle.load(open('savemodel.pickle','rb'))

@app.route("/")  
#@cross_origin()


def home():
    
    return render_template("home.html")


@app.route("/predict", methods= ["GET","POST"])
#@cross_origin()


def predict():
    
    if request.method == 'POST':
      
       city_development_index = float(request.form['city_development_index'])
       gender = request.form['gender']
       relevent_experience = request.form['relevent_experience']
       
       education_level = request.form['education_level']
       
       experience = int(request.form['experience'])
       
       

       enrolled_university = request.form['enrolled_university']
       if(enrolled_university == "enrolled_university_no_enrollment"):
       
          enrolled_university_no_enrollment =1
          enrolled_university_Full_time_course =0
          enrolled_university_Part_time_course =0
       
       
       elif(enrolled_university == "enrolled_university_Full_time_course"):
             
            enrolled_university_Full_time_course =1
            enrolled_university_no_enrollment = 0
            
            enrolled_university_Part_time_course = 0
      
       else:
            enrolled_university_Part_time_course = 1
            enrolled_university_no_enrollment = 0
            enrolled_university_Full_time_course =0
            

       major_discipline = request.form['major_discipline']
       if   (major_discipline == "major_discipline_Arts"):
            major_discipline_Arts =1
            
            major_discipline_Business_Degree = 0
            major_discipline_Humanities = 0
            major_discipline_STEM = 0
            major_discipline_No_Major = 0
            major_discipline_Other = 0

       elif (major_discipline == "major_discipline_STEM"):
            major_discipline_STEM =1
            major_discipline_Arts =0
            major_discipline_Business_Degree = 0
            major_discipline_Humanities = 0
            
            major_discipline_No_Major = 0
            major_discipline_Other = 0

       elif (major_discipline == "major_discipline_Business_Degree"):
             major_discipline_Business_Degree = 1
             major_discipline_Arts =0
             
             major_discipline_Humanities = 0
             major_discipline_STEM = 0
             major_discipline_No_Major = 0
             major_discipline_Other = 0

       elif (major_discipline == 'major_discipline_Humanities'):
             major_discipline_Humanities = 1
             major_discipline_Arts =0
             major_discipline_Business_Degree = 0
             
             major_discipline_STEM = 0
             major_discipline_No_Major = 0
             major_discipline_Other = 0

       elif (major_discipline == 'major_discipline_No_Major'):
             major_discipline_No_Major = 1
             major_discipline_Arts =0
             major_discipline_Business_Degree = 0
             major_discipline_Humanities = 0
             major_discipline_STEM = 0
             
             major_discipline_Other = 0
       else:
             major_discipline_Business_Degree = 1
             major_discipline_Arts =0
            
             major_discipline_Humanities = 0
             major_discipline_STEM = 0
             major_discipline_No_Major = 0
             major_discipline_Other = 0
             
       company_type = request.form['company_type']
       if(   company_type == "company_type_Early_Stage_Startup"):
             company_type_Early_Stage_Startup = 1
             company_type_Pvt_Ltd = 0
             company_type_Funded_Startup = 0
             company_type_Other = 0
             company_type_Public_Sector = 0
             company_type_NGO = 0
             company_type_NW =0
       elif (company_type == "company_type_Pvt_Ltd"):
             company_type_Early_Stage_Startup = 0
             company_type_Pvt_Ltd = 1
             company_type_Funded_Startup = 0
             company_type_Other = 0
             company_type_Public_Sector = 0
             company_type_NGO = 0
             company_type_NW =0
       elif (company_type == 'company_type_Funded_Startup'):
             company_type_Early_Stage_Startup = 0
             company_type_Pvt_Ltd = 0
             company_type_Funded_Startup = 1
             company_type_Other = 0
             company_type_Public_Sector = 0
             company_type_NGO = 0
             company_type_NW =0
       elif (company_type == 'company_type_Other'):
             company_type_Early_Stage_Startup = 0
             company_type_Pvt_Ltd = 0
             company_type_Funded_Startup = 0
             company_type_Other = 1
             company_type_Public_Sector = 0
             company_type_NGO = 0
             company_type_NW =0
              
       elif (company_type == 'company_type_Public_Sector'):
             company_type_Early_Stage_Startup = 0
             company_type_Pvt_Ltd = 0
             company_type_Funded_Startup = 0
             company_type_Other = 0
             company_type_Public_Sector = 1
             company_type_NGO = 0
             company_type_NW =0
             
       elif (company_type == 'company_type_NW'):
             company_type_Early_Stage_Startup = 0
             company_type_Pvt_Ltd = 0
             company_type_Funded_Startup = 0
             company_type_Other = 0
             company_type_Public_Sector = 0
             company_type_NGO = 0
             company_type_NW = 1
             
       else:
             company_type_NGO = 1
             company_type_Early_Stage_Startup = 0
             company_type_Pvt_Ltd = 0
             company_type_Funded_Startup = 0
             company_type_Other = 0
             company_type_Public_Sector = 0
             
             company_type_NW = 0

       company_size= request.form['company_size']
       last_new_job = int(request.form['last_new_job'])
       training_hours = int(request.form['training_hours'])
         


       prediction= model.predict(np.array([[city_development_index, gender, relevent_experience, education_level, experience, company_size, last_new_job,
       training_hours,enrolled_university_Full_time_course,enrolled_university_Part_time_course,enrolled_university_no_enrollment,major_discipline_Arts,
       major_discipline_Business_Degree,major_discipline_Humanities,major_discipline_No_Major,major_discipline_Other,major_discipline_STEM,company_type_Early_Stage_Startup,
       company_type_Funded_Startup ,company_type_NGO,company_type_NW,company_type_Other,company_type_Public_Sector,company_type_Pvt_Ltd]]))[0]
      


       output = int(prediction)
       if (output == 0):
         
            return render_template("result.html",prediction_text="No, the person is not looking for job change, the predicted value is : ""{}".format(output))
       else :
            return render_template("result.html",prediction_text="Yes, the person is looking for job change, the predicted value is :""{}".format(output))
       
      
        
if __name__=="__main__":
    app.run(debug=True)
