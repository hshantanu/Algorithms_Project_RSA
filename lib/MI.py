# Modulo Inverse using Gaussian Elimination
def gaussInverse(a, m):

    if a < 0:
        t = a * -1;
        res = gaussInverse(t, m);
        return m-res;
    else:
        val = -1;
        i = 1;

        while val== -1:
            factor = m/a + i;

            num = factor % m;
            dem = (a*factor) % m;

            val = modInverse(dem, m);
            i += 1;

        num = (num*val) % m;
        return num
    ###End Of IF ELSE

###End of function        


# Assuming m to be positive
def modInverse(a, m):
    if a < 0:
        t = a * -1;
        res = modInverse(t,m);
        return m-res;
    elif gcd(a, m) != 1:
        # Applicable only in-case-of co-prime numbers
        return -1;
    elif m == 1:
        # In case of m==1, modulo inverse cannot exist 
        return -1;
    elif m >= 2:
        # If a and m are relatively prime
        # then Using Fermat's Little Theorem - modulo inverse is a^(m-2) mod m
        return power(a, m-2, m);
    else:
        print "Error: Found Negative moduli";
        return -1;
###End of function

#To compute x^y under modulo m
def power(x, y, m):
    if y == 0:
        return 1;

    p = power(x, y/2, m) % m;
    p = (p * p) % m;
 
    if y%2 == 0:
        return p;
    else:
        return (x * p) % m;
###End of function
 
#Function to return gcd of a and b
def gcd(a, b):
    if a == 0:
        return b;
    return gcd(b%a, a);
###End of function


if __name__ == "__main__":
    import sys
    modInverse(int(sys.argv[1]), int(sys.argv[2]))