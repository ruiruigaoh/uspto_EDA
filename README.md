# "Patent Pending": Exploratory analysis of the biotech patent landscape and patent processing times

Though not a cornerstone of all industries, patents are extremely **valuable to the biotechnology and pharmaceutical industries** in particular, given the astronomical costs of pharmaceutical research and development (R&D) and the low overall probability of clinical success (i.e., regulatory approval). In these industries, securing robust patent protection is a *key* mechanism for companies to recoup the massive upfront investment that drug development requires. In the U.S., the government entity that oversees the regulation and issuance of patents is the United States Patent and Trademark Office (USPTO). 

Using Python, I conducted an exploratory analysis of the USPTO's patent records, focusing specifically on **biotech- and pharma-related patents**. I investigated historical trends in the processing times of these patents, uncovering insights about how factors such as market shifts, patent law/policy changes, examiner "difficulty", and different technology categories are linked to patent processing times at the USPTO. These insights, summarized below, can be leveraged by life sciences companies to make patent-related business decisions, e.g., developing patent portfolios or planning patent filing timelines as a part of wider business development activities, like licensing and R&D strategy. 

---
## Technical overview

**Main packages:** pandas, numpy, matplotlib, seaborn.

**Other packages:** scipy.stats, geopandas, geoplot.

A Jupyter notebook containing code and writeup for the analysis can be found [here](https://github.com/ruiruigao/uspto_EDA/blob/main/uspto_EDA.ipynb).

A slide deck that takes a deeper dive into the findings of my analysis can be found [here](https://github.com/ruiruigao/uspto_EDA/blob/main/USPTO_EDA_Python.pdf).

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
## Summary of Insights

**Background:** Every patent begins as a _patent application_ filed at the USPTO. Patent applications need to be granted (approved) by an examiner (a USPTO official) to become a legally enforceable patent; not all patent applications become granted. Processing time describes the time between when a patent is filed and when it is granted.

* *Trends in patent categories:* Overall, biotech and pharma patents fall into **9 broad technology categories**. The graph below captures the **emergence of technologies** such as **DNA-related patents** in the late 1990's, while technology related to **drugs and pharmaceutical chemistry**, which dominated biotech patent filings before 2000, shows a decreasing trend in recent years. **Data science-related patents are beginning to emerge** and are expected to continue gaining ground as the biotech and pharma industries continue to incorporate AI to accelerate drug discovery and development.

<p align="center" width="100%">
  <img height="400" src="results/prop-categories-by-year"><br>
</p>

* *Processing times vary depending on technology:* Patents related to **radiation detection and measurement** had the **shortest processing times** (median 30 months), while patents related to **living organisms and model systems** had the **longest processing times** (median 42 months). The difference is **statistically significant**. Patents related to more **abstract concepts and natural phenomena** such as **cells, DNA, diagnostics, data science, and living organisms** typically face **longer approval times**, reflecting the fact that U.S. law restricts patents on certain types of inventions, such as those related to abstract concepts and non-manmade objects.

<p align="center" width="100%">
  <img height="500" src="results/pendency-by-category"><br>
</p>

* *Processing time can be affected by changes in patent law and market behavior:* A sharp spike in the number of filed applications can be observed in 1995 in the graph below (right), which could be attributed to **a change in patent term** that occurred in that year. This change in patent term, from 17 years from grant to 20 years from filing, potentially **disadvantaged patents** that took longer than three years to be approved by the USPTO. The sharp rise in applications in 1995 is likely due to companies **rushing to file** before the new law took effect. **Processing time also spiked** in 1995, possibly due to the sudden **influx of applications.** However, the graphs also show a positive outcome. Despite **steadily increasing filings**, the USPTO has managed to **significantly decrease processing times** since 2005, reflecting their ability to **adapt to increasing market demand**.

<p align="center" width="100%">
  <img height="250" src="results/patex-pendency-vs-filing-year"><br>
</p>

* *Examiner 'difficulty' is positively related to processing time:* From a sample of examiners selected from the data, examiner difficulty ranking (sourced from [PatentBots](https://www.patentbots.com/stats/)) is **positively correlated with average processing times**. This means that applications assigned to more 'difficult' examiners tend to experience longer processing times, with a **moderately strong association** (r = 0.62).  

<p align="center" width="100%">
  <img height="400" src="results/examiner-difficulty-pendency"><br>
</p>

---
## Recommendations

The following recommendations are based on the above insights and are intended to help biotech and pharma companes develop more informed patent strategies:

* *Focus on emerging trends, but balance novelty with patentability:* The data suggests a shift in focus from traditional drug and chemical patents to emerging areas like data science. Consider aligning R&D strategy with these emerging fields, but **also be mindful of the potentially longer processing times** associated with emerging technologies, especially those related to natural phenomena (DNA, living organisms) or abstract concepts (AI, software).
* *Expect longer processing times for complex inventions:* Patents related to certain technologies may face longer approval times due to legal restrictions and increased examiner scrutiny -- plan accordingly for these delays.
* *Stay informed about legal changes:* Monitor upcoming changes in patent law, which can potentially impact processing times by creating a spike in filings.
* *Consider examiner difficulty:* Research the assigned examiner's "difficulty" ranking and use regression analysis to potentially estimate a processing time. Conduct more in-depth analysis to investigate potential factors that are associated with faster processing times even for examiners with very high difficulty rankings, and use these findings to guide patent prosecution strategies. 
