# Figure8 contextual dataset

This dataset is created by mapping a publicly available dataset from [Figure 8](https://www.figure-eight.com/data-for-everyone/) to [IAB taxonomy (version 1)](https://www.iab.com/guidelines/iab-quality-assurance-guidelines-qag-taxonomy/).

The resultant dataset covers a subset of IAB categories (both tier-1 and tier-2). It is by far the largest public dataset to evaluate contextual targeting classification. Another coarse-grained evaluation dataset can be found [here](https://github.com/YipingNUS/nle-supplementary-dataset).

Two files are provided here:

1. `figure8_simplified.csv`: a simplified version of the original figure8 dataset following their categories. Remove all irrelevant fields and ignore the "Not working" cases. 
2. `figure8_iag.csv`: mapped to IAB taxonomy categories. The URLs which cannot be mapped are removed.
 
---

The description of [the original dataset](https://d1p17r2m4rzlbo.cloudfront.net/wp-content/uploads/2016/03/URL-categorization-DFE.csv) is as follows:

## URL categorization

To create this large, enriched dataset of categorized websites, contributors clicked provided links and selected a main and sub-category for URLs. The 31,000+ sites are in a variety of languages and have been split into the following main categories (with each having multiple sub-categories as well):

![summary](https://github.com/YipingNUS/figure8-contextual-dataset/blob/master/img/summary.png)


