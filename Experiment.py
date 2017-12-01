from BasicRSA import *
from ParallelRSATrial import ParallelRSATrial
from RNS import GetRandomMessage
from Primes import primes

MIN_BIT_SIZE = 8;
MAX_BIT_SIZE = 4096;
TEST_CASES = 64;

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



def stat():
    
    from Results import *

    min8= 100;
    min16= 100
    min32= 100
    min64= 100
    min128= 100
    min256= 100
    min512= 100
    min1024= 100
    min2048 = 100;
    min4096= 100;
    max8= 0
    max16= 0
    max32= 0
    max64= 0
    max128= 0
    max256= 0
    max512= 0
    max1024= 0
    max2048 = 0
    max4096= 0;

    for i in xrange(0, 1240):
        if tc_r_8[i] < min8:
            min8 = tc_r_8[i]
        if tc_r_8[i] > max8:
            max8 = tc_r_8[i]

        if tc_r_16[i] < min16:
            min16 = tc_r_16[i]
        if tc_r_16[i] > max16:
            max16 = tc_r_16[i]

        if tc_r_32[i] < min32:
            min32 = tc_r_32[i]
        if tc_r_32[i] > max32:
            max32 = tc_r_32[i]

        if tc_r_64[i] < min64:
            min64 = tc_r_64[i]
        if tc_r_64[i] > max64:
            max64 = tc_r_64[i]

        if tc_r_128[i] < min128:
            min128 = tc_r_128[i]
        if tc_r_128[i] > max128:
            max128 = tc_r_128[i]

        if tc_r_256[i] < min256:
            min256 = tc_r_256[i]
        if tc_r_256[i] > max256:
            max256 = tc_r_256[i]

        if tc_r_512[i] < min512:
            min512 = tc_r_512[i]
        if tc_r_512[i] > max512:
            max512 = tc_r_512[i]

        if tc_r_1024[i] < min1024:
            min1024 = tc_r_1024[i]
        if tc_r_1024[i] > max1024:
            max1024 = tc_r_1024[i]

        if tc_r_2048[i] < min2048:
            min2048 = tc_r_2048[i]
        if tc_r_2048[i] > max2048:
            max2048 = tc_r_2048[i]

        if tc_r_4096[i] < min4096:
            min4096 = tc_r_4096[i]
        if tc_r_4096[i] > max4096:
            max4096 = tc_r_4096[i]


    print max8 - min8;
    print max16 - min16;
    print max32 - min32;
    print max64 - min64;
    print max128 - min128;
    print max256 - min256;
    print max512 - min512;
    print max1024 - min1024;
    print max2048 - min2048;
    print max4096 - min4096;

### End of fuction


def start():
    #varyE();
    varyN();

if __name__ == '__main__':
    start();
    #stat();