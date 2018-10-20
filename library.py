#!/bin/python

import os,re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def TPM_vs_Length(df, ax):

    '''
        Function plot TPM vs length of transcripts.
        Scale of Lengths is logarithmic and TPM is smoothed.
        input: - "df" for DataFrame (Salmon output) 
               - "ax" for axes (pyplot object corresponding to area of a figure)
    '''

    # get data from df.
    xy = df.sort_values('Length')[['Length', 'TPM']].values

    # Data is too sparce => apply log
    length = np.log(xy[:,0])
    
    # make x labels non logarithmic. 6 ticks is enough.
    xticks = np.linspace(np.log(xy[:,0].min()), np.log(xy[:,0].max()), 6)
    xlabels = np.exp(xticks).astype(int)
    
    # Smooth the data a little since is too spiky and very difficult to see any difference between the two samples.
    tpm = np.convolve(xy[:,1], np.ones(1000)/1000, mode="same")
    
    # plot data
    ax.plot(length, tpm)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, rotation=45)
    ax.grid()
    ax.set_xlabel('Length of transcripts')
    ax.set_ylabel('slightly smoothed TPMs')
    
    # return 
    return length, tpm



'''
     I've splitted the sam files into smaller files, since it requires too much memory.
     Filenames are kit1_aa, kit_ab... and kit2_aa...
'''
# Test each file independently and average the results to make this evaluation less memory expensive 
sub_sam_files = lambda x: [i for i in os.listdir('./STAR_results/') if re.search(''.join([x,'_a']), i)]


def sam(samfile):
    '''
        function open sam files and returns chromosome, start and length joined as a string. 
        Exact same string is unlikely to happend and will be considered a duplicate 
    '''
    m = []
    for line in open(samfile):
        # skip header
        if line[0]=="@": continue
        sam = line.strip('\n').split('\t')
        chrom, start, length = sam[2], sam[3], sam[7]
        tmp = '_'.join([chrom, start, length])
        m.append(tmp)
    return m


def histo(data, bins, color):
    '''
        function plot a cummulative histogram 
        input: data (numpy array), bins and color
    '''
    # make histogram
    values, base = np.histogram(data, bins=bins)
    #calculate cumulative
    cumulative = np.cumsum(values)
    # plot 
    plt.plot(base[:-1], cumulative, color=color)
    

