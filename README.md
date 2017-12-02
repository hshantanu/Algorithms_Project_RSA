# Algorithms_Project_RSA (CMSC 641 - Fall 2017)

## Evaluation of RSA Encryption Speeds Using Residue Number Systems to Parallelize Integer Exponentiation 
We evaluate the improvement to RSA encryption speeds from parallelization through converting messages into a Residue Number System (RNS). Additionally, we use Montgomery multiplication to improve integer exponentiation processing times. Two implementations of RSA are studied: one which uses Montgomery multipliers with RNS to parallelize the encryption process and another which does not use RNS or Montgomery exponentiation and is therefore not parallelizable. We analyze the theoretical running times and perform two experiments, one which evaluates the effect of message length and another which evaluates the effect of exponent size. We find that a parallel implementation of RSA using residue number systems and Montgomery exponentiation is asymptotically faster than original RSA algorithm. 

### Prerequisites:
* Python 2
* Crypto Library: 
``` pip install crypto ```

### Files:
* BasicRSA.py: The code for the simplest implementation of the basic RSA algorithm.
* Experiment.py: Run the experiments. It contains the main().
* MM.py: Montgomery Multiplication code. 
* ParallelRSATrial.py: Sets up the parallelization environment for the RSA code. 
* RNS.py: Residue Number System implementation. 

### How to run the experiment: 
``` python Experiment.py ```

### This will run all three experiments containg different values for: 
* 'e', 
* 'n'
* number of processors.
