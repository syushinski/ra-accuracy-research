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

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPClassifier
from corels import *

from ..data.data import *
from ..data.data import split as splt
from ..data.consts import *
from ..impl.funcs import *
from ..impl.dists import *
from ..impl.simp import *
from ..util.log import *
from ..util.log import log as lg
from ..util.util import *
from ..expertsys.RuleListClassifier import *

# Parameters

# general training parameters
trainingProp = 0.6 # proportion of training data
cvProp = 0.3 # proportion of cv data

# Gaussian mixture model parameters
nComponents = 20

# random forest training parameters
nTrees = 1000

# decision tree extraction parameters
tgtScore = None
minGain = None
maxSize = 33

nPts = 1500
nPtTries = 100
nTestPts = 1500

hiddenSize = 500

# decision tree training parameters
nGreedyTries = 1
maxDtSize = maxSize

# printing parameters
names = ['rf train score: ', 'rf cv score: ', 'rf test score: ',
 'extracted dt train score: ', 'extracted dt cv score: ', 'extracted dt test score: ',
  'dtExtractRelTrainScore: ', 'dtExtractRelCvScore: ', 'dtExtractRelTestScore: ',
   'trained dt train score: ', 'trained dt cv score: ', 'trained dt test score: ',
    'mlp train score: ', 'mlp cv score: ', 'mlp test score: ']

sklearn = ['expertsys train score: ', 'expertsys cv score: ', 'expertsys test score:',
'expertsys relative mlp test score: ', 'expertsys relative rf test score: ']

corels = ['corels train score: ', 'corels cv score: ', 'corels test score: ',
            'expertsys relative mlp test score: ', 'expertsys relative rf test score: ']

# This function
# (1) Loads the dataset
# (2) Trains a random forest
# (3) Extracts a decision tree from the trained random forest
#
# parameters/returns:
#  path : str (path to csv containing dataset)
#  hasHeader : bool (whether the csv has a header)
#  dataTypes : [int] (labels for dataset column data types)
#  isClassify : bool (classification vs. regression)
#  nDataMatrixCols : int (the number of columns in the constructed data matrix)
#  distType: 'CategoricalGaussianMixture' , the type of distribution
#  return : float * float * float * float * float * float * float * float * float (the train, cv, test scores for the random forest, extracted decision tree, and trained decision tree)
def runCsvSingle(path, hasHeader, dataTypes, isClassify, nDataMatrixCols,distType):
    # Step 1: Learn random forest
    lg('Parsing CSV...', INFO)
    (df, res, resMap, catFeats) = readCsv(path, hasHeader, dataTypes, nDataMatrixCols, False)
    lg('Done!', INFO)

    lg('Splitting into training and test...', INFO)
    (trainDfFull, testDf) = splt(df, trainingProp + cvProp)
    (trainDf, cvDf) = splt(trainDfFull, trainingProp / (trainingProp + cvProp))
    lg('Done!', INFO)

    lg('Constructing data matrices...', INFO)
    (XTrainFull, yTrainFull, catFeatIndsFull, numericFeatIndsFull) = \
        constructDataMatrix(trainDfFull, res, catFeats)
    (XTrain, yTrain, catFeatIndsTrain, numericFeatIndsTrain) = \
        constructDataMatrix(trainDf, res, catFeats)
    (XCv, yCv, catFeatIndsCv, numericFeatIndsCv) = \
        constructDataMatrix(cvDf, res, catFeats)
    (XTest, yTest, catFeatIndsTest, numericFeatIndsTest) = \
        constructDataMatrix(testDf, res, catFeats)
    assert(catFeatIndsFull == catFeatIndsTrain)
    assert(catFeatIndsFull == catFeatIndsCv)
    assert(catFeatIndsFull == catFeatIndsTest)
    assert(numericFeatIndsFull == numericFeatIndsTrain)
    assert(numericFeatIndsFull == numericFeatIndsCv)
    assert(numericFeatIndsFull == numericFeatIndsTest)
    lg('Done!', INFO)


    lg('Training random forest...', INFO)
    rf = RandomForestClassifier(n_estimators=nTrees)
    rf.fit(XTrain, yTrain)
    lg('Done!', INFO)

    mlp = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(hiddenSize,))
    mlp.fit(XTrain, yTrain)

    mlpTrainScore = mlp.score(XTrain, yTrain)
    mlpCvScore = mlp.score(XCv, yCv)
    mlpTestScore = mlp.score(XTest, yTest)

    rfTrainScore = rf.score(XTrain, yTrain)
    rfCvScore = rf.score(XCv, yCv)
    rfTestScore = rf.score(XTest, yTest)

    rf = mlp

    # Step 2: Set up decision tree extraction inputs
    paramsLearn = ParamsLearn(tgtScore, minGain, maxSize)
    paramsSimp = ParamsSimp(nPts, nTestPts, isClassify)

    # Step 3: Function
    rfFunc = getRfFunc(rf)

    # Step 4: Distribution
    if distType == 'CategoricalGaussianMixture':
        dist = CategoricalGaussianMixtureDist(XTrainFull, catFeatIndsFull,
                numericFeatIndsFull, nComponents)
        #dist = GaussianMixtureDist(XTrainFull, nComponents)
    else:
        raise Exception('Invalid distType: ' + distType)

    # Step 5: Extract decision tree
    dtExtract = learnDTSimp(genAxisAligned, rfFunc, dist, paramsLearn, paramsSimp)

    lg('Decision tree:', INFO)
    lg(str(dtExtract), INFO)
    lg('Node count: ' + str(dtExtract.nNodes()), INFO)

    dtExtractRelTrainScore = acc(dtExtract.eval, XTrain, rf.predict(XTrain))
    dtExtractRelCvScore = acc(dtExtract.eval, XCv, rf.predict(XCv))
    dtExtractRelTestScore = acc(dtExtract.eval, XTest, rf.predict(XTest))

    lg('DTExtract Relative training score: ' + str(dtExtractRelTrainScore), INFO)
    lg('DTExtract Relative CV score: ' + str(dtExtractRelCvScore), INFO)
    lg('DTExtract Relative test score: ' + str(dtExtractRelTestScore), INFO)

    dtExtractTrainScore = acc(dtExtract.eval, XTrain, yTrain)
    dtExtractCvScore = acc(dtExtract.eval, XCv, yCv)
    dtExtractTestScore = acc(dtExtract.eval, XTest, yTest)

    lg('DTExtract Training score: ' + str(dtExtractTrainScore), INFO)
    lg('DTExtract CV score: ' + str(dtExtractCvScore), INFO)
    lg('DTExtract Test score: ' + str(dtExtractTestScore), INFO)

    # Step 6: Train a (greedy) decision tree regressor, best out of nGreedyTries tries (on test score!)
    lg('Training greedy decision tree, best of: ' + str(nGreedyTries), INFO)
    dtConstructor = DecisionTreeClassifier if isClassify else DecisionTreeRegressor
    maxDtLeaves = (maxDtSize + 1)/2
    cvScore = -1.0
    dtTrain = None
    for i in range(nGreedyTries):
        # train the tree (use randomness for i > 0 so there is variety
        dtTrainCur = dtConstructor(max_leaf_nodes = maxDtLeaves, splitter = ('best' if i == 0 else 'random'))
        dtTrainCur.fit(XTrain, yTrain)
        # score the tree
        cvScoreCur = dtTrainCur.score(XCv, yCv)
        # retain the highest scoring tree
        if cvScore < cvScoreCur:
            cvScore = cvScoreCur
            dtTrain = dtTrainCur
    lg('Done!', INFO)
    lg('Node count: ' + str(dtTrain.tree_.node_count), INFO)

    dtTrainTrainScore = dtTrain.score(XTrain, yTrain)
    dtTrainCvScore = dtTrain.score(XCv, yCv)
    dtTrainTestScore = dtTrain.score(XTest, yTest)

    lg('GreedyTree Training score: ' + str(dtTrainTrainScore), INFO)
    lg('GreedyTree CV score: ' + str(dtTrainCvScore), INFO)
    lg('GreedyTree Test score: ' + str(dtTrainTestScore), INFO)

    lg('MLP Training score: ' + str(mlpTrainScore), INFO)
    lg('MLP CV score: ' + str(mlpCvScore), INFO)
    lg('MLP Test score: ' + str(mlpTestScore), INFO)

    lg('Random Forest Training score: ' + str(rfTrainScore), INFO)
    lg('Random Forest CV score: ' + str(rfCvScore), INFO)
    lg('Random Forest Test score: ' + str(rfTestScore), INFO)

    return [rfTrainScore, rfCvScore, rfTestScore,
     dtExtractTrainScore, dtExtractCvScore, dtExtractTestScore,
      dtExtractRelTrainScore, dtExtractRelCvScore, dtExtractRelTestScore,
       dtTrainTrainScore, dtTrainCvScore, dtTrainTestScore,
        mlpTrainScore, mlpCvScore, mlpTestScore]

def runCsvSklearn(path, hasHeader, dataTypes, isClassify, delim_whitespace,distType):
    # Step 1: Learn random forest
    lg('Parsing CSV...', INFO)
    (df, res, resMap, catFeats) = readCsv(path, hasHeader, dataTypes, delim_whitespace, False)
    lg('Done!', INFO)

    lg('Splitting into training and test...', INFO)
    (trainDfFull, testDf) = splt(df, trainingProp + cvProp)
    (trainDf, cvDf) = splt(trainDfFull, trainingProp / (trainingProp + cvProp))
    lg('Done!', INFO)

    lg('Constructing data matrices...', INFO)
    (XTrainFull, yTrainFull, catFeatIndsFull, numericFeatIndsFull) = \
        constructDataMatrix(trainDfFull, res, catFeats)
    (XTrain, yTrain, catFeatIndsTrain, numericFeatIndsTrain) = \
        constructDataMatrix(trainDf, res, catFeats)
    (XCv, yCv, catFeatIndsCv, numericFeatIndsCv) = \
        constructDataMatrix(cvDf, res, catFeats)
    (XTest, yTest, catFeatIndsTest, numericFeatIndsTest) = \
        constructDataMatrix(testDf, res, catFeats)
    assert(catFeatIndsFull == catFeatIndsTrain)
    assert(catFeatIndsFull == catFeatIndsCv)
    assert(catFeatIndsFull == catFeatIndsTest)
    assert(numericFeatIndsFull == numericFeatIndsTrain)
    assert(numericFeatIndsFull == numericFeatIndsCv)
    assert(numericFeatIndsFull == numericFeatIndsTest)
    lg('Done!', INFO)

    lg('Training expertsys...', INFO)
    clf = RuleListClassifier(max_iter=10000, n_chains=3)
    clf.fit(XTrain, yTrain)
    lg('Done!', INFO)

    sklearnTrainScore = clf.score(XTrain, yTrain)
    sklearnCvScore = clf.score(XCv, yCv)
    sklearnTestScore = clf.score(XTest, yTest)

    lg('sklearnTrainScore: ' + str(sklearnTrainScore), INFO)
    lg('sklearnCvScore: ' + str(sklearnCvScore), INFO)
    lg('sklearnTestScore: ' + str(sklearnTestScore), INFO)

    mlp =  MLPClassifier(solver='lbfgs', hidden_layer_sizes=(hiddenSize,))
    mlp.fit(XTrain, yTrain)

    mlptestscore = mlp.score(XTest, yTest)
    sklearnRelativeMlpTestScore = clf.score(XTest, mlp.predict(XTest))

    lg('sklearn rel mlp test: ' + str(sklearnRelativeMlpTestScore), INFO)
    rf = RandomForestClassifier(n_estimators=nTrees)
    rf.fit(XTrain, yTrain)

    sklearnRelRfTestScore = clf.score(XTest, rf.predict(XTest))

    lg('sklearn rel rf test: ' + str(sklearnRelRfTestScore), INFO)

    return [sklearnTrainScore, sklearnCvScore, sklearnTestScore, sklearnRelativeMlpTestScore, sklearnRelRfTestScore]

def runCsvCorels(path, hasHeader, dataTypes, isClassify, delim_whitespace,distType):
    # Step 1: Learn random forest
    lg('Parsing CSV...', INFO)
    (df, res, resMap, catFeats) = readCsv(path, hasHeader, dataTypes, delim_whitespace, CORELS=True)
    lg('Done!', INFO)

    lg('Splitting into training and test...', INFO)
    (trainDfFull, testDf) = splt(df, trainingProp + cvProp)
    (trainDf, cvDf) = splt(trainDfFull, trainingProp / (trainingProp + cvProp))
    lg('Done!', INFO)

    lg('Constructing data matrices...', INFO)
    (XTrainFull, yTrainFull, catFeatIndsFull, numericFeatIndsFull) = \
        constructDataMatrix(trainDfFull, res, catFeats)
    (XTrain, yTrain, catFeatIndsTrain, numericFeatIndsTrain) = \
        constructDataMatrix(trainDf, res, catFeats)
    (XCv, yCv, catFeatIndsCv, numericFeatIndsCv) = \
        constructDataMatrix(cvDf, res, catFeats)
    (XTest, yTest, catFeatIndsTest, numericFeatIndsTest) = \
        constructDataMatrix(testDf, res, catFeats)
    assert(catFeatIndsFull == catFeatIndsTrain)
    assert(catFeatIndsFull == catFeatIndsCv)
    assert(catFeatIndsFull == catFeatIndsTest)
    assert(numericFeatIndsFull == numericFeatIndsTrain)
    assert(numericFeatIndsFull == numericFeatIndsCv)
    assert(numericFeatIndsFull == numericFeatIndsTest)
    lg('Done!', INFO)

    lg('training corels', INFO)
    clf = CorelsClassifier()
    clf.fit(XTrain, yTrain)
    lg('Done!', INFO)

    corelsTrainScore = clf.score(XTrain, yTrain)
    corelsCvScore = clf.score(XCv, yCv)
    corelsTestScore = clf.score(XTest, yTest)

    lg('corelsTrainScore: ' + str(corelsTrainScore), INFO)
    lg('corelsCvScore: ' + str(corelsCvScore), INFO)
    lg('corelsTestScore: ' + str(corelsTestScore), INFO)

    mlp =  MLPClassifier(solver='lbfgs', hidden_layer_sizes=(hiddenSize,))
    mlp.fit(XTrain, yTrain)

    mlptestscore = mlp.score(XTest, yTest)
    corelsRelativeMlpTestScore = clf.score(XTest, mlp.predict(XTest))

    lg('corels rel mlp test: ' + str(corelsRelativeMlpTestScore), INFO)
    rf = RandomForestClassifier(n_estimators=nTrees)
    rf.fit(XTrain, yTrain)

    corelsRelRfTestScore = clf.score(XTest, rf.predict(XTest))

    lg('corels rel rf test: ' + str(corelsRelRfTestScore), INFO)

    return [corelsTrainScore, corelsCvScore, corelsTestScore, corelsRelativeMlpTestScore, corelsRelRfTestScore ]

# Runs the CSV example repeatedly and reports the average values.
#
# parameters/returns:
#  path : str (path to csv containing dataset)
#  hasHeader : bool (whether the csv has a header)
#  dataTypes : [int] (labels for dataset column data types)
#  isClassify : bool (classification vs. regression)
#  nDataMatrixCols : int (the number of columns in the constructed data matrix)
#  distType: "SamplePlusGauss" | "CategoricalGaussianMixture", the type of distribution, default "CategoricalGaussianMixture"
#  nRepeats : int (default : 1) (number of repetitions to compute the average)
def runCsv(path, hasHeader, dataTypes, isClassify, delim_whitespace, output, distType = "CategoricalGaussianMixture", nRepeats=10):
    #change outputs around for logs
    setCurOutput('logs/newfolder/' + output)

    # change names to corels or sklearn if using corels or expertsys respectively
    nVals = len(names)
    vals = [0.0 for i in range(nVals)]

    # obtain averages
    for i in range(nRepeats):
        #change runCsvSingle to runCsvSklearn if you want to use expertsys and runCsvCorels if you want to use CORELS
        curVals = runCsvSingle(path, hasHeader, dataTypes, isClassify, delim_whitespace, distType)
        for j in range(nVals):
            vals[j] += curVals[j]

    # normalize
    for i in range(nVals):
        vals[i] /= float(nRepeats)

    for i in range(nVals):
        #Don't forget to change names to whatever you set it to above
        lg("Averaged over 10 trials: " + names[i] + str(vals[i]), INFO)
