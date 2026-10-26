from statsmodels.stats.proportion import proportions_ztest

conversions = [80, 120]
visitors = [1000, 1000]

z_stat, p_value = proportions_ztest(conversions, visitors)

rate_A = conversions[0] / visitors[0] * 100
rate_B = conversions[1] / visitors[1] * 100

print("Campaign A Conversion Rate:", rate_A, "%")
print("Campaign B Conversion Rate:", rate_B, "%")
print("z-statistic:", round(z_stat, 2))
print("p-value:", round(p_value, 4))

alpha = 0.05

if p_value < alpha:
    print("Reject the Null Hypothesis")
    print("The conversion rates are significantly different.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("There is no significant difference in conversion rates.")
