import math
import scipy.stats
import numpy as np
import scipy.special as scsp
import streamlit as st

import streamlit as st

s1=50
s2=60
x1_bar=25
x2_bar=124
n1=24
n2=25
significance_level=0.03
u1,u2=0,0
diff=20


#---------------------Hypothesis test start---------------
ho="="#input("u:(p)  u_0 : ")
ha="!="#input("u:(p)  u_0 : ")

def hypo_test(ho,ha):

    if((ho==">=" and ha=="!=") or (ho==">=" and ha==">") or (ho=="<=" and ha=="!=")or (ho=="<=" and ha=="<")):
        return False
    elif (ha=="<"):
        return "Left_tail"
    elif (ha==">"):
        return "Right_tail"
    else:
        return "Two_tail"
st.write("Ho:(u) :  u1-u2  " + ho + f": {diff}")
st.write("Ha:(u) :  u1-u2 "  + ha + f" : {diff}")

#---------------------Hypothesis test end---------------






# ----------- Pooled Variance Start------------------

s_p=(((n1-1)*(s1*s1))+((n2-1)*(s2*s2)))/(n1+n2-2)
st.write(s_p)

# ----------- Pooled Variance End------------------

# ----------------------- Test Statistic Start-----------------------

t_test=((x1_bar-x2_bar) - diff)/(math.sqrt(s_p*(1/n1 + 1/n2)))
st.write(t_test)

dof=n1+n2-2
st.write(dof)
# ----------------------- Test Statistic End-----------------------

# ---------------- P value start-----------
p_two_tailed=0# (1 - (scipy.stats.t.cdf((t_test), dof))) * 2
p_right=0# 1 - scipy.stats.t.cdf((t_test))
p_left=0.99#scipy.stats.t.cdf(t_test)

# ---------------- P value end-----------

def rejecion_region():
# Rejection Region for 2 tail
            if (hypo_test(ho, ha) == "Two_tail"):
                t_critical = scipy.stats.t.ppf(1 - significance_level / 2, dof)
                # if t_test < (-(scipy.stats.norm.ppf(1 - significance_level / 2))) or t_test > (
                # scipy.stats.norm.ppf(1 - significance_level / 2)):
                #
                #     st.write(f"z critical <{t_critical}" if t_test<0 else f"z critica >{abs(t_critical)}")
                #     # st.write("\nTwo Null hypothesis is rejected ")
                st.write("z test statistic  is :", (t_test))
                st.write("Decision through z statistic : ")
                st.write(f"since test statistic z calculated < {round(t_critical,2)} \n Therefore Null hypothesis is rejected" if t_test < t_critical else f"since test statistic z calculated > {round(t_critical,2)} \n Therefore Null hypothesis is not rejected")
                st.write("Decision through p value : ")
                st.write("p_value is : ", p_two_tailed)
                st.write(f"since p value is < {significance_level}")


            # Rejection Region for left tail
            if (hypo_test(ho, ha) == "Left_tail"):
                t_critical=scipy.stats.t.ppf(significance_level,dof)
                # if z < (-(scipy.stats.norm.ppf(1 - significance_level / 2))):
                #     pass
                #     # st.write("\n Left Null hypothesis is rejected ")

                st.write(f"z critical value is : {t_critical}")
                st.write("z test statistic  is  :", (t_test))
                st.write("Decision through z statistic :")
                st.write(
                    f"since test statistic z calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t_test < t_critical else f"since test statistic z calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")
                st.write("Decision through p value : ")
                st.write("p_value is : ", p_left)
                st.write(f"p_left < {significance_level}")

            # Rejection Region for right tail
            t_critical=scipy.stats.t.ppf(1-significance_level,dof)
            if (hypo_test(ho, ha) == "Right_tail"):
                if t_test > (scipy.stats.norm.ppf(1 - significance_level / 2)):
                    st.write("\nRight Null hypothesis is rejected ")
                st.write(f"z critical value is : {t_critical}")
                st.write("z test statistic  is : ", (t_test))
                st.write("Decision through z statistic :")
                st.write(
                    f"since test statistic z calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t_test > t_critical else f"since test statistic z calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")
                st.write("Decision through p value : ")
                st.write("p_value is : ", p_right)
                st.write(f"p_right > {significance_level}")

if (st.button("calculate")):

    rejecion_region()












