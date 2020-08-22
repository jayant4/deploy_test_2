import math
import math
import scipy.stats
import numpy as np
from scipy import stats
import scipy.special as scsp

u1,u2=0,0
diff=10
s1=50
s2=60
x1_bar=25
x2_bar=124
n1=24
n2=25

# signinficane level sigma
significance_level=0.01


#---------------------Hypothesis test start---------------
ho="="#input("u:(p)  u_0 : ")
ha=">"#input("u:(p)  u_0 : ")


def hypo_test(ho,ha):

    if((ho==">=" and ha=="!=") or (ho==">=" and ha==">") or (ho=="<=" and ha=="!=")or (ho=="<=" and ha=="<")):
        return False
    elif (ha=="<"):
        return "Left_tail"
    elif (ha==">"):
        return "Right_tail"
    else:
        return "Two_tail"
print("Ho:(u) :  u1-u2  " + ho + f": {diff}")
print("Ha:(u) :  u1-u2 "  + ha + f" : {diff}")

#---------------------Hypothesis test end---------------

#---------------Test Statistic start ----------------
# t=((x1_bar-x2_bar) - (diff))/math.sqrt((s1*s1/n1)+(s2*s2/n2))
t_test=((x1_bar-x2_bar) - diff)/(math.sqrt(((s1*s1)/n1)+((s2*s2)/n2)))
print("t test",t_test)

#---------------Test Statistic end ------------------






#---------------- degree of freedom start ------------

def degree_of_freedoms(s1,s2,n1,n2):

    op_numerator=(((s1*s1)/n1)+((s2*s2)/n2))**2
    op_denom=((1/(n1-1))*((s1*s1)/n1)**2)+((1/(n2-1))*((s2*s2)/n2)**2)
    return(op_numerator/op_denom)
#---------------- degree of freedom start ------------


# --------------------------Rejection Region Start---------------------------------


def rejection_region():
    degree_of_freedom=degree_of_freedoms(s1,s2,n1,n2)
    pval = round((stats.t.sf(np.abs(t_test), degree_of_freedom)*2),3)
    print("p value is ",pval)
    # Rejection Region for 2 tail
    if (hypo_test(ho, ha) == "Two_tail"):

        if t_test < (-(scipy.stats.norm.ppf(1 - significance_level / 2))) or t_test > scipy.stats.norm.ppf(1 - significance_level / 2):
            Two_tailed_test=scipy.stats.t.ppf(1-significance_level/2,degree_of_freedom)
            print(f"z<{Two_tailed_test}" if t_test<0 else f"z>{abs(Two_tailed_test)}")
            print("\nTwo Null hypothesis is rejected ")
        print("t is :", (t_test))
        print("Decision is :")
        # print("p_value is : ", p_two_tailed)


    # Rejection Region for left tail
    if (hypo_test(ho, ha) == "Left_tail"):
        if t_test < scipy.stats.t.ppf(significance_level,degree_of_freedom):
            print("\n Left Null hypothesis is rejected ")
        print("t is :", (t_test))
        print("Decision is :")
        # print("p_value is : ", p_left)
        print(f"p_left < {significance_level}")

    # Rejection Region for right tail
    if (hypo_test(ho, ha) == "Right_tail"):
        if t_test > scipy.stats.t.ppf(1-significance_level,degree_of_freedom):
            print("\nRight Null hypothesis is rejected ")
        print("t is :", abs(t_test))
        print("Decision is :")
        # print("p_value is : ", p_right)
        print(f"p_right > {significance_level}")
rejection_region()
# --------------------------Rejection Region End---------------------------------

