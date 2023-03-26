# Table of Contents
* 1\. [Bayesian Testing](#bayesian-testing)
* 2\. [Bayesian Testing Pros](#bayesian-testing-pros) 
* 3\. [Bayesian Testing Cons](#bayesian-testing-cons) 
* 4\. [Steps of Bayesian Testing](#steps-of-bayesian-testing) 
* 5\. [Bayesian Statistics Calculations](#bayesian-statistics-calculations) 
* 6\. [References](#references)
        
# Bayesian Testing
Bayesian Testing or Bayesian A/B Testing is a form of hypothesis testing. Bayesian testing uses Bayesian Statistics, beginning by specifying separate prior distributions to describe each hypothesis. Then  the distributions which describe each hypothesis (posterior distributions) are updated using both  the observed data and the prior distributions. 

![Bayesian Statistics](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*N7HgfQDnxCJo6c7tEGwA9A.png)

# Bayesian Testing Pros:
1. Interpretability, Bayesian Testing [allow useful calculations](https://towardsdatascience.com/bayesian-a-b-testing-and-its-benefits-a7bbe5cb5103), such as the probability that a treatment is better than the control.
2. Bayesian inference also performs much better on [small sample sizes](https://towardsdatascience.com/exploring-bayesian-a-b-testing-with-simulations-7500b4fc55bc);  sample size can be reduced by 75%.

# Bayesian Testing Cons:
1. computationally expensive than traditional frequentist approaches



# Steps of Bayesian Testing
1.  **[Select distribution](https://towardsdatascience.com/bayesian-a-b-testing-and-its-benefits-a7bbe5cb5103) based on your metric of interest.** metrics can be binary, categorical, or continues.
2.  **Calculate the prior.** 
3.  **Calculate the posteriors**
4.  **Calculate Bayesian Statistics (percent lift, probability of being best, and expected loss).** 

# Bayesian Statistics Calculations
1. Treatment lift: the percent change between treatment and control. 
2. Probability of being the best: the percentage of the time that treatment is better than control. 
3. Expected loss: the cost of implementing an incorrect treatment. Loss calculation may vary depending on metric of interest.

# References
1. [Bayesian A/B Testing in 5 Minutes](https://towardsdatascience.com/bayesian-a-b-testing-and-its-benefits-a7bbe5cb5103)
2. [How to run A/B Tests as a Data Scientist!](https://www.youtube.com/watch?v=OVgi6ftJiyQ&t=1415s&ab_channel=CodeEmporium)
3. [The Beta Distribution : Data Science Basics](https://www.youtube.com/watch?v=1k8lF3BriXM&ab_channel=ritvikmath)
