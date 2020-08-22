import math
import scipy.special as scsp
import scipy.stats
import numpy as np

n1=230
n2=540
x1=100
x2=200
significance_level=0.01

#Sample proportion
p1_hat=x1/n1
# print("p1 hat : ",p1_hat)

p2_hat=x2/n2
# print("p2 hat : ",p2_hat)

#Pooled Population
p_bar=(x1+x2)/(n1+n2)
# print("p bar : ",p_bar)
#
#Hypothesis Test
#---------------------Hypothesis test start---------------

ho="="#input("Ho:(P1)  P2 : ")
ha="!="#input("Ho:(P1)  P2 : ")

def hypo_test(ho,ha):

    if((ho==">=" and ha=="!=") or (ho==">=" and ha==">") or (ho=="<=" and ha=="!=")or (ho=="<=" and ha=="<")):
        return False
    elif (ha=="<"):
        return "Left_tail"
    elif (ha==">"):
        return "Right_tail"
    else:
        return "Two_tail"
# print("Ho:(P1) : " + ho + f" : {p2_hat}")
# print("Ha:(P1) : " + ha + f" : {p2_hat}")

# print(hypo_test(ho,ha))




#---------------------Hypothesis test end---------------
# Test Statistic
z=(p1_hat-p2_hat)/(math.sqrt(p_bar*(1-p_bar)*(1/n1+1/n2)))
print("test statistic z : ",z)

#----------------P value from Z Start-------------
p_left =round(0.5 * (1 + scsp.erf(float(z) / np.sqrt(2))),5)
p_right =1-p_left
p_two_tailed=1
if float(z) < 0:
    p_two_tailed = 2 * p_left
else:
    p_two_tailed = 2 * p_right
# #----------------P value from Z End-------------


def rejection_region():
    # Rejection Region for 2 tail
    if (hypo_test(ho, ha) == "Two_tail"):
        if z < (-(scipy.stats.norm.ppf(1 - significance_level / 2))) or z > (
                scipy.stats.norm.ppf(1 - significance_level / 2)):
            z_critical = ((-(scipy.stats.norm.ppf(1 - significance_level / 2))))
            print(f"z<{z_critical}" if z < 0 else f"z>{abs(z_critical)}")
            print("\nTwo Null hypothesis is rejected ")
        print("z is :", (z))
        print("Decision is :")
        print("p_value is : ", p_two_tailed)

    # Rejection Region for left tail
    if (hypo_test(ho, ha) == "Left_tail"):
        print(f"Left Null hypothesis is rejected if z < {(-(scipy.stats.norm.ppf(1 - significance_level / 2)))}")

        print("z is :", (z))
        print("Decision is :")
        print("p_value is : ", p_left)
        print(f"p_left < {significance_level}")

    # Rejection Region for right tail
    if (hypo_test(ho, ha) == "Right_tail"):

        print(f"\nRight Null hypothesis is rejected if z >{((scipy.stats.norm.ppf(1 - significance_level / 2)))}")
        print("z is :", abs(z))
        print("Decision is :")
        print("p_value is : ", p_right)
        print(f"p_right > {significance_level}")
rejection_region()
# --------------------------Rejection Region End---------------------------------