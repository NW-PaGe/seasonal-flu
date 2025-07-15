# Seasonal Influenza (A/H1N1, A/H3N2, B/Victoria) (Washington State Focused)

## Build Overview
- **Build Name**: Seasonal Influenza (A/H1N1, A/H3N2, B/Victoria)
- **Pathogen/Strain**: A/H1N1, A/H3N2, B/Victoria
- **Scope**: A/H1N1 (HA), A/H1N1 (NA), A/H3N2 (HA), A/H3N2 (NA), B/Vic (NA), B/Vic	(HA)
- **Purpose**: The purpose of a Washington state-focused seasonal influenza Nextstrain build is to provide real-time genomic surveillance of circulating influenza strains to enhance public health responses and inform vaccination strategies. By analyzing genetic sequences of influenza viruses collected within the state, the build allows epidemiologists and health officials to track viral evolution, identify potential outbreaks, and assess the efficacy of current vaccines. This information is critical for monitoring the spread of influenza and guiding timely interventions to mitigate its impact on the population, ultimately improving overall public health outcomes in Washington state.
- **Nextstrain Build/s Location/s**: https://nextstrain.org/groups/wadoh#seasonal-flu

## Table of Contents
- [Pathogen Background](#pathogen-background)
- [Scientific Decisions](#scientific-decisions)
- [Getting Started](#getting-started)
  - [Data Sources & Inputs](#data-sources--inputs)
  - [Setup & Dependencies](#setup--dependencies)
    - [Installation](#installation)
    - [Clone the repository](#clone-the-repository)
- [Run the Build](#run-the-build-with-test-data)
- [Repository File Structure Overview](#repository-file-structure-overview)
- [Expected Outputs](#expected-outputs)
- [Customization for Local Adaptation](#customization-for-local-adaptation)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

# Pathogen Background
Seasonal influenza is primarily caused by influenza viruses categorized into four main types: A, B, C, and D, with types A and B responsible for the majority of seasonal outbreaks in humans. Among these, the A/H1N1 and A/H3N2 subtypes of influenza A are particularly significant due to their capacity for antigenic drift and shift, which can lead to seasonal epidemics. A/H1N1 emerged in 1918 and re-emerged as a pandemic strain in 2009, typically circulating during the winter months in Washington State. Its frequent mutations highlight the need for continuous surveillance to ensure vaccine effectiveness. A/H3N2, first identified in 1968, is associated with more severe illness and demonstrates a higher mutation rate, complicating vaccine formulation each season.

In addition to influenza A, the B/Victoria lineage of influenza B, which originated in the 1980s, plays a critical role in seasonal epidemics. In Washington, understanding the circulation and evolution of these strains is essential for epidemiologists and public health officials. Ongoing monitoring of A/H1N1, A/H3N2, and B/Victoria allows for timely public health interventions and the implementation of effective vaccination strategies. This proactive approach also facilitates targeted communication efforts to minimize the impact of influenza on the population, thereby enhancing community resilience during the influenza season. Ultimately, the continual adaptation to the evolving landscape of seasonal influenza underscores the importance of vigilant surveillance and responsive health measures.

# Scientific Decisions
Nextstrain builds are designed for specific purposes and not all types of builds for a particular pathogen will answer the same questions. The following are critical decisions that were made during the development of this build that should be kept in mind when analyzing the data and using this build.

- **Subsampling**: [Describe subsampling strategy, focusing on regions, priorities, etc...]
- **Root selection**: [Describe the root selected for the build that mutations are called against]
- **Reference selection**: [Describe the reference selected for the build that was used in alignment]
- **Inclusion/Exclusion**: [Explain why certain sequences may or may not be included/excluded]
- **Other adjustments**: 
    - Prior to March 31, 2023, we selected strains for each build using a custom Python script called [select_strains.py](https://github.com/nextstrain/seasonal-flu/blob/64b5204d23c0b95e4b06f943e4efb8db005759c0/scripts/select_strains.py). With the merge of [the refactored workflow](https://github.com/nextstrain/seasonal-flu/pull/76), we have since used a configuration file to define the `augur filter` query logic we want for strain selection per build.


## Getting Started
Some high-level features and capabilities specific to this build include:

- **A/H1N1, A/H3N2, B/Victoria are Concurently Analyzed**: This build concurrently analyzes all four currently circulating seasonal influenza lineages (A/H3N2, A/H1N1pdm, B/Victoria, and B/Yamagata) utilizing a singular Snakefile with appropriate wildcards. Additionally, we perform analyses on both the hemagglutinin (HA) and neuraminidase (NA) segments of the influenza virus genome while examining datasets that span varying time intervals (e.g., two, three, and six years). Furthermore, the Nextstrain analysis of influenza virus evolution incorporates antigenic and serological data from various World Health Organization (WHO) collaborating centers, enhancing the robustness and depth of the evolutionary insights derived from this comprehensive approach.

- **HA and NA Analysis**: A key aspect of our genomic analysis focuses on two crucial proteins found on the surface of the influenza virus: hemagglutinin (HA) and neuraminidase (NA). This build has been tailored to facilitate the analysis of HA and NA sequences for A/H1N1, A/H3N2, B/Victoria influenza strains. 
  - **Hemagglutinin (HA)**: This protein facilitates the virus's ability to enter host cells by binding to sialic acid receptors on the cell surface. HA is also a primary target for the immune response, making it central to vaccine design. Variations in the HA gene can lead to antigenic drift, where small changes in the virus enable it to evade immune recognition. By tracking HA variations, we can better predict how well current vaccines will perform and make informed decisions regarding updates to vaccine formulations.
  - **Neuraminidase (NA)**: This enzyme plays a vital role in the release of new virions from infected cells, allowing the virus to spread within the host. Like HA, the NA protein is also subject to mutation, which can impact the virus's ability to be effectively targeted by antiviral treatments. Monitoring genetic changes in the NA gene helps us assess the potential for antiviral resistance and remain prepared for changing treatment landscapes.

- **Comparative Analysis of Two-Year Influenza Nextstrain Builds**: The high-level feature of showcasing two-year and three-year builds of A/H1N1, A/H3N2, and B/Victoria influenza strains lies in the comparative analysis of genetic variations and evolutionary trends over time. By examining these influenza strains across different time intervals, public health professionals can identify patterns of antigenic drift and shifts that impact vaccine effectiveness and disease transmission. The two-year build provides insights into recent changes and adaptations of the virus, while the three-year build allows for a broader context of its evolution. This longitudinal analysis enhances the understanding of strain behavior, aids in predicting future outbreaks, and informs timely adjustments to vaccination strategies, ultimately leading to improved public health interventions and better preparedness for seasonal influenza epidemics.

### Data Sources & Inputs
*(Provide any information on data sources and the inputs needed to run the build)*
This build relies on publicly available data sourced from [data sources].

- **Sequence Data**: [Data sources]
- **Metadata**: [Metadata sources]
- **Expected Inputs**:
    - `[data_location]/sequences.fasta` (containing viral genome sequences)
    - `[data_location]/metadata.xls` (with relevant sample information)
- **Private data, if applicable**:

### Setup & Dependencies
#### Installation
Ensure that you have [Nextstrain](https://docs.nextstrain.org/en/latest/install.html) installed.

To check that Nextstrain is installed:
```
nextstrain check-setup
```

#### Clone the repository:

```
git clone https://github.com/[your-github-repo].git
cd [your-github-repo]
```

## Run the Build With Test Data
To test the pipeline with the provided example data located in `xxxx/xxxxx/example_data` run the following command:
```
nextstrain build .  --configfile profiles/example/builds.yaml
```
When you run the build using `nextstrain build .`, Nextstrain uses Snakemake as the workflow manager to automate genomic analyses. The Snakefile in a Nextstrain build defines how raw input data (sequences and metadata) are processed step-by-step in an automated way. Nextstrain builds are powered by Augur (for phylogenetics) and Auspice (for visualization) and Snakemake is used to automate the execution of these steps using Augur and Auspice based on file dependencies.

When the build has finished running, view the output Auspice trees via:
```
nextstrain view auspice/
```

## Run the Build
- <details><summary><b>Quickstart with GISAID Data:</b> In order to run the build, you will first need to download GISAID data. Follow the below instructions on this process by clicking the dropdown arrow:</summary>

  - In order to run the build, navigate to [GISAID](https://gisaid.org/). Select the "EpiFlu" link in the top navigation bar and then select "Search" from the EpiFlu navigation bar. From the search interface, select A/H3N2 human samples collected in the last six months, as shown in the example below.

    ![Search for recent A/H3N2 data](images/01-search-gisaid-for-h3n2.png)

  - Also, under the "Required Segments" section at the bottom of the page, select "HA". Then select the "Search" button. Select the checkbox in the top-left corner of the search results (the same row with the column headings), to select all matching records as shown below.
  
    ![Select all matching records from search results](images/02-gisaid-search-results.png)

  - Select the "Download" button. From the "Download" window that appears, select "Isolates as XLS (virus metadata only)" and then select the "Download" button.

    ![Download metadata](images/03-download-metadata.png)

  - Create a new directory for these data in the seasonal-flu working directory.
    ```
    mkdir -p data/h3n2/
    ```

  - Save the XLS file you downloaded (e.g., `gisaid_epiflu_isolates.xls`) as `data/h3n2/metadata.xls`. Return to the GISAID "Download" window, and select "Sequences (DNA) as FASTA". In the "DNA" section, select the checkbox for "HA". In the "FASTA Header" section, enter only `Isolate name`. Leave all other sections at the default values.

    ![alt text](image-3.png)

  - Select the "Download" button. Save the FASTA file you downloaded (e.g., `gisaid_epiflu_sequences.fasta`) as `data/h3n2/raw_sequences_ha.fasta`.
  </details>
 </details>
</details>
</details>

- <details><summary><b>Run the Nextstrain Workflow:</b> Run the build with the following instructions by clicking the dropdown arrow:</summary>

  -  Run the build with these data to produce an annotated phylogenetic tree of recent A/H3N2 HA data with the following command.
     ```
     nextstrain build . --configfile profiles/gisaid/builds.yaml
     ```

  -  When the workflow finishes running, visualize the resulting tree with the following command.
     ```
     nextstrain view auspice
     ```    

  -  Explore the configuration file for this workflow by opening `profiles/gisaid/builds.yaml` in your favorite text editor. This configuration file determines how the workflow runs, including how samples get selected for the tree. Try changing the number of maximum sequences retained from subsampling from `100` to `500` and the geographic grouping from `region` to `country`. Rerun your analysis by adding the `--forceall` flag to the end of the nextstrain build command you ran above. How did those changes to the configuration file change the tree?

  -  To skip subsampling and use all records that you downloaded from GISAID, set `filters` string in the build configuration file to an empty string as shown in the following subsection of the YAML file.
     ```
     subsamples:
        global:
            filters: ""     
     ``` 

  -  Explore the other configuration files in `profiles/`, to see other examples of how you can build your own Nextstrain workflows for influenza.
    </details>
 </details>
</details>
</details>


> [!IMPORTANT]
> The workflow is optimized for HA and NA segments and requires additional files if you are building other segments! Please click the dropdown arrow to refer to these files.

- <details><summary><b>The following files are required for different lineage and segment builds:</b></summary>

    - reference: "config/{lineage}/{segment}/reference.fasta"
    - annotation: "config/{lineage}/{segment}/genemap.gff"
    - tree_exclude_sites: "config/{lineage}/{segment}/exclude-sites.txt"
    - The workflow assigns clade annotations to non-HA segments from HA, so the `clades` configuration should always point to the HA clade definition TSV.
    - The workflow only has subclade annotations for HA and NA segments, so remove the `subclades` configuration for other segments builds.
</details>
 </details>
</details>
</details>


## Repository File Structure Overview
*(This section outlines the high-level file structure of the repo to help folks navigate the repo. If the build follows the pathogen template repo feel free to make this section brief and link to the pathogen template repo resource)*

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

## Expected Outputs
*(Outline the expected outputs and in which folders to locate them)*

After successfully running the build there will be two output folders containing the build results.

- `auspice/` folder contains: a .json file
- `results/` folder contains:


## Customization for Local Adaptation
 *[Brief overview on how to adapt this build for another jurisdiction, such as a state, city, county, or country. Including links to Readmes in other sections that contain detailed instructions on what and how to modify the files]*
This build can be customized for use by other demes, including as states, cities, counties, or countries.

## Contributing
For any questions please submit them to our [Discussions](insert link here) page otherwise software issues and requests can be logged as a Git [Issue](insert link here).

## License
This project is licensed under a modified GPL-3.0 License.
You may use, modify, and distribute this work, but commercial use is strictly prohibited without prior written permission.

## Acknowledgements

*[add acknowledgements to those who have contributed to this work]*
