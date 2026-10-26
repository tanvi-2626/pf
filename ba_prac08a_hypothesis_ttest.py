import numpy as np
from scipy.stats import ttest_1samp

sales = np.array([52000, 48000, 51000, 53000, 49500,
                  50500, 51500, 49000, 52500, 50000])

claimed_mean = 50000

t_stat, p_value = ttest_1samp(sales, claimed_mean)

print("Sample Mean:", sales.mean())
print("Claimed Mean:", claimed_mean)
print("t-statistic:", round(t_stat, 2))
print("p-value:", round(p_value, 4))

alpha = 0.05

if p_value < alpha:
    print("Reject the Null Hypothesis")
    print("There is significant evidence that average sales differ from Rs. 50,000.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("There is not enough evidence that average sales differ from Rs. 50,000.")
