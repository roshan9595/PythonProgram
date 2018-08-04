class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if (n == 0): 
            return 1%d
        elif (int(n % 2) == 0):
            return ((pow(x, int(n / 2),d) * pow(x, int(n / 2),d))%d)
        else:
            return ((x * pow(x, int(n / 2),d) * pow(x, int(n / 2),d))%d)
        

