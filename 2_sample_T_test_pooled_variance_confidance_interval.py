import scipy.stats
import  math
s1=50
s2=60
x1_bar=25
x2_bar=124
n1=24
n2=25
significance_level=0.01


# ----------- Pooled Variance Start------------------

s_p=(((n1-1)*(s1*s1))+((n2-1)*(s2*s2)))/(n1+n2-2)
print(s_p)
dof=n1+n2-2
print(dof)

# ----------- Pooled Variance End------------------

#------confidence interval start----------
lhs=x1_bar-x2_bar




rhs=(scipy.stats.t.ppf(1-significance_level/2,dof))*(math.sqrt((s_p)*(1/n1+1/n2)))

confidence_level_minus,confidence_level_plus=lhs-rhs,lhs+rhs
print(confidence_level_minus,confidence_level_plus)
print(f"Lower bound : {confidence_level_minus}")
print(f"Upper bound : {confidence_level_plus}")

#------confidence interval end----------