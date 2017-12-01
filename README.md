# Algorithms_Project_RSA
## RSA implementation with modifications for the CMSC 641 project. 

## Prerquisites:
Python 2
Crypto Library: 
``` pip install crypto ```

Files:
* BasicRSA.py: The code for the simplest implementation of the basic RSA algorithm.
* Experiment.py: Run the experiments. It contains the main().
* MM.py: Montgomery Multiplication code. 
* ParallelRSATrial.py: Sets up the parallelization environment for the RSA code. 
* RNS.py: Residue Number System implementation. 

How to run the experiment: 
``` python Experiment.py ```

This will run all three experiments containg different values for: 
* 'e', 
* 'n'
* number of processors.
