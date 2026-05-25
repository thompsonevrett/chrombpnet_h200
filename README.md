# ChromBPNet compatability upgrade and performance optimizations

- Wiki with detailed step-by step instructions: https://github.com/kundajelab/chrombpnet/wiki 

## Installation

This section will discuss the packages needed to train a ChromBPNet model. Firstly, it is recommended that you use a GPU for model training and have the necessary NVIDIA drivers and CUDA already installed. Secondly, on newer hardware (i.e. H200, RTX5000 ada, or newer), CUDA >= v12.0 and corresponding cuDNN is required to run the necessary **Tensorflow** version of **2.21.0**. I have confirmed that CUDA v12.8.0 and cuDNN v9.10.1.4 allows for GPU accelerated training. 

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

Install non-Python requirements via conda
```
conda install -y -c conda-forge -c bioconda samtools bedtools ucsc-bedgraphtobigwig pybigwig meme pango
```
### 3. Install ChromBPNet 

```
pip install -e .
```
## Optimizations Provided in this Repo
### 1. Updated Tensorflow to v2.21.0
**Rationale:** Enable full compatibility with compute capability v9.0 Nvidia GPUs\
**Key Changes:** Updated the minimum Python version to 3.10 and requirements.txt to include tensorflow==2.21.0 and tf-keras==2.21.0

### 2. Implemented tf-keras v2.21.0
**Rationale:** The Keras implementation packaged with Tensorflow created compatability issues with the newer version\
**Key Changes:** Replaced legacy tensorflow.keras references with tf_keras to prevent errors.

### 3. General speed-up optimizations
**Rationale:** Reduce the amount of time required to train the bias and ChromBPNet models\
**Key Changes:**
- Refactored filter_edge_regions and get_seqs_cts to replace Pandas .iterrows() with fast column zip-unpacking loops, significantly reducing startup/loading overhead.
- Added the workers=4 parameter to model.fit() to allow multi-threaded background queue prefetching. This keeps the GPU fully occupied and prevents idle states between epochs.
- Refactored predict_on_batch_wrapper to run predictions in bulk using model.predict on test_generator.cur_seqs instead of batch-by-batch iteration calling model.predict_on_batch(X).

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


