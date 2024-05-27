import scipy.stats as stats

# Expected probabilities for each sum (2 to 12)
probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Observed counts from the two runs
observed_counts_1 = [4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13]
observed_counts_2 = [3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5]

# Calculate total number of observations for each run
total_1 = sum(observed_counts_1)
total_2 = sum(observed_counts_2)

# Calculate expected counts for each sum
expected_counts_1 = [probabilities[sum_] * total_1 for sum_ in range(2, 13)]
expected_counts_2 = [probabilities[sum_] * total_2 for sum_ in range(2, 13)]

# Perform the chi-squared test
chi2_stat_1, p_val_1 = stats.chisquare(observed_counts_1, f_exp=expected_counts_1)
chi2_stat_2, p_val_2 = stats.chisquare(observed_counts_2, f_exp=expected_counts_2)

# Significance level
alpha = 0.05

# Interpret the results
def interpret_chi2(p_val):
    if p_val < alpha:
        return "not sufficiently random"
    elif p_val < 2 * alpha:
        return "suspect"
    elif p_val < 3 * alpha:
        return "almost suspect"
    else:
        return "sufficiently random"

# Labels for the two runs
label_1 = interpret_chi2(p_val_1)
label_2 = interpret_chi2(p_val_2)

# Output the results
print(f"Run 1: χ² = {chi2_stat_1:.2f}, p-value = {p_val_1:.4f}, Randomness: {label_1}")
print(f"Run 2: χ² = {chi2_stat_2:.2f}, p-value = {p_val_2:.4f}, Randomness: {label_2}")