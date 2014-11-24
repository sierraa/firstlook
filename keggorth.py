# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 23:53:19 2014

@author: Sierra
"""
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class KO:
    def __init__(self, name, data, reference, t2d, filename=None):
        self.T2D_samples = []
        self.control_samples = []
        self.data = data
        self.name = name
        for x in range(0, len(data)):
            if reference[x] in t2d:
                self.T2D_samples.append(data[x])
            else:
                self.control_samples.append(data[x])
        
    def basic_stats(self):
        self.T2D_mean = stats.nanmean(self.T2D_samples)
        self.T2D_std = stats.nanstd(self.T2D_samples, axis=None)
        self.control_mean = stats.nanmean(self.control_samples)
        self.control_std = stats.nanstd(self.control_samples, axis=None)
        
    def pval_stats(self):
        self.ttest_pval = stats.ttest_ind(self.T2D_samples, self.control_samples)[1]
        self.ranksums_pval = stats.ranksums(self.T2D_samples, self.control_samples)[1]
        self.mean_pval = (self.ttest_pval + self.ranksums_pval) / 2
        
    def more_stats(self):
        if self.T2D_mean > self.control_mean:
            self.percent_diff = round(((self.T2D_mean - self.control_mean)/self.control_mean)*100, 2)
        else:
            self.percent_diff = round(((self.control_mean - self.T2D_mean)/self.T2D_mean)*100, 2)
        self.rank = (1 - self.mean_pval)*self.percent_diff
        tpresencecount = 0.0;
        cpresencecount = 0.0;
        for i in self.T2D_samples:
            if i > 0:
                tpresencecount += 1;
        for j in self.control_samples:
            if j > 0:
                cpresencecount += 1;
        self.T2D_presence = round((tpresencecount / len(self.T2D_samples))*100, 2)
        self.control_presence = round((cpresencecount / len(self.control_samples))*100, 2)
    
    def graph_stats(self, data1, data2):
        temp = {tuple(data1), tuple(data2)}        
        plt.hist(tuple(temp))
        plt.xlabel('Relative Abundance');
        blue = mpatches.Patch(color='blue', label='Type 2 Diabetes');
        green = mpatches.Patch(color='green', label='Control');
        plt.legend(handles=[blue, green],loc='best');
        plt.show();
    
    def print_stats(self):
        self.basic_stats()
        self.pval_stats()
        self.more_stats()
        print self.name
        print "Mean relative abundance for T2D samples:", self.T2D_mean
        print "Standard deviation for T2D samples:", self.T2D_std
        print
        print "Mean relative abundance for control samples:", self.control_mean
        print "Standard deviation for control samples:", self.control_std
        print
        if self.T2D_mean > self.control_mean:
            print "More prevalent in T2D samples than control by %.2f%%" % self.percent_diff
        else:
            print "More prevalent in control samples than T2D by %.2f%%" % self.percent_diff
        print "Present in %.2f %% of T2D samples" % self.T2D_presence
        print "Present in %.2f %% of control samples" % self.control_presence 
        print
        print "P-value for Student's t-test:", self.ttest_pval
        print "P-value for Wilcoxon rank-sum test:", self.ranksums_pval
        print "Mean p-value of the two tests:", self.mean_pval
        print
        
        self.graph_stats(data1=self.T2D_samples,data2=self.control_samples)
        
    