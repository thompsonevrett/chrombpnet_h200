# Bias factorized, base-resolution deep learning models of chromatin accessibility reveal cis-regulatory sequence syntax, transcription factor footprints and regulatory variants

- This repo contains code for the paper [ChromBPNet: Bias factorized, base-resolution deep learning models of chromatin accessibility reveal cis-regulatory sequence syntax, transcription factor footprints and regulatory variants](https://www.biorxiv.org/content/10.1101/2024.12.25.630221v1)
- Wiki with detailed step-by step instructions: https://github.com/kundajelab/chrombpnet/wiki 
- Please contact [Anusri Pampari] (\<first-name\>@stanford.edu) for suggestions and comments. 
- Here is a link to the [slides](https://docs.google.com/presentation/d/1Ow6K8TYN40u7T3ODdo-JRCLuv5fUUacA/edit?usp=sharing&ouid=104820480456877027097&rtpof=true&sd=true), [ISMB talk](https://www.youtube.com/watch?v=3W3JeJvvjLc) and a comprehensive [tutorial](https://github.com/kundajelab/chrombpnet/wiki). Please see the [FAQ](https://github.com/kundajelab/chrombpnet/wiki/FAQ) and file a github [issue](https://github.com/kundajelab/chrombpnet/issues) if you have questions.
- If you are using chrombpnet <= v0.1.3 please refer to the note here - https://github.com/kundajelab/chrombpnet/wiki/Denovo-motif-discovery 
- If you are using chrombpnet repo actively in your project, I strongly recommend adding yourself to the watchers list for updates. Click on the eye symbol (below the star and above the fork symbol to the right). This will keep you informed of all the major updates and bugs posted for this repo.  

Chromatin profiles (DNASE-seq and ATAC-seq) exhibit multi-resolution shapes and spans regulated by co-operative binding of transcription factors (TFs). This complexity is further difficult to mine because of confounding bias from enzymes (DNASE-I/Tn5) used in these assays. Existing methods do not account for this complexity at base-resolution and do not account for enzyme bias correctly, thus missing the high-resolution architecture of these profiles. Here we introduce ChromBPNet to address both these aspects.

ChromBPNet (shown in the image as `Bias-Factorized ChromBPNet`) is a fully convolutional neural network that uses dilated convolutions with residual connections to enable large receptive fields with efficient parameterization. It also performs automatic assay bias correction in two steps, first by learning simple model on chromatin background that captures the enzyme effect (called `Frozen Bias Model` in the image). Then we use this model to regress out the effect of the enzyme from the ATAC-seq/DNASE-seq profiles. This two step process ensures that the sequence component of the ChromBPNet model (called `TF Model`) does not learn enzymatic bias. 

<p align="center">
<img src="images/chrombpnet_arch.png" alt="ChromBPNet" align="center" style="width: 400px;"/>
</p>

## Table of contents

- [Installation](#installation)
- [QuickStart](#quickstart)
- [How-to-cite](#how-to-cite)

## Installation

This section will discuss the packages needed to train a ChromBPNet model. Firstly, it is recommended that you use a GPU for model training and have the necessary NVIDIA drivers and CUDA already installed. You can verify that your machine is set up to use GPU's properly by executing the `nvidia-smi` command and ensuring that the command returns information about your system GPU(s) (rather than an error). Secondly there are two ways to ensure you have the necessary packages to train ChromBPNet models which we detail below,

### 1. Clone the current repo
```
git clone https://github.com/thompsonevrett/chrombpnet_h200.git
```

### 2. Environment setup

Create a clean conda environment with python 3.10 
```
conda create -n chrombpnet-h100-env python=3.10
conda activate chrombpnet-h100-env
```

Install non-Python  requirements via conda
```
conda install -y -c conda-forge -c bioconda samtools bedtools ucsc-bedgraphtobigwig pybigwig meme
```
### 3. Install ChromBPNet 

```
pip install -e .
```
## How to Cite

If you're using ChromBPNet in your work, please cite as follows:

```
@article {Pampari2024.12.25.630221,
	author = {Pampari, Anusri and Shcherbina, Anna and Kvon, Evgeny and Kosicki, Michael and Nair, Surag and Kundu, Soumya and Kathiria, Arwa S. and Risca, Viviana I. and Kuningas, Kristiina and Alasoo, Kaur and Greenleaf, William James and Pennacchio, Len A. and Kundaje, Anshul},
	title = {ChromBPNet: bias factorized, base-resolution deep learning models of chromatin accessibility reveal cis-regulatory sequence syntax, transcription factor footprints and regulatory variants},
	elocation-id = {2024.12.25.630221},
	year = {2024},
	doi = {10.1101/2024.12.25.630221},
	publisher = {Cold Spring Harbor Laboratory},
	URL = {https://www.biorxiv.org/content/early/2024/12/25/2024.12.25.630221},
	eprint = {https://www.biorxiv.org/content/early/2024/12/25/2024.12.25.630221.full.pdf},
	journal = {bioRxiv}
}
```


