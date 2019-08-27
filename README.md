First off, run setup.sh to unzip the datasets and unzip expertsys as well as pip install CORELS. As long as you're all set up you should be able to run any example you wish.

I used a lot of the same code from https://github.com/obastani/dtextract. Specifically, python/dtextract/examples/runCsv.py. Along with the given example files, I made more to go with the extra datasets. To run all of the example files you can run all.py, by simply doing

      $ cd python
      $ python -m dtextract.examples.all

You can also modify the code in runCsv to make it run CORELS and expertsys, as long as you have expertsys in the same folder as the examples folder, and as long as you have CORELS installed via pip.

You can change lines 340, 346, and 356 of runCsv.py to either run CORELS, expertsys, or DTExtract. You can follow the comments for guidance in that. For example, you'll see:

      340 nVals = len(names)

      346 curVals = runCsvSingle(path, hasHeader, dataTypes, isClassify, delim_whitespace, distType)

      356 lg("Averaged over 10 trials: " + names[i] + str(vals[i]), INFO)

names can be changed to corels and sklearn to run corels and expertsys respectively and runCsvSingle can be changed to runCsvCorels and runCsvSklearn to run corels and sklearn respectively. You need to change both the names variable and the function call in order to correctly run corels, sklearn, and DTExtract. 
