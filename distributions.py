# -*- coding: utf-8 -*-
from scipy.stats import beta
import pandas as pd
class Beta:
      def __init__(self, prior_df=pd.DataFrame(), conversion_column=None, alpha=2, betaa=2):
          """
          Initiate beta distribution using:
              1- prior data if given
              2- parameters
          Input:
              prior_df: data to be used as a prior
              conversion_column: column which indicates weather a user have converged or not
              alpha, betaa: beta distribution parameters
          """
          if not prior_df.empty:
             assert conversion_column in prior_df.columns, "A valid Conversion Column should be provided"
             
             # Model Beta Distribtion from samples means
             prior_means = []
             for i in range(10000):
                 prior_means.append(prior_df.sample(1000)[conversion_column].mean())
             alpha, betaa, _, _ = beta.fit(prior_means, floc=0, fscale=1)
          self.alpha = alpha
          self.betaa = betaa
          self.dist = beta(self.alpha,self.betaa)

      def sample(self, n_samples):
          """ Sample n_samples from the distribution """
          return self.dist.rvs(n_samples)

      def update_parameters(self, update_df, conversion_column):
          """
          update the distribution parameters given the newly seen data
          Input:
              update_df: newly seen data
              conversion_column: column which indicates weather a user have converged or not
          Output:
              update the distribution parameters
          """
          # get number of conversions and non-conversions
          conversion_count = sum(update_df[conversion_column] == 1)
          non_conversion_count = len(update_df) - conversion_count
          
          # update parameters
          self.alpha += conversion_count
          self.betaa += non_conversion_count
          self.dist = beta(self.alpha,self.betaa)