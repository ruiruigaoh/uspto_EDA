# Patent Pending
## An exploratory analysis of the biotech patent landscape through USPTO patent data

This is an exploratory data analysis (EDA) of publicly available datasets from the USPTO (United States Patent and Trademark Office). The bulk of the analysis is done in IPython (via a Jupyter notebook), and heavily features the use of several packages including NumPy, Pandas, and Matplotlib, among others.

The goal of my analysis was to explore how technological development, bureaucracy, and private actors affect patent pendency (the length of time between when a patent application is filed and when it is issued at the USPTO). This Git repo also includes a slide deck that summarizes the main findings of the project.

---

## Data

**Main datasets:**
- Cancer Moonshot Patent Data (available for download from the USPTO website [here](https://www.uspto.gov/ip-policy/economic-research/research-datasets/cancer-moonshot-patent-data))
- Patent Examination Research Dataset -- 2022 release (available for download from the USPTO website [here](https://www.uspto.gov/ip-policy/economic-research/research-datasets/patent-examination-research-dataset-public-pair)). The specific data files that you'll want to download *from the 2022 release* are:
    - `application_data.csv`
    - `correspondence_address.csv`
    - `all_inventors.csv`

**Additional datasets:**
- Cities and Towns of the United States, 2014 (available for download from the University of Texas at Austin [here](https://geodata.lib.utexas.edu/catalog/stanford-bx729wr3020))
- The analysis also produces two small CSV files containing processed data, which are downloadable via the following Google Drive links:
    - `random_sample_examiners.csv`: [download](https://drive.google.com/file/d/1mGrZPvld78x3kFc8xAAiZkvlWtutGvRy/view?usp=sharing)
    - `stratified_sample_examiners.csv`: [download](https://drive.google.com/file/d/1qI618WNMovnz7QraC8Ylp2RcH3GQABJc/view?usp=sharing)

    Once you have downloaded the datasets, you can move it into the empty `data/` subfolder after cloning the Git repo onto your local machine.