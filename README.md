# Kit-comparison
Comparison of two kits for mRNA purification


# Description
Hi Ariel:

Here’s the project description:

Goal:
Compare two RNA-seq libraries of the same UHRR + 1% synthetic ERCC control input (10 ng),  prepared with kits from different vendors.
I recommend Salmon for transcript abundance estimation.

Potentially interesting questions:
How sensitive are these two libraries prep methods?
Are high abundance transcripts missing from one or the other library?

What questions arise from your observations?
What other experiments would you design to answer these questions?

Figures that speak to these questions would be helpful.
(e.g. correlations, TPM vs. # of transcripts with at least that TPM (cumulative histogram))

I’ve put the sequence data and a gencode-v25+ERCC reference fasta onto an amazon instance that I spun up for this project.
Feel free to install any software you might need into /mnt/data (conda install X will probably get you what you want). I’ve already installed salmon, and a few other packages.

You can log in here (once I have your public key in the trust list)

ssh langhorst@52.91.193.76

I’m happy to discuss any questions that might come up.


Brad

# Analysis
[analysis](https://htmlpreview.github.io/?https://github.com/aerijman/Kit-comparison/blob/master/analysis.html)
