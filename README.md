I used a lot of the same code from https://github.com/obastani/dtextract. Specifically, python/dtextract/examples/runCsv.py. Along with the given example files, I made more to go with the extra datasets. To run all of the example files you can run all.py, by simply doing

      $ cd python
      $ python -m dtextract.examples.all

You can also modify the code in runCsv to make it run CORELS and expertsys, as long as you have expertsys in the same folder as the examples folder, and as long as you have CORELS installed via pip.

You can change lines 340, 346, and 356 of runCsv.py to either run CORELS, expertsys, or DTExtract. You can follow the comments for guidance in that.
