# Copyright 2015-2016 Stanford University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from data import *

# Constants

# Global constants

TMP_PATH = '../tmp'

# Diabetes constants

DIABETES_PATH = TMP_PATH + '/pima-indians-diabetes.csv'
DIABETES_HAS_HEADER = True
DIABETES_DATA_TYPES = [NUM, NUM, NUM, NUM, NUM, NUM, NUM, NUM, CAT_RES]

DIABETES_IS_CLASSIFY = True
DIABETES_DELIM_WHITESPACE = False

DIABETES_OUTPUT = 'pima_indians_diabetes.log'

# Iris constants

IRIS_PATH = TMP_PATH + '/iris.data'
IRIS_HAS_HEADER = False
IRIS_DATA_TYPES = [NUM, NUM, NUM, NUM, CAT_RES]

IRIS_IS_CLASSIFY = True
IRIS_DELIM_WHITESPACE = False

IRIS_OUTPUT = 'iris.log'

# Wine constants

WINE_PATH = TMP_PATH + '/wine.data'
WINE_HAS_HEADER = False
WINE_DATA_TYPES = [CAT_RES] + [NUM for i in range(13)]

WINE_IS_CLASSIFY = True
WINE_DELIM_WHITESPACE = False

WINE_OUTPUT = 'wine.log'

# Student constants

# Returns the type of val.
def getType(val):
    if val.__class__ == type(''):
        return CAT
    if val.__class__ == type(0.0) or val.__class__ == type(0):
        return NUM
    raise Exception('Invalid type: ' + str(val))

# Breast cancer dataset

BREAST_CANCER_DIAG_PATH = TMP_PATH + '/breast_cancer_diag.data'
BREAST_CANCER_DIAG_HAS_HEADER = False
BREAST_CANCER_DIAG_EXAMPLE = [17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]
BREAST_CANCER_DIAG_DATA_TYPES = [ID, CAT_RES] + [getType(val) for val in BREAST_CANCER_DIAG_EXAMPLE]
BREAST_CANCER_DIAG_IS_CLASSIFY = True
BREAST_CANCER_DIAG_DELIM_WHITESPACE = False

BREAST_CANCER_DIAG_OUTPUT = 'Breast Cancer Diagnosis.log'

BREAST_CANCER_PROG_PATH = TMP_PATH + '/breast_cancer_prog.data'
BREAST_CANCER_PROG_HAS_HEADER = False
BREAST_CANCER_PROG_EXAMPLE = [18.02,27.6,117.5,1013,0.09489,0.1036,0.1086,0.07055,0.1865,0.06333,0.6249,1.89,3.972,71.55,0.004433,0.01421,0.03233,0.009854,0.01694,0.003495,21.63,37.08,139.7,1436,0.1195,0.1926,0.314,0.117,0.2677,0.08113,5,5]

BREAST_CANCER_PROG_CL_DATA_TYPES = [ID, CAT_RES, ID] + [getType(val) for val in BREAST_CANCER_PROG_EXAMPLE]
BREAST_CANCER_PROG_CL_IS_CLASSIFY = True
BREAST_CANCER_PROG_CL_DELIM_WHITESPACE = False

BREAST_CANCER_PROG_CL_OUTPUT = 'Breast Cancer Prognosis.log'

BREAST_CANCER_PROG_RG_DATA_TYPES = [ID, ID, NUM_RES] + [getType(val) for val in BREAST_CANCER_PROG_EXAMPLE]
BREAST_CANCER_PROG_RG_IS_CLASSIFY = False
BREAST_CANCER_PROG_RG_DELIM_WHITESPACE = 33

BREAST_CANCER_PROG_RG_OUTPUT = 'breast_cancer_prog_rg.log'

BREAST_CANCER_PROG_MIX_DATA_TYPES = [ID, CAT_RES, NUM] + [getType(val) for val in BREAST_CANCER_PROG_EXAMPLE]
BREAST_CANCER_PROG_MIX_IS_CLASSIFY = True
BREAST_CANCER_PROG_MIX_DELIM_WHITESPACE = 34

BREAST_CANCER_PROG_MIX_OUTPUT = 'breast_cancer_prog_mix.log'

# Car value dataset

CAR_PATH = TMP_PATH + '/car.data'
CAR_HAS_HEADER = False
CAR_DATA_TYPES = [CAT for i in range(6)] + [CAT_RES]
CAR_IS_CLASSIFY = True
CAR_DELIM_WHITESPACE = False

CAR_OUTPUT = 'Car Evaluation.log'


# Fertility dataset

FERTILITY_PATH = TMP_PATH + '/fertility.txt'
FERTILITY_HAS_HEADER = False
FERTILITY_DATA_TYPES = [NUM, NUM, CAT, CAT, CAT, CAT, NUM, CAT, NUM, CAT_RES]
FERTILITY_IS_CLASSIFY = True
FERTILITY_DELIM_WHITESPACE = False

FERTILITY_OUTPUT = 'fertility.log'

MONKS_1_PATH = TMP_PATH + '/monks-1-clean.csv'
MONKS_HAS_HEADER = False
MONKS_DATA_TYPES = [CAT_RES, CAT, CAT, CAT, CAT, CAT, CAT]
MONKS_IS_CLASSIFY = True
MONKS_DELIM_WHITESPACE = False

MONKS_1_OUTPUT = 'monks_1.log'

MONKS_2_PATH = TMP_PATH + '/monks-2-clean.csv'

MONKS_2_OUTPUT = 'monks_2.log'

MONKS_3_PATH = TMP_PATH + '/monks-3-clean.csv'

MONKS_3_OUTPUT = 'monks_3.log'

BANKNOTE_PATH = TMP_PATH + '/data_banknote_authentication.txt'
BANKNOTE_HAS_HEADER = True
BANKNOTE_DATA_TYPES = [NUM, NUM, NUM, NUM, CAT_RES]
BANKNOTE_IS_CLASSIFY = True
BANKNOTE_DELIM_WHITESPACE = False

BANKNOTE_OUTPUT = 'banknote.log'

TAE_PATH = TMP_PATH + '/tae.data'
TAE_HAS_HEADER = False
TAE_DATA_TYPES = [NUM, NUM, NUM, NUM, NUM, NUM_RES]
TAE_IS_CLASSIFY = True
TAE_DELIM_WHITESPACE = False

TAE_OUTPUT = 'Teaching Assistant Evaluation.log'

NEW_THYROID_PATH = TMP_PATH + '/new-thyroid.data'
NEW_THYROID_HAS_HEADER = False
NEW_THYROID_DATA_TYPES = [CAT_RES, NUM, NUM, NUM, NUM, NUM]
NEW_THYROID_IS_CLASSIFY = True
NEW_THYROID_DELIM_WHITESPACE = False

NEW_THYROID_OUTPUT = 'Thyroid Disease New Thyroid.log'

HOUSE_VOTES_PATH = TMP_PATH + '/house-votes-84.data'
HOUSE_VOTES_HAS_HEADER = False
HOUSE_VOTES_DATA_TYPES = [CAT_RES] + [CAT for i in range(16)]
HOUSE_VOTES_IS_CLASSIFY = True
HOUSE_VOTES_DELIM_WHITESPACE = False

HOUSE_VOTES_OUTPUT = 'Conressional Voting Records.log'

BALANCE_PATH = TMP_PATH + '/balance-scale.data'
BALANCE_HAS_HEADER = False
BALANCE_DATA_TYPES = [CAT_RES, CAT, CAT,CAT,CAT]
BALANCE_IS_CLASSIFY = True
BALANCE_DELIM_WHITESPACE = False

BALANCE_OUTPUT = 'balance-scale.log'

SONAR_PATH = TMP_PATH + '/sonar.all-data'
SONAR_HAS_HEADER = False
SONAR_DATA_TYPES = [NUM for i in range(60)] + [CAT_RES]
SONAR_IS_CLASSIFY = True
SONAR_DELIM_WHITESPACE = False

SONAR_OUTPUT = 'Connectionist Bench Sonar.log'

TRANSFUSION_PATH = TMP_PATH + '/transfusion.data'
TRANSFUSION_HAS_HEADER = True
TRANSFUSION_DATA_TYPES = [NUM, NUM, NUM, NUM, CAT_RES]
TRANSFUSION_IS_CLASSIFY = True
TRANSFUSION_DELIM_WHITESPACE = False

TRANSFUSION_OUTPUT = 'Blood Transfusion.log'

CREDIT_PATH = TMP_PATH + '/crx.data'
CREDIT_HAS_HEADER = False
CREDIT_DATA_TYPES = [CAT, NUM, NUM, CAT, CAT, CAT, CAT, NUM, CAT, CAT, NUM, CAT, CAT, NUM, NUM, CAT_RES]
CREDIT_IS_CLASSIFY = True
CREDIT_DELIM_WHITESPACE = False

CREDIT_OUTPUT = 'credit approval.log'

CHESS_PATH = TMP_PATH + '/kr-vs-kp.data'
CHESS_HAS_HEADER = False
CHESS_DATA_TYPES = [CAT for i in range(36)] + [CAT_RES]
CHESS_IS_CLASSIFY = True
CHESS_DELIM_WHITESPACE = False

CHESS_OUTPUT = 'chess king rook versus king pawn.log'

#To read diagnosis.data go to dtextract/python/dtextract/data/data.py and go to
#change line 148 in data.py to have delim_whitespace=True
ACUTE_PATH = TMP_PATH + '/diagnosis.data'
ACUTE_HAS_HEADER = False
#Change the data-types between [NUM, CAT, ..., CAT_RES, ID]/[NUM, CAT, ..., ID, CAT_RES] for acute-1/acute-2
ACUTE_1_DATA_TYPES = [NUM, CAT, CAT, CAT, CAT, CAT, CAT_RES, ID]
ACUTE_2_DATA_TYPES = [NUM, CAT, CAT, CAT, CAT, CAT, ID, CAT_RES]
ACUTE_IS_CLASSIFY = True
ACUTE_DELIM_WHITESPACE = True

ACUTE_1_OUTPUT = 'acute-1.log'
ACUTE_2_OUTPUT = 'acute-2.log'

CMC_PATH = TMP_PATH + '/cmc.data'
CMC_HAS_HEADER = False
CMC_DATA_TYPES = [NUM, CAT, CAT, NUM, CAT, CAT, CAT, CAT, CAT, CAT_RES]
CMC_IS_CLASSIFY = True
CMC_DELIM_WHITESPACE = False

CMC_OUTPUT = 'Contraceptive Method Choice.log'

CYLINDER_PATH = TMP_PATH + '/bands.data'
CYLINDER_HAS_HEADER = False
CYLINDER_DATA_TYPES = [ID, ID] + [CAT for i in range(18)] + [NUM for i in range(19)] + [CAT_RES]
CYLINDER_IS_CLASSIFY = True
CYLINDER_DELIM_WHITESPACE = False

CYLINDER_OUTPUT = 'cylinder bands.log'

ECHOCARDIOGRAM_PATH = TMP_PATH + '/echocardiogram.data'
ECHOCARDIOGRAM_HAS_HEADER = False
ECHOCARDIOGRAM_DATA_TYPES = [NUM, CAT_RES, NUM, CAT, NUM, NUM, NUM, ID, NUM, ID, ID, ID, CAT]
ECHOCARDIOGRAM_IS_CLASSIFY = True
ECHOCARDIOGRAM_DELIM_WHITESPACE = False

ECHOCARDIOGRAM_OUTPUT = 'echocardiogram.log'

HABERMAN_PATH = TMP_PATH + '/haberman.data'
HABERMAN_HAS_HEADER = False
HABERMAN_DATA_TYPES = [NUM, NUM, NUM, CAT_RES]
HABERMAN_IS_CLASSIFY = True
HABERMAN_DELIM_WHITESPACE = False

HABERMAN_OUTPUT = 'haberman.log'

HAYES_PATH = TMP_PATH + '/hayes-roth.data'
HAYES_HAS_HEADER = False
HAYES_DATA_TYPES = [ID, ID, CAT, CAT, CAT, CAT_RES]
HAYES_IS_CLASSIFY = True
HAYES_DELIM_WHITESPACE = False

HAYES_OUTPUT = 'hayes-roth.log'

CLEVELAND_PATH = TMP_PATH + '/processed.cleveland.data'
CLEVELAND_HAS_HEADER = False
CLEVELAND_DATA_TYPES = [NUM, CAT, CAT, NUM, NUM, CAT, CAT, NUM, CAT, NUM, CAT, CAT, CAT, CAT_RES]
CLEVELAND_IS_CLASSIFY = True
CLEVELAND_DELIM_WHITESPACE = False

CLEVELAND_OUTPUT = 'Heart Disease Cleveland.log'

HEPATITIS_PATH = TMP_PATH + '/hepatitis.data'
HEPATITIS_HAS_HEADER = False
HEPATITIS_DATA_TYPES = [CAT_RES, NUM] + [CAT for i in range(12)] + [NUM, NUM, NUM, NUM, NUM, CAT]
HEPATITIS_IS_CLASSIFY = True
HEPATITIS_DELIM_WHITESPACE = False

HEPATITIS_OUTPUT = 'hepatitis.log'

IMAGE_PATH = TMP_PATH + '/segmentation.data'
IMAGE_HAS_HEADER = True
IMAGE_DATA_TYPES = [CAT_RES] + [NUM for i in range(19)]
IMAGE_IS_CLASSIFY = True
IMAGE_DELIM_WHITESPACE = False

IMAGE_OUTPUT = 'Image segmentation.log'

ILP_PATH = TMP_PATH + '/ilp.csv'
ILP_HAS_HEADER = False
ILP_DATA_TYPES = [NUM, CAT] + [NUM for i in range(8)] + [CAT_RES]
ILP_IS_CLASSIFY = True
ILP_DELIM_WHITESPACE = False

ILP_OUTPUT = 'indian liver patient.log'

IONOSPHERE_PATH = TMP_PATH + '/ionosphere.data'
IONOSPHERE_HAS_HEADER = False
IONOSPHERE_DATA_TYPES = [NUM for i in range(34)] + [CAT_RES]
IONOSPHERE_IS_CLASSIFY = True
IONOSPHERE_DELIM_WHITESPACE = False

IONOSPHERE_OUTPUT = 'ionosphere.log'

MAMMOGRAPHIC_PATH = TMP_PATH + '/mammographic_masses.data'
MAMMOGRAPHIC_HAS_HEADER = False
MAMMOGRAPHIC_DATA_TYPES = [CAT, NUM, CAT, CAT, CAT, CAT_RES]
MAMMOGRAPHIC_IS_CLASSIFY = True
MAMMOGRAPHIC_DELIM_WHITESPACE = False

MAMMOGRAPHIC_OUTPUT = 'mammographic.log'

OPTICAL_PATH = TMP_PATH + '/optdigits.tra'
OPTICAL_HAS_HEADER = False
OPTICAL_DATA_TYPES = [NUM for i in range(64)] + [CAT_RES]
OPTICAL_IS_CLASSIFY = True
OPTICAL_DELIM_WHITESPACE = False

OPTICAL_OUTPUT = 'optical recognition.log'

OZONE_8_PATH = TMP_PATH + '/eighthr.data'
OZONE_8_HAS_HEADER = False
OZONE_8_DATA_TYPES = [ID] + [NUM for i in range(72)] + [CAT_RES]
OZONE_8_IS_CLASSIFY = True
OZONE_8_DELIM_WHITESPACE = False

OZONE_8_OUTPUT = 'ozone_eight.log'

OZONE_1_PATH = TMP_PATH + '/onehr.data'
OZONE_1_HAS_HEADER = False
OZONE_1_DATA_TYPES = [ID] + [NUM for i in range(72)] + [CAT_RES]
OZONE_1_IS_CLASSIFY = True
OZONE_1_DELIM_WHITESPACE = False

OZONE_1_OUTPUT = 'ozone_one.log'

PARKINSONS_PATH = TMP_PATH + '/parkinsons.data'
PARKINSONS_HAS_HEADER = True
PARKINSONS_DATA_TYPES = [ID] + [NUM for i in range(16)] + [CAT_RES] + [NUM for i in range(6)]
PARKINSONS_IS_CLASSIFY = True
PARKINSONS_DELIM_WHITESPACE = False

PARKINSONS_OUTPUT = 'parkinsons.log'

#change line 148 in data.py to have delim_whitespace=True

PLRX_PATH = TMP_PATH + '/plrx.txt'
PLRX_HAS_HEADER = False
PLRX_DATA_TYPES = [NUM for i in range(12)] + [CAT_RES]
PLRX_IS_CLASSIFY = True
PLRX_DELIM_WHITESPACE = True

PLRX_OUTPUT = 'planning relax.log'

#change line 148 in data.py to have sep=';'

QSAR_PATH = TMP_PATH + '/biodeg.csv'
QSAR_HAS_HEADER = False
QSAR_DATA_TYPES = [NUM for i in range(41)] + [CAT_RES]
QSAR_IS_CLASSIFY = True
QSAR_DELIM_WHITESPACE = False

QSAR_OUTPUT = 'qsar biodegredation.log'

#change line 148 in data.py to have delim_whitespace=True
SEEDS_PATH = TMP_PATH + '/seeds_dataset.txt'
SEEDS_HAS_HEADER = False
SEEDS_DATA_TYPES = [NUM for i in range(7)] + [CAT_RES]
SEEDS_IS_CLASSIFY = True
SEEDS_DELIM_WHITESPACE = True

SEEDS_OUTPUT = 'seeds.log'

SEISMIC_PATH = TMP_PATH + '/seismic-bumps.arff'
SEISMIC_HAS_HEADER = False
SEISMIC_DATA_TYPES = [CAT, CAT, CAT, NUM, NUM, NUM, NUM, CAT] + [NUM for i in range(10)] + [CAT_RES]
SEISMIC_IS_CLASSIFY = True
SEISMIC_DELIM_WHITESPACE = False

SEISMIC_OUTPUT = 'seismic bumps.log'

SOYBEAN_PATH = TMP_PATH + '/soybean-small.data'
SOYBEAN_HAS_HEADER = False
SOYBEAN_DATA_TYPES = [NUM for i in range(31)] + [CAT_RES]
SOYBEAN_IS_CLASSIFY = True
SOYBEAN_DELIM_WHITESPACE = False

SOYBEAN_OUTPUT = 'soybean small.log'

SPAMBASE_PATH = TMP_PATH + '/spambase.data'
SPAMBASE_HAS_HEADER = False
SPAMBASE_DATA_TYPES = [NUM for i in range(57)] + [CAT_RES]
SPAMBASE_IS_CLASSIFY = True
SPAMBASE_DELIM_WHITESPACE = False

SPAMBASE_OUTPUT = 'spambase.log'

SPECT_PATH = TMP_PATH + '/SPECT.train'
SPECT_HAS_HEADER = False
SPECT_DATA_TYPES = [CAT_RES] + [CAT for i in range(22)]
SPECT_IS_CLASSIFY = True
SPECT_DELIM_WHITESPACE = False

SPECT_OUTPUT = 'spect.log'

SPECTF_PATH = TMP_PATH + '/SPECTF.train'
SPECTF_HAS_HEADER = False
SPECTF_DATA_TYPES = [CAT_RES] + [NUM for i in range(44)]
SPECTF_IS_CLASSIFY = True
SPECTF_DELIM_WHITESPACE = False

SPECTF_OUTPUT = 'spectf.log'

#change line 148 in data.py to have delim_whitespace=True
GERMAN_PATH = TMP_PATH + '/german.data-numeric'
GERMAN_HAS_HEADER = False
GERMAN_DATA_TYPES = [NUM for i in range(24)] + [CAT_RES]
GERMAN_IS_CLASSIFY = True
GERMAN_DELIM_WHITESPACE = True

GERMAN_OUTPUT = 'statlog project german credit.log'

#change line 148 in data.py to have delim_whitespace=True
LANDSAT_PATH = TMP_PATH + '/sat.trn'
LANDSAT_HAS_HEADER = False
LANDSAT_DATA_TYPES = [NUM for i in range(36)] + [CAT_RES]
LANDSAT_IS_CLASSIFY = True
LANDSAT_DELIM_WHITESPACE = True

LANDSAT_OUTPUT = 'statlog project landsat satellite.log'

TICTAC_PATH = TMP_PATH + '/tic-tac-toe.data'
TICTAC_HAS_HEADER = False
TICTAC_DATA_TYPES = [CAT for i in range(9)] + [CAT_RES]
TICTAC_IS_CLASSIFY = True
TICTAC_DELIM_WHITESPACE = False

TICTAC_OUTPUT = 'tictactoe.log'

WALL_PATH = TMP_PATH + '/sensor_readings_2.data'
WALL_HAS_HEADER = False
WALL_DATA_TYPES = [NUM, NUM, CAT_RES]
WALL_IS_CLASSIFY = True
WALL_DELIM_WHITESPACE = False

WALL_OUTPUT = 'wall.log'

THORAIC_PATH = TMP_PATH + '/ThoraricSurgery.arff'
THORAIC_HAS_HEADER = False
THORAIC_DATA_TYPES = [CAT, NUM, NUM, CAT, CAT, CAT, CAT, CAT, CAT, CAT, CAT, CAT, CAT, CAT, CAT, NUM, CAT_RES]
THORAIC_IS_CLASSIFY = True
THORAIC_DELIM_WHITESPACE = False

THORAIC_OUTPUT = 'thoraic surgery.log'

THYROID_ANN_PATH = TMP_PATH + '/ann-train.data'
THYROID_ANN_HAS_HEADER = False
THYROID_ANN_DATA_TYPES = [NUM] + [CAT for i in range(15)] + [NUM for i in range(5)] + [CAT_RES]
THYROID_ANN_IS_CLASSIFY = True
THYROID_ANN_DELIM_WHITESPACE = True

THYROID_ANN_OUTPUT = 'thyroid disease ann thyroid.log'

CLIMATE_PATH = TMP_PATH + '/pop_failures.dat'
CLIMATE_HAS_HEADER = True
CLIMATE_DATA_TYPES = [ID, ID] + [NUM for i in range(18)] + [CAT_RES]
CLIMATE_IS_CLASSIFY = True
CLIMATE_DELIM_WHITESPACE = True

CLIMATE_OUTPUT = 'climate model crashes.log'

CONNECTIONIST_PATH = TMP_PATH + '/vowel-context.data'
CONNECTIONIST_HAS_HEADER = False
CONNECTIONIST_DATA_TYPES = [ID, ID, ID] + [NUM for i in range(10)] + [CAT_RES]
CONNECTIONIST_IS_CLASSIFY = True
CONNECTIONIST_DELIM_WHITESPACE = True

CONNECTIONIST_OUTPUT = 'connectionist bench.log'

BREAST_CANCER_PATH = TMP_PATH + '/breast-cancer-wisconsin.data'
BREAST_CANCER_HAS_HEADER = False
BREAST_CANCER_DATA_TYPES = [ID] + [CAT for i in range(9)] + [CAT_RES]
BREAST_CANCER_IS_CLASSIFY = True
BREAST_CANCER_DELIM_WHITESPACE = False

BREAST_CANCER_OUTPUT = 'breast cancer.log'

# Dermatology dataset

DERMATOLOGY_PATH = TMP_PATH + '/dermatology.data'
DERMATOLOGY_HAS_HEADER = False
DERMATOLOGY_DATA_TYPES = [NUM for i in range(33)] + [NUM, CAT_RES]
DERMATOLOGY_IS_CLASSIFY = True
DERMATOLOGY_DELIM_WHITESPACE = False

DERMATOLOGY_OUTPUT = 'dermatology.log'
