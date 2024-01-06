
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE



data = pd.read_csv("aug_train.csv")

data["major_discipline"].replace(["Business Degree", "No Major"],
                             ["Business_Degree","No_Major"],inplace=True)

data["enrolled_university"].replace(["Full time course", "Part time course"],
                             ['Full_time_course','Part_time_course'],inplace=True)

data["education_level"].replace(["High School", "Primary School"],
                             ['High_School','Primary_School'],inplace=True)

data["company_type"].replace(["Pvt Ltd","Funded Startup","Public Sector","Early Stage Startup"],
                             ["Pvt_Ltd","Funded_Startup","Public_Sector","Early_Stage_Startup"],inplace=True)

data["company_size"].replace(["<10","10/49", "50-99", "100-500", "500-999", "1000-4999", "5000-9999", "10000+"],
                             ["Startup","Small","Small","Medium","Medium","Large","Large","Large"],inplace=True)

data["relevent_experience"].replace(["Has relevent experience", "No relevent experience"],
                             ['Yes','No'],inplace=True)

data["last_new_job"].replace([">4","never"],
                        ['5',"0"],inplace=True)



data["experience"].replace([">20","<1"],["21","0"],inplace=True)



data["company_size"].fillna(value="NW",inplace=True) #not working yet
data["company_type"].fillna(value="NW",inplace=True)
data["gender"].fillna(value="DNM",inplace=True)

data["enrolled_university"].fillna(data["enrolled_university"].mode()[0],inplace=True)

data["education_level"].fillna(data["education_level"].mode()[0],inplace=True)

data["major_discipline"].fillna(data["major_discipline"].mode()[0],inplace =True)

data["last_new_job"].fillna(data["last_new_job"].mode()[0],inplace=True)

data["experience"].fillna(data["experience"].mode()[0],inplace=True)

data = data.astype({'last_new_job':'int'})

data["experience"] = data["experience"].astype(int)

data.isnull().sum()

train=data.drop(['enrollee_id',"city"],axis=1) # dropping enrollee id and city
train



le= LabelEncoder()

train["relevent_experience"] = le.fit_transform(train["relevent_experience"])

train["relevent_experience"].unique()

train["education_level"] = le.fit_transform(train["education_level"])

train["education_level"].unique()

train["last_new_job"].unique()

train["last_new_job"] = train["last_new_job"].astype(int)

train["company_size"] = le.fit_transform(train["company_size"])

train["company_size"].unique()



train["gender"] = le.fit_transform(train["gender"])

train["gender"].unique()

train = pd.get_dummies(train)

X = train.drop("target",axis=1)
Y = pd.DataFrame(train["target"])


smote = SMOTE()
X,Y = smote.fit_resample(X,Y)

X.tail()

Y= np.squeeze(Y)


x_train,x_test,y_train,y_test = train_test_split(X,Y, test_size = 0.2, random_state=42)


rf_cls =RandomForestClassifier()





model_rf = rf_cls.fit(x_train,y_train)

y_pred_rf = model_rf.predict(x_test)



