{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOlLobtDWvjvVVu3T5nVgmD",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sheena-k/hrmodel/blob/main/model.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_d4SShZYvfdF"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data = pd.read_csv(\"aug_train.csv\")"
      ],
      "metadata": {
        "id": "dZLUX8rfvy5Y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"major_discipline\"].replace([\"Business Degree\", \"No Major\"],\n",
        "                             [\"Business_Degree\",\"No_Major\"],inplace=True)"
      ],
      "metadata": {
        "id": "hCRJvcj5vzfp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"enrolled_university\"].replace([\"Full time course\", \"Part time course\"],\n",
        "                             ['Full_time_course','Part_time_course'],inplace=True)"
      ],
      "metadata": {
        "id": "lDHRHpw3wkra"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"education_level\"].replace([\"High School\", \"Primary School\"],\n",
        "                             ['High_School','Primary_School'],inplace=True)"
      ],
      "metadata": {
        "id": "OZ0HW3_3w5md"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"company_type\"].replace([\"Pvt Ltd\",\"Funded Startup\",\"Public Sector\",\"Early Stage Startup\"],\n",
        "                             [\"Pvt_Ltd\",\"Funded_Startup\",\"Public_Sector\",\"Early_Stage_Startup\"],inplace=True)"
      ],
      "metadata": {
        "id": "ZozNmWltw8ts"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"company_size\"].replace([\"<10\",\"10/49\", \"50-99\", \"100-500\", \"500-999\", \"1000-4999\", \"5000-9999\", \"10000+\"],\n",
        "                             [\"Startup\",\"Small\",\"Small\",\"Medium\",\"Medium\",\"Large\",\"Large\",\"Large\"],inplace=True)\n"
      ],
      "metadata": {
        "id": "t959CaCGxB0s"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"relevent_experience\"].replace([\"Has relevent experience\", \"No relevent experience\"],\n",
        "                             ['Yes','No'],inplace=True)"
      ],
      "metadata": {
        "id": "4oHcTwGpxGI6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"last_new_job\"].replace([\">4\",\"never\"],\n",
        "                        ['5',\"0\"],inplace=True)"
      ],
      "metadata": {
        "id": "MIAhXiKD1wpP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "DbeSgBVH174r"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"experience\"].replace([\">20\",\"<1\"],[\"21\",\"0\"],inplace=True)"
      ],
      "metadata": {
        "id": "EQsbotD613Ze"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"education_level\"].unique()"
      ],
      "metadata": {
        "id": "CwJzrkO8xKpi",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "39fb6a06-4fac-4327-b826-159f2a4bf4b1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Graduate', 'Masters', 'High_School', nan, 'Phd', 'Primary_School'],\n",
              "      dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"company_size\"].fillna(value=\"NW\",inplace=True) #not working yet\n",
        "data[\"company_type\"].fillna(value=\"NW\",inplace=True)\n",
        "data[\"gender\"].fillna(value=\"DNM\",inplace=True)"
      ],
      "metadata": {
        "id": "hdWf-2P2xRR-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"enrolled_university\"].fillna(data[\"enrolled_university\"].mode()[0],inplace=True)"
      ],
      "metadata": {
        "id": "Qfx9KivBxeGk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"education_level\"].fillna(data[\"education_level\"].mode()[0],inplace=True)"
      ],
      "metadata": {
        "id": "PwShze-Dxh16"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "data[\"major_discipline\"].fillna(data[\"major_discipline\"].mode()[0],inplace =True)"
      ],
      "metadata": {
        "id": "H0C2RUnzxlm8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"last_new_job\"].fillna(data[\"last_new_job\"].mode()[0],inplace=True)"
      ],
      "metadata": {
        "id": "0MuwFicoxo3n"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"experience\"].fillna(data[\"experience\"].mode()[0],inplace=True)"
      ],
      "metadata": {
        "id": "nuK-4rJDxwMM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data = data.astype({'last_new_job':'int'})"
      ],
      "metadata": {
        "id": "4QQgnVKXDV1B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"experience\"] = data[\"experience\"].astype(int)"
      ],
      "metadata": {
        "id": "RlykodjTDV4d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"education_level\"].unique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eZyG-DOTbiAt",
        "outputId": "f839930e-1725-453e-b72a-1bea6dc3dbc3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Graduate', 'Masters', 'High_School', 'Phd', 'Primary_School'],\n",
              "      dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"company_size\"].unique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "huTFd0uLbjVJ",
        "outputId": "afe6bc9a-0e77-4c2b-f7c8-e1f78b47e46a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['NW', 'Small', 'Startup', 'Large', 'Medium'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"gender\"].unique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q9Wx6r5-bwq5",
        "outputId": "090e4a84-1d2f-4cf8-a02b-927cc1f5f70a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Male', 'DNM', 'Female', 'Other'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "U5DXLbJBb1jw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vwuniKztxz1g",
        "outputId": "a6e6b625-4405-469a-f1b1-bbe5a49e89d3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "enrollee_id               0\n",
              "city                      0\n",
              "city_development_index    0\n",
              "gender                    0\n",
              "relevent_experience       0\n",
              "enrolled_university       0\n",
              "education_level           0\n",
              "major_discipline          0\n",
              "experience                0\n",
              "company_size              0\n",
              "company_type              0\n",
              "last_new_job              0\n",
              "training_hours            0\n",
              "target                    0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "train=data.drop(['enrollee_id',\"city\"],axis=1) # dropping enrollee id and city\n",
        "train"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 443
        },
        "id": "J9RSciZex45q",
        "outputId": "5e360229-181f-4f7f-a4d6-88a928c89f61"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       city_development_index gender relevent_experience enrolled_university  \\\n",
              "0                       0.920   Male                 Yes       no_enrollment   \n",
              "1                       0.776   Male                  No       no_enrollment   \n",
              "2                       0.624    DNM                  No    Full_time_course   \n",
              "3                       0.789    DNM                  No       no_enrollment   \n",
              "4                       0.767   Male                 Yes       no_enrollment   \n",
              "...                       ...    ...                 ...                 ...   \n",
              "19153                   0.878   Male                  No       no_enrollment   \n",
              "19154                   0.920   Male                 Yes       no_enrollment   \n",
              "19155                   0.920   Male                 Yes       no_enrollment   \n",
              "19156                   0.802   Male                 Yes       no_enrollment   \n",
              "19157                   0.855    DNM                  No       no_enrollment   \n",
              "\n",
              "      education_level major_discipline  experience company_size  \\\n",
              "0            Graduate             STEM          21           NW   \n",
              "1            Graduate             STEM          15        Small   \n",
              "2            Graduate             STEM           5           NW   \n",
              "3            Graduate  Business_Degree           0           NW   \n",
              "4             Masters             STEM          21        Small   \n",
              "...               ...              ...         ...          ...   \n",
              "19153        Graduate       Humanities          14           NW   \n",
              "19154        Graduate             STEM          14           NW   \n",
              "19155        Graduate             STEM          21        Small   \n",
              "19156     High_School             STEM           0       Medium   \n",
              "19157  Primary_School             STEM           2           NW   \n",
              "\n",
              "         company_type  last_new_job  training_hours  target  \n",
              "0                  NW             1              36     1.0  \n",
              "1             Pvt_Ltd             5              47     0.0  \n",
              "2                  NW             0              83     0.0  \n",
              "3             Pvt_Ltd             0              52     1.0  \n",
              "4      Funded_Startup             4               8     0.0  \n",
              "...               ...           ...             ...     ...  \n",
              "19153              NW             1              42     1.0  \n",
              "19154              NW             4              52     1.0  \n",
              "19155         Pvt_Ltd             4              44     0.0  \n",
              "19156         Pvt_Ltd             2              97     0.0  \n",
              "19157              NW             1             127     0.0  \n",
              "\n",
              "[19158 rows x 12 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-4b604d11-0520-422b-8a37-d017d74ecb3d\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>city_development_index</th>\n",
              "      <th>gender</th>\n",
              "      <th>relevent_experience</th>\n",
              "      <th>enrolled_university</th>\n",
              "      <th>education_level</th>\n",
              "      <th>major_discipline</th>\n",
              "      <th>experience</th>\n",
              "      <th>company_size</th>\n",
              "      <th>company_type</th>\n",
              "      <th>last_new_job</th>\n",
              "      <th>training_hours</th>\n",
              "      <th>target</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.920</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>no_enrollment</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>STEM</td>\n",
              "      <td>21</td>\n",
              "      <td>NW</td>\n",
              "      <td>NW</td>\n",
              "      <td>1</td>\n",
              "      <td>36</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.776</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>no_enrollment</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>STEM</td>\n",
              "      <td>15</td>\n",
              "      <td>Small</td>\n",
              "      <td>Pvt_Ltd</td>\n",
              "      <td>5</td>\n",
              "      <td>47</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.624</td>\n",
              "      <td>DNM</td>\n",
              "      <td>No</td>\n",
              "      <td>Full_time_course</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>STEM</td>\n",
              "      <td>5</td>\n",
              "      <td>NW</td>\n",
              "      <td>NW</td>\n",
              "      <td>0</td>\n",
              "      <td>83</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0.789</td>\n",
              "      <td>DNM</td>\n",
              "      <td>No</td>\n",
              "      <td>no_enrollment</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Business_Degree</td>\n",
              "      <td>0</td>\n",
              "      <td>NW</td>\n",
              "      <td>Pvt_Ltd</td>\n",
              "      <td>0</td>\n",
              "      <td>52</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0.767</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>no_enrollment</td>\n",
              "      <td>Masters</td>\n",
              "      <td>STEM</td>\n",
              "      <td>21</td>\n",
              "      <td>Small</td>\n",
              "      <td>Funded_Startup</td>\n",
              "      <td>4</td>\n",
              "      <td>8</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19153</th>\n",
              "      <td>0.878</td>\n",
              "      <td>Male</td>\n",
              "      <td>No</td>\n",
              "      <td>no_enrollment</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>Humanities</td>\n",
              "      <td>14</td>\n",
              "      <td>NW</td>\n",
              "      <td>NW</td>\n",
              "      <td>1</td>\n",
              "      <td>42</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19154</th>\n",
              "      <td>0.920</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>no_enrollment</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>STEM</td>\n",
              "      <td>14</td>\n",
              "      <td>NW</td>\n",
              "      <td>NW</td>\n",
              "      <td>4</td>\n",
              "      <td>52</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19155</th>\n",
              "      <td>0.920</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>no_enrollment</td>\n",
              "      <td>Graduate</td>\n",
              "      <td>STEM</td>\n",
              "      <td>21</td>\n",
              "      <td>Small</td>\n",
              "      <td>Pvt_Ltd</td>\n",
              "      <td>4</td>\n",
              "      <td>44</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19156</th>\n",
              "      <td>0.802</td>\n",
              "      <td>Male</td>\n",
              "      <td>Yes</td>\n",
              "      <td>no_enrollment</td>\n",
              "      <td>High_School</td>\n",
              "      <td>STEM</td>\n",
              "      <td>0</td>\n",
              "      <td>Medium</td>\n",
              "      <td>Pvt_Ltd</td>\n",
              "      <td>2</td>\n",
              "      <td>97</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19157</th>\n",
              "      <td>0.855</td>\n",
              "      <td>DNM</td>\n",
              "      <td>No</td>\n",
              "      <td>no_enrollment</td>\n",
              "      <td>Primary_School</td>\n",
              "      <td>STEM</td>\n",
              "      <td>2</td>\n",
              "      <td>NW</td>\n",
              "      <td>NW</td>\n",
              "      <td>1</td>\n",
              "      <td>127</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>19158 rows × 12 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4b604d11-0520-422b-8a37-d017d74ecb3d')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-4b604d11-0520-422b-8a37-d017d74ecb3d button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-4b604d11-0520-422b-8a37-d017d74ecb3d');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-431367e7-ca00-435b-a5c1-4d17c0703aa7\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-431367e7-ca00-435b-a5c1-4d17c0703aa7')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-431367e7-ca00-435b-a5c1-4d17c0703aa7 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_46844335-e43d-4039-8358-f5b5ac56cfdc\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('train')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_46844335-e43d-4039-8358-f5b5ac56cfdc button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('train');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import LabelEncoder"
      ],
      "metadata": {
        "id": "RUHagPErx_D_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "le= LabelEncoder()"
      ],
      "metadata": {
        "id": "BNOFAmH7yN8y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train[\"relevent_experience\"] = le.fit_transform(train[\"relevent_experience\"])"
      ],
      "metadata": {
        "id": "upndx1sryQ5a"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train[\"relevent_experience\"].unique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c2qhmngryVgm",
        "outputId": "5cb89f99-de8c-4f13-88af-b4bf9f8e64d8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 0])"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "train[\"education_level\"] = le.fit_transform(train[\"education_level\"])"
      ],
      "metadata": {
        "id": "d9K2st2SydIq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train[\"education_level\"].unique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZLJGo9i7ylh9",
        "outputId": "ba16ba7d-b07a-4ab7-96c7-7eaca9ec80de"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0, 2, 1, 3, 4])"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "5M70Ip1jbLGT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train[\"last_new_job\"].unique()"
      ],
      "metadata": {
        "id": "9frYeCFwyqB_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "43b1da13-caef-4f8e-c8f4-da89133de714"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 5, 0, 4, 3, 2])"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "train[\"experience\"] = train[\"experience\"].astype(int)"
      ],
      "metadata": {
        "id": "87dVRDA2Fogo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train[\"last_new_job\"] = train[\"last_new_job\"].astype(int)"
      ],
      "metadata": {
        "id": "f8Cx8yh9y1rI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "train[\"company_size\"] = le.fit_transform(train[\"company_size\"])"
      ],
      "metadata": {
        "id": "PbzoOPxmy4S2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train[\"company_size\"].unique()"
      ],
      "metadata": {
        "id": "j8a3e4PMy-Lf",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "06a21618-79cc-40ca-f395-4d2cfa6c5a63"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([2, 3, 4, 0, 1])"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "x9QCRRHbzBnV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "train[\"gender\"] = le.fit_transform(train[\"gender\"])"
      ],
      "metadata": {
        "id": "vgku3fsQzF6y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train[\"gender\"].unique()"
      ],
      "metadata": {
        "id": "uLZ0Dk1rzJ82",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "22c5cfd5-45eb-4941-fcd5-0afa77b2a7c9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([2, 0, 1, 3])"
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "train = pd.get_dummies(train)"
      ],
      "metadata": {
        "id": "1raMZGdXzNWT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X = train.drop(\"target\",axis=1)\n",
        "Y = pd.DataFrame(train[\"target\"])\n"
      ],
      "metadata": {
        "id": "Q9jVqL0VzRzC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from imblearn.over_sampling import SMOTE"
      ],
      "metadata": {
        "id": "N3enEx_uzZ7k"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "smote = SMOTE()\n",
        "X,Y = smote.fit_resample(X,Y)"
      ],
      "metadata": {
        "id": "Y9_QjkD1zf0s"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X.tail()"
      ],
      "metadata": {
        "id": "bIAta1LjzjHS",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 255
        },
        "outputId": "abc6f31a-6880-44c4-cc83-2474649e62cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       city_development_index  gender  relevent_experience  education_level  \\\n",
              "28757                0.624000       2                    1                2   \n",
              "28758                0.917986       2                    1                0   \n",
              "28759                0.746827       0                    0                0   \n",
              "28760                0.920000       2                    0                0   \n",
              "28761                0.742341       0                    1                0   \n",
              "\n",
              "       experience  company_size  last_new_job  training_hours  \\\n",
              "28757           3             2             1             130   \n",
              "28758          21             2             5               7   \n",
              "28759           4             2             1               9   \n",
              "28760          16             2             0              17   \n",
              "28761           8             3             1              44   \n",
              "\n",
              "       enrolled_university_Full_time_course  \\\n",
              "28757                                     0   \n",
              "28758                                     0   \n",
              "28759                                     0   \n",
              "28760                                     0   \n",
              "28761                                     0   \n",
              "\n",
              "       enrolled_university_Part_time_course  ...  major_discipline_No_Major  \\\n",
              "28757                                     0  ...                          0   \n",
              "28758                                     0  ...                          0   \n",
              "28759                                     0  ...                          0   \n",
              "28760                                     0  ...                          0   \n",
              "28761                                     0  ...                          0   \n",
              "\n",
              "       major_discipline_Other  major_discipline_STEM  \\\n",
              "28757                       0                      1   \n",
              "28758                       0                      1   \n",
              "28759                       0                      1   \n",
              "28760                       0                      0   \n",
              "28761                       0                      1   \n",
              "\n",
              "       company_type_Early_Stage_Startup  company_type_Funded_Startup  \\\n",
              "28757                                 0                            0   \n",
              "28758                                 0                            0   \n",
              "28759                                 0                            0   \n",
              "28760                                 0                            0   \n",
              "28761                                 0                            0   \n",
              "\n",
              "       company_type_NGO  company_type_NW  company_type_Other  \\\n",
              "28757                 0                0                   0   \n",
              "28758                 0                1                   0   \n",
              "28759                 0                1                   0   \n",
              "28760                 0                1                   0   \n",
              "28761                 0                0                   0   \n",
              "\n",
              "       company_type_Public_Sector  company_type_Pvt_Ltd  \n",
              "28757                           0                     0  \n",
              "28758                           0                     0  \n",
              "28759                           0                     0  \n",
              "28760                           0                     0  \n",
              "28761                           0                     1  \n",
              "\n",
              "[5 rows x 24 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-60f68932-92bf-4dfb-a85b-4b309045cd0c\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>city_development_index</th>\n",
              "      <th>gender</th>\n",
              "      <th>relevent_experience</th>\n",
              "      <th>education_level</th>\n",
              "      <th>experience</th>\n",
              "      <th>company_size</th>\n",
              "      <th>last_new_job</th>\n",
              "      <th>training_hours</th>\n",
              "      <th>enrolled_university_Full_time_course</th>\n",
              "      <th>enrolled_university_Part_time_course</th>\n",
              "      <th>...</th>\n",
              "      <th>major_discipline_No_Major</th>\n",
              "      <th>major_discipline_Other</th>\n",
              "      <th>major_discipline_STEM</th>\n",
              "      <th>company_type_Early_Stage_Startup</th>\n",
              "      <th>company_type_Funded_Startup</th>\n",
              "      <th>company_type_NGO</th>\n",
              "      <th>company_type_NW</th>\n",
              "      <th>company_type_Other</th>\n",
              "      <th>company_type_Public_Sector</th>\n",
              "      <th>company_type_Pvt_Ltd</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>28757</th>\n",
              "      <td>0.624000</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>130</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>28758</th>\n",
              "      <td>0.917986</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>21</td>\n",
              "      <td>2</td>\n",
              "      <td>5</td>\n",
              "      <td>7</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>28759</th>\n",
              "      <td>0.746827</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>4</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>9</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>28760</th>\n",
              "      <td>0.920000</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>16</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>17</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>28761</th>\n",
              "      <td>0.742341</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>8</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>44</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 24 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-60f68932-92bf-4dfb-a85b-4b309045cd0c')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-60f68932-92bf-4dfb-a85b-4b309045cd0c button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-60f68932-92bf-4dfb-a85b-4b309045cd0c');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-5a050dd2-1273-4c31-bc61-5b9b31f0033f\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-5a050dd2-1273-4c31-bc61-5b9b31f0033f')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-5a050dd2-1273-4c31-bc61-5b9b31f0033f button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Y= np.squeeze(Y)"
      ],
      "metadata": {
        "id": "4xeR-YFV3oeF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split"
      ],
      "metadata": {
        "id": "QYlZWXIl2oUT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x_train,x_test,y_train,y_test = train_test_split(X,Y, test_size = 0.2, random_state=42)"
      ],
      "metadata": {
        "id": "JFU_2ZXw2p-X"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.ensemble import RandomForestClassifier"
      ],
      "metadata": {
        "id": "Gv_mqCOtzpGj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "rf_cls =RandomForestClassifier()"
      ],
      "metadata": {
        "id": "AijpZQ3V2Xo0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import accuracy_score"
      ],
      "metadata": {
        "id": "2errvm8L2kyp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "48xJGMcd3gqY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_rf = rf_cls.fit(x_train,y_train)"
      ],
      "metadata": {
        "id": "1CEBBkUA3XES"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred_rf = model_rf.predict(x_test)"
      ],
      "metadata": {
        "id": "85bDAZPT3OTn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "accuracy_score(y_test,y_pred_rf)"
      ],
      "metadata": {
        "id": "tTc6eBy635MP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "54a44726-34e8-47d8-c58e-9ea9e4da027e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.8362593429515036"
            ]
          },
          "metadata": {},
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pickle"
      ],
      "metadata": {
        "id": "dOqKyfmh2nKM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "filename=\"savemodel.pickle\""
      ],
      "metadata": {
        "id": "wfNiRIQa2dzN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "with open(filename,\"wb\") as file:\n",
        "  pickle.dump(model_rf,file)"
      ],
      "metadata": {
        "id": "FneWcjrV4sPf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "6OF0hwgQ4tSt"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}