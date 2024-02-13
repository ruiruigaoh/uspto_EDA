# "Patent Pending": Exploratory analysis of the biotech patent landscape and patent processing times

**Overview:** This analysis explores historical trends in the processing times of biotech-related patents, and uncovers links between patent processing time and factors such as market shifts, patent law/policy changes, examiner "difficulty", and the technology category of a patent. 

**Why patents?** While not a cornerstone of all industries, patents are extremely valuable to the biotech and pharma industries in particular, given the astronomical costs of pharmaceutical research and development (R&D) and the low overall probability of clinical success (i.e., regulatory approval). In other words, securing patent protection is a *key* mechanism for biotech and pharma companies to recoup the massive upfront investment that drug development requires. Strong and robust patent portfolios are therefore an essential pillar for most companies in these industries.

**Main packages used:** pandas, numpy, matplotlib, seaborn.

**Minor packages:** geopandas, geoplot.

Slide deck that presents and summarizes the main findings of the analysis can be found [here]().

---

## Data

**Main datasets:**
- Cancer Moonshot Patent Data (available for download from the USPTO website [here](https://www.uspto.gov/ip-policy/economic-research/research-datasets/cancer-moonshot-patent-data))
- Patent Examination Research Dataset -- 2022 release (available for download from the USPTO website [here](https://www.uspto.gov/ip-policy/economic-research/research-datasets/patent-examination-research-dataset-public-pair)). The specific data files used in my analysis from the 2022 release are:
    - `application_data.csv`
    - `correspondence_address.csv`
    - `all_inventors.csv`

**Additional datasets:**
- Cities and Towns of the United States, 2014 (available for download from the University of Texas at Austin [here](https://geodata.lib.utexas.edu/catalog/stanford-bx729wr3020))
- The analysis also produces two small CSV files containing processed data, which are downloadable via the following Google Drive links:
    - `random_sample_examiners.csv`: [download](https://drive.google.com/file/d/1mGrZPvld78x3kFc8xAAiZkvlWtutGvRy/view?usp=sharing)
    - `stratified_sample_examiners.csv`: [download](https://drive.google.com/file/d/1qI618WNMovnz7QraC8Ylp2RcH3GQABJc/view?usp=sharing)

If you are interested in reproducing my analysis, once the datasets are downloaded, they can be moved into the empty `data/` subfolder after the repo is cloned.
