# [Title]

## Build Overview
- **Build Name**: Washington focused seasonal flu build
- **Pathogen/Strain**: Influenza A/H3N1, A/H1N1pdm and  B/Victoria
- **Scope**: HA and NA segments, Washington focused
- **Purpose**: This build supports statewide genomic surveillance for seasonal flu in Washington for real-time public health situational awareness. Sequences are included from Washington State, with contextual sequences of North America and global origin included using a tiered-subsampling scheme. Different than the Nextstrain Team's seasonal flu build, this pipeline allows a more focused look at Washington seasonal flu surveillance as opposed to a more global look at seasonal flu surveillance.

- **Nextstrain Build Locations**:

**Two-year HA builds:**

[https://nextstrain.org/groups/wadoh/flu/seasonal/washington/h1n1pdm/2y/ha] [https://nextstrain.org/groups/wadoh/flu/seasonal/washington/h3n2/2y/ha] [https://nextstrain.org/groups/wadoh/flu/seasonal/washington/vic/2y/ha]

**Two-year NA builds:**

 [https://nextstrain.org/groups/wadoh/flu/seasonal/washington/h1n1pdm/2y/na] [https://nextstrain.org/groups/wadoh/flu/seasonal/washington/h3n2/2y/na] [https://nextstrain.org/groups/wadoh/flu/seasonal/washington/vic/2y/na]

**Three-year HA builds:**

[https://nextstrain.org/groups/wadoh/flu/seasonal/washington/h1n1pdm/3y/ha] [https://nextstrain.org/groups/wadoh/flu/seasonal/washington/h3n2/3y/ha] [https://nextstrain.org/groups/wadoh/flu/seasonal/washington/vic/3y/ha]

**Three-year NA builds:**

[https://nextstrain.org/groups/wadoh/flu/seasonal/washington/h1n1pdm/3y/na] [https://nextstrain.org/groups/wadoh/flu/seasonal/washington/h3n2/3y/na] [https://nextstrain.org/groups/wadoh/flu/seasonal/washington/vic/3y/na]



## Table of Contents
- [Pathogen Epidemiology](#pathogen-epidemiology)
- [Scientific Decisions](#scientific-decisions)
- [Getting Started](#getting-started)
  - [Data Sources & Inputs](#data-sources--inputs)
  - [Setup & Dependencies](#setup--dependencies)
    - [Installation](#installation)
    - [Clone the repository](#clone-the-repository)
- [Run the Build](#run-the-build-with-test-data)
  - [Expected Outputs](#expected-outputs)
  - [Visualizing Results](#visualize-results)
- [Customization for Local Adaptation](#customization-for-local-adaptation)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)


## Pathogen Epidemiology
- Overview:
  - Pathogen type and family
  - Key subtypes/lineages relevant to the build
  - Mode(s) of transmission
- Nomenclature
- Geographic Distribution and Seasonality
  - Summarize where the pathogen has been found globally and/or in the region
  - Any seasonality patterns

- Public health importance
  - Why does surveillance matter for this pathogen.
- Genomic Relevance
  - Why are genomic data useful for this pathogen:
    - detecting lineage shifts
    - detecting emergence of variants
    - outbreak investigations
    - monitoring vaccine escape or antiviral resistance
    - understanding transmission pathways

- Additional Resources
  - Link any additional resources that are helpful in learning about this pathogen
  - Link Pathogen Genomic Profile if we have one created

## Scientific Decisions

Nextstrain builds are designed for specific purposes and not all types of builds for a particular pathogen will answer the same questions. The following are critical decisions that were made during the development of this build that should be kept in mind when analyzing the data and using this build. <!-- *Subsampling, root selection, and reference selection must be included at minimum.* -->

- **Nomenclature**: The nomenclature used by in this build to designate clade names is determined by [X]
- **Subsampling**: Includes all Washington, Idaho, Oregon, and British Columbia human sequences,
- **Root selection**: [Describe the root selected for the build that mutations are called against]
- **Reference selection**: Based off of Nextstrain's seasonal flu reference selection but curated to focus on more recent, regional strains
- **Inclusion/Exclusion**: [Explain why certain sequences may or may not be included/excluded]
- **Other adjustments**: [Explain any other important adjustments]

## Getting Started
*(Provide any context new users should know before using this project.) Some high-level features and capabilities specific to this build include:*

- [Feature 1: Feature 1 is helpful because it allows for X]
- [Feature 2: Feature 2 is helpful because it allows for X]

### Data Sources & Inputs
*(Provide any information on data sources and the inputs needed to run the build)*
This build relies on publicly available data sourced from [data sources].

- **Sequence Data**: Sequence data originate from [GISAID](https://gisaid.org/)
- **Metadata**: Metadata data originate from [GISAID](https://gisaid.org/)
- **Expected Inputs**:
    - `[data]/{subtype}/raw_sequences_{segment}.fasta` (containing viral genome sequences per segment)
    - `[data]/{subtype}/metadata.xlsx` (with relevant sample information)
<!-- - **Private data, if applicable**: -->

### Setup & Dependencies
#### Installation
Ensure that you have [Nextstrain](https://docs.nextstrain.org/en/latest/install.html) installed.

To check that Nextstrain is installed:
```
nextstrain check-setup
```

#### Clone the repository:

```
git clone https://github.com/NW-PaGe/seasonal-flu.git
cd seasonal-flu
```

<!--## Run the Build
*(Explain how to run the build with test data. Example text on how this might be explained is below)* -->

To test the pipeline with the provided example data located in `test_data/` make sure you are located in the build folder `seasonal-flu` before running the build command:

```
nextstrain build .
```

When you run the build using `nextstrain build .`, Nextstrain uses Snakemake as the workflow manager to automate genomic analyses. The Snakefile in a Nextstrain build defines how raw input data (sequences and metadata) are processed step-by-step in an automated way. Nextstrain builds are powered by Augur (for phylogenetics) and Auspice (for visualization) and Snakemake is used to automate the execution of these steps using Augur and Auspice based on file dependencies.

<!-- ### Run the Build with Test Data (Optional)
For builds that do not programmatically pull data from NCBI or another source, include a `test_data/` folder containing a minimal working example of test data that can be successfully executed by the build. -->

### Expected Outputs
The file structure of the repository is as follows with `*`" folders denoting folders that are the build's expected outputs.

```
.
├── README.md
├── Snakefile
├── auspice*
├── clade-labeling
├── config
├── data
├── test_data
├── results*
└── scripts
```
More details on the file structure of this build can be found here (link to Wiki page that contains contents of  Repository File Structure Overview section).

After successfully running the build there will be two output folders containing the build results.

- `auspice/` folder contains: a .json file
- `results/` folder contains:

### Visualize Results
- Dropping .json into auspice.us
- `nextstrain view auspice/*.json`

- Link folks to tree interpretation resources that people can use to make their inferences.


## Customization for Local Adaptation
 *[Brief overview on how to adapt this build for another jurisdiction, such as a state, city, county, or country. Including links to Readmes in other sections that contain detailed instructions on what and how to modify the files]*

This build can be customized for use by other demes, including as states, cities, counties, or countries.

- What files or folders need to be modified in order to adapt for other jurisdictions? If this is lengthy then you can link to a wiki page tab that goes into detail on how someone might adapt this build for their jurisdiction.

## Contributing
For any questions please submit them to our [Discussions](https://github.com/NW-PaGe/seasonal-flu/discussions) page otherwise software issues and requests can be logged as a Git [Issue](https://github.com/NW-PaGe/seasonal-flu/issues).

## License
This project is licensed under a modified GPL-3.0 License.
You may use, modify, and distribute this work, but commercial use is strictly prohibited without prior written permission.

## Acknowledgements

*[add acknowledgements to those who have contributed to this work]*

<!-- Repository File Structure Overview [**Move contents of this section to Wiki**]
(This section outlines the high-level file structure of the repo to help folks navigate the repo. If the build follows the pathogen template repo feel free to make this section brief and link to the pathogen template repo resource)*

Example text below:

This Nextstrain build follows the structure detailed in the [Pathogen Repo Guide](https://github.com/nextstrain/pathogen-repo-guide).
Mainly, this build contains [number] workflows for the analysis of [pathogen] virus data:
- ingest/ [link to ingest workflow] Download data from [source], clean, format, curate it, and assign clades.
- phylogenetic/ [link to phylogenetic workflow] Subsample data and make phylogenetic trees for use in nextstrain.

OR
The file structure of the repository is as follows with `*`" folders denoting folders that are the build's expected outputs.

```
.
├── README.md
├── Snakefile
├── auspice*
├── clade-labeling
├── config
├── new_data
├── results*
└── scripts
```

- `Snakefile`: Snakefile description
- `config/`: contains what
- `new_data/`: contains What
- `scripts/`: contains what
- `clade-labeling`: contains what
-->
