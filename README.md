# "Patent Pending": Exploratory analysis of the biotech patent landscape and patent processing times

Though not a cornerstone of all industries, patents are extremely valuable to the biotechnology and pharmaceutical industries in particular, given the astronomical costs of pharmaceutical research and development (R&D) and the low overall probability of clinical success (i.e., regulatory approval). In these industries, securing robust patent protection is a *key* mechanism for companies to recoup the massive upfront investment that drug development requires. In the U.S., the government entity that oversees the regulation and issuance of patents is the United States Patent and Trademark Office (USPTO). 

Using Python, I conducted an exploratory analysis of the USPTO's patent records, focusing specifically on biotech- and pharma-related patents. I investigated historical trends in the processing times of these patents, uncovering insights about how factors such as market shifts, patent law/policy changes, examiner "difficulty", and different technology categories are linked to patent processing times at the USPTO. These insights, summarized below, can be leveraged by life sciences companies to make patent-related business decisions, e.g., planning patent filing timelines as a part of wider business development activities like licensing and R&D strategy. 

## Technical overview

**Main packages:** pandas, numpy, matplotlib, seaborn.

**Other packages:** geopandas, geoplot.

A Jupyter notebook containing code and writeup for the analysis can be found [here](https://github.com/ruiruigao/uspto_EDA/blob/main/uspto_EDA.ipynb).

A slide deck that summarizes the main findings of my analysis can be found [here](https://github.com/ruiruigao/uspto_EDA/blob/main/USPTO_EDA_Python.pdf).

---
## Data

The main dataset used in this analysis contains **~270K** records of cancer research-related patents that were filed at the USPTO from **1976-2016**. To increase the richness and depth of the analysis, additional features from a separate USPTO dataset were pulled in by joining three additional tables to the main dataset on patent application numbers (unique IDs assigned to patent applications).

**USPTO datasets:**
* [Cancer Moonshot Patent Data](https://www.uspto.gov/ip-policy/economic-research/research-datasets/cancer-moonshot-patent-data) 
* Patent Examination Research Dataset -- [2022 release](https://www.uspto.gov/ip-policy/economic-research/research-datasets/patent-examination-research-dataset-public-pair)

**Additional datasets:**
* [2014 Cities and Towns of the United States](https://geodata.lib.utexas.edu/catalog/stanford-bx729wr3020)
* The analysis also produces two small CSV files containing processed data, which are downloadable via the following Google Drive links:
    - `random_sample_examiners.csv`: [download](https://drive.google.com/file/d/1mGrZPvld78x3kFc8xAAiZkvlWtutGvRy/view?usp=sharing)
    - `stratified_sample_examiners.csv`: [download](https://drive.google.com/file/d/1qI618WNMovnz7QraC8Ylp2RcH3GQABJc/view?usp=sharing)

**Note:** Downloaded datasets can be moved into the empty `data/` subfolder in this repo.

---
# Summary of Insights

Every patent begins as a _patent application_ filed at the USPTO. Patent applications need to be _granted_ by an examiner to become legally enforceable; this is a legal decision, and not all patent applications become granted (a sizeable portion are abandoned). For conciseness, the industry term "_pendency_" is used in this analysis to describe the processing time for a patent application to become a granted patent. 


<p align="center" width="100%">
  <img width="70%" src="results/prop-categories-by-year.png"><br>
</p>

**Pendency is affected by changes in patent law and market behavior:** In 1995, patent term was changed from 17 years from the date of grant to 20 years from the filing date. This act effectively shortened patent term for patent applications that took longer than three years to be processed. The graph above, right, shows a sharp spike in the number of applications filed in that year, likely because companies were rushing to file their applications in order to be covered under the previous law before the new law came into effect. Pendency also spiked in that year, likely reflecting the sudden backlog of applications at the USPTO. The graphs also show that despite steadily increasing numbers of applications being filed at the USPTO, the agency has managed to maintain consistent processing times after hitting a maximum in 2005. 


