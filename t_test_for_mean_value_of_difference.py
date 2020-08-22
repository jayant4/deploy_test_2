import math
import scipy.stats
import numpy as np
import scipy.special as scsp
import streamlit as st
import pandas as pd

import numpy as np
import streamlit as st

x=[15.09,6.33,3.27,5.86,11.08,2.41,12.32,6.61,14.33]
y=[9.09,3.86,0.63,3.91,12.47,1.13,11.70,8.9,7.5]
n=8
ud=0
difference = []
ho="="#input("Ho:(p)  P0 : ")
ha=">"#input("Ho:(p)  P0 : ")
significance_level=0.1

zip_object = zip(x, y)
for list1_i, list2_i in zip_object:
    difference.append(list1_i-list2_i)

sumation_d=sum(difference)

d_bar=np.mean(difference)

dict_op={"X":x,"Y":y,"d_bar : X-Y":difference}

op_df=pd.DataFrame(dict_op)
st.write(op_df)

std_dev=np.std(difference)
# print(np.std(difference))


# ---------------------Hypothesis test start---------------


def hypo_test(ho, ha):
    if ((ho == ">=" and ha == "!=") or (ho == ">=" and ha == ">") or (ho == "<=" and ha == "!=") or (
            ho == "<=" and ha == "<")):
        return False
    elif (ha == "<"):
        return "Left_tail"
    elif (ha == ">"):
        return "Right_tail"
    else:
        return "Two_tail"


# print(hypo_test(ho,ha))

# st.write("Ho:(p) : " + ho + f" : {P0}")
# st.write("Ho:(p) : " + ha + f" : {P0}")

# ---------------------Hypothesis test end---------------

# --------------------Test Statistic Start--------------------
t=(d_bar-ud)/(std_dev/math.sqrt(n))
# print(t)

# --------------------Test Statistic End--------------------

# ---------------- P value start-----------
df=n-1
p_two_tailed= (1 - (scipy.stats.t.cdf((t),df)))*2
p_right=1 - scipy.stats.t.cdf((t),df)
p_left=scipy.stats.t.cdf(t,df)
print(p_two_tailed)
# ---------------- P value end-----------

def rejecion_region():
# Rejection Region for 2 tail
            if (hypo_test(ho, ha) == "Two_tail"):
                print(f"p value is {p_two_tailed}")
                print(f"since  p-value > {significance_level} therefore fail to reject " if p_two_tailed > significance_level else f"since  p-value > {significance_level} therefore reject ")

# Rejection Region for left tail
            if (hypo_test(ho, ha) == "Left_tail"):
                print(f"p value is {p_left}")
                print(f"since  p-value > {significance_level} therefore fail to reject " if p_two_tailed > significance_level else f"since  p-value > {significance_level} therefore reject ")

# Rejection Region for right tail
            if (hypo_test(ho, ha) == "Right_tail"):

                print(f"p value is {p_right}")
                print(f"since  p-value > {significance_level} therefore fail to reject " if p_two_tailed > significance_level else f"since  p-value > {significance_level} therefore reject ")

rejecion_region()
if (st.button("calculate")):
    rejecion_region()


# print(f"since  p-value > {significance_level} therefore fail to reject " if p_two_tailed>significance_level else f"since  p-value > {significance_level} therefore reject ")
