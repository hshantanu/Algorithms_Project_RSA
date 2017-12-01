from BasicRSA import *
from ParallelRSATrial import ParallelRSATrial

MIN_BIT_SIZE = 8;
MAX_BIT_SIZE = 4096;
TEST_CASES = 3;

PROCESSORS = 4

def average(list):

    sum = 0;
    total = 0;

    for e in list:
        sum += e;
        total += 1;

    #return float("{0:.5f}".format( float(sum / total) ));
    return float(sum / total);

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
    #return float("{0:.5f}".format(float(math.sqrt(temp))));
    return float(math.sqrt(temp));

### End of function


def accuracy(list):

    total = len(list);
    acc = 0;

    for e in list:
        if e == True:
            acc += 1;

    return float("{0:.3f}".format( float((acc*100) / total) ));

### End of function


def varyN():

    #MSG = "This message is a small text.";
    bits = MIN_BIT_SIZE;
    e = 1023

    while bits <= MAX_BIT_SIZE:

        print "===================================== ", bits ," bits ========================================\n";
        MSG = RNS.GetRandomMessage(bits)

        rTimeList = [];
        pTimeList = [];
        #rStatList = [];
        #pStatList = [];


        for t in xrange(0, TEST_CASES):

            n = generateRSAParameters(bits);

            #rStatList.append( regularRSATrial(MSG, e, n)[0] );
            rTimeList.append( regularRSATrial(MSG, e, n) );

            #pStatList.append( ParallelRSATrial(e, n, MSG, PROCESSORS, bits)[0] );
            pTimeList.append( ParallelRSATrial(e, n, MSG, PROCESSORS, bits) );

        ### End of for loop


        print "------------Regular RSA------------";
        print "Time Consumed: "+ str(rTimeList);
        print "Average Time: "+ str( average(rTimeList) );
        print "Standard Deviation: " + str(standardDeviation(rTimeList));
        #print "Accuracy: " + str( accuracy(rStatList) ) +"%";
        print "\n";

        print "------------Improved RSA------------";
        print "Time Consumed: "+ str(pTimeList);
        print "Average Time: "+ str( average(pTimeList) );
        print "Standard Deviation: " + str(standardDeviation(pTimeList));
        # print "Accuracy: " + str(accuracy(pStatList)) + "%";
        print "\n";

        bits *= 2;

        ### End of loop

### End of fuction


def varyE():

    bits = 1024
    e = 2;

    while e <= 65536:

        print "===================================== " + str(e) + " ========================================\n";
        MSG = RNS.GetRandomMessage(bits)

        rTimeList = [];
        pTimeList = [];
        #rStatList = [];
        #pStatList = [];


        for t in xrange(0, TEST_CASES):

            n = generateRSAParameters(bits);

            rTimeList.append( regularRSATrial(MSG, e, n) );
            #rStatList.append( regularRSATrial(MSG, e, n)[0] );

            pTimeList.append( ParallelRSATrial(e, n, MSG, PROCESSORS, bits) );
            #pStatList.append( ParallelRSATrial(e, n, MSG, PROCESSORS, bits)[0] );

        ### End of for loop


        print "------------Regular RSA------------";
        print "Time Consumed: "+ str(rTimeList);
        print "Average Time: "+ str( average(rTimeList) );
        print "Standard Deviation: " + str(standardDeviation(rTimeList));
        # print "Accuracy: " + str( accuracy(rStatList) ) +"%";
        print "\n";

        print "------------Improved RSA------------";
        print "Time Consumed: "+ str(pTimeList);
        print "Average Time: "+ str( average(pTimeList) );
        print "Standard Deviation: " + str(standardDeviation(pTimeList));
        # print "Accuracy: " + str(accuracy(pStatList)) + "%";
        print "\n";

        e *= 2;

        ### End of loop

### End of fuction


def varyProcessors():

    bits = 1024
    e = 1023;
    p = 2;

    while p <= 512:

        print "===================================== " + str(p) + " ========================================\n";
        MSG = RNS.GetRandomMessage(bits)

        rTimeList = [];
        pTimeList = [];
        #rStatList = [];
        #pStatList = [];


        for t in xrange(0, TEST_CASES):

            n = generateRSAParameters(bits);

            rTimeList.append( regularRSATrial(MSG, e, n) );
            #rStatList.append( regularRSATrial(MSG, e, n)[0] );

            pTimeList.append( ParallelRSATrial(e, n, MSG, p, bits) );
            #pStatList.append( ParallelRSATrial(e, n, MSG, PROCESSORS, bits)[0] );

        ### End of for loop


        print "------------Regular RSA------------";
        print "Time Consumed: "+ str(rTimeList);
        print "Average Time: "+ str( average(rTimeList) );
        print "Standard Deviation: " + str(standardDeviation(rTimeList));
        # print "Accuracy: " + str( accuracy(rStatList) ) +"%";
        print "\n";

        print "------------Improved RSA------------";
        print "Time Consumed: "+ str(pTimeList);
        print "Average Time: "+ str( average(pTimeList) );
        print "Standard Deviation: " + str(standardDeviation(pTimeList));
        # print "Accuracy: " + str(accuracy(pStatList)) + "%";
        print "\n";

        p *= 2;

        ### End of loop

### End of fuction


def start():
    #varyN();
    #varyE();
    varyProcessors()


if __name__ == '__main__':
    start();
    #stat();