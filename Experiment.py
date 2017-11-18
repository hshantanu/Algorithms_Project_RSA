from BasicRSA import *
import time

MIN_BIT_SIZE = 16;
MAX_BIT_SIZE = 512;
TEST_CASES = 128;


def average(list):

    sum = 0;
    total = 0;

    for e in list:
        sum += e;
        total += 1;

    return float("{0:.5f}".format( float(sum / total) ));

### End of function


def standardDeviation(list):

    avg = average(list);
    n = len(list);
    var = 0;

    for e in list:
        temp = e - avg;
        sq = temp*temp;
        var += sq;

    temp = float(var / (n-1));
    import math
    return float("{0:.5f}".format(float(math.sqrt(temp))));

### End of function


def accuracy(list):

    total = len(list);
    acc = 0;

    for e in list:
        if e == True:
            acc += 1;

    return float("{0:.3f}".format( float((acc*100) / total) ));

### End of function


def start():

    MSG = "This message is a small text.";
    bits = MIN_BIT_SIZE;

    while bits <= MAX_BIT_SIZE:

        print "===================================== " + str(bits) + " bits ========================================\n";
        rTimeList = [];
        pTimeList = [];
        rStatList = [];
        pStatList = [];

        for t in xrange(1, TEST_CASES):

            params = generateRSAParameters(bits);

            rStatList.append( regularRSATrial(MSG, params)[0] );
            rTimeList.append( regularRSATrial(MSG, params)[1] );

        # pStatList.append( regularRSATrial(MSG, params)[0] );            # TODO change to parallelRSATrail
        # pTimeList.append( regularRSATrial(MSG, params)[1] );            # TODO change to parallelRSATrail

        ### End of for loop

        print "------------Regular RSA------------";
        print "Time Consumed: "+ str(rTimeList);
        print "Average Time: "+ str( average(rTimeList) );
        print "Standard Deviation: " + str(standardDeviation(rTimeList));
        print "Accuracy: " + str( accuracy(rStatList) ) +"%";
        print "\n";

        # print "------------Improved RSA------------";
        # print "Time Consumed: "+ str(pTimeList);
        # print "Average Time: "+ str( average(pTimeList) );
        # print "Standard Deviation: " + str(standardDeviation(pTimeList));
        # print "Accuracy: " + str(accuracy(pStatList)) + "%";
        # print "\n";

        bits *= 2;

        ### End of while loop

### End of fuction


if __name__ == '__main__':
    start();