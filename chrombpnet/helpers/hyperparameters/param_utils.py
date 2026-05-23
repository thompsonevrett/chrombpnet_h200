import numpy as np
import chrombpnet.training.utils.one_hot as one_hot
import tensorflow as tf
from tf_keras.utils import get_custom_objects
from tf_keras.models import load_model

import chrombpnet.training.utils.losses as losses

def filter_edge_regions(peaks_df, bw, width, peaks_bool):
    """
    Filter regions in bed file that are on edges i.e regions that cannot be used to construct
    input length + jitter length of the sequence
    """
    input_shape = peaks_df.shape[0]

    # left edge case
    filtered = np.array((peaks_df['start'] + peaks_df['summit'] - width//2) < 0)
    peaks_df = peaks_df[~filtered]
    num_filtered = sum(filtered)

    # right edge case
    chrom_to_sizes = bw.chroms()
    filtered = []
    chrs = peaks_df['chr'].values
    starts = peaks_df['start'].values
    summits = peaks_df['summit'].values
    for chrom, start, summit in zip(chrs, starts, summits):
        if start + summit + width//2 > chrom_to_sizes.get(chrom, 0) :
            filtered.append(True)
        else:
            filtered.append(False)
    filtered=np.array(filtered)
    peaks_df = peaks_df[~filtered]
    num_filtered += sum(filtered)

    if peaks_bool:
        print("Number of peaks input: ",input_shape)
        print("Number of peaks filtered because the input/output is on the edge: ", num_filtered)
        print("Number of peaks being used: ",peaks_df.shape[0])
    else:
        print("Number of non peaks input: ",input_shape)
        print("Number of non peaks filtered because the input/output is on the edge: ", num_filtered)
        print("Number of non peaks being used: ",peaks_df.shape[0])
    return peaks_df

def get_seqs_cts(genome, bw, peaks_df, input_width=2114, output_width=1000):
    """
    Output counts (not log counts)
    Output one-hot encoded sequence
    """
    vals = []
    seqs = []
    chrs = peaks_df['chr'].values
    starts = peaks_df['start'].values
    summits = peaks_df['summit'].values
    for chrom, start, summit in zip(chrs, starts, summits):
        sequence = str(genome[chrom][(start + summit - input_width//2):(start + summit + input_width//2)])
        seqs.append(sequence)
        bigwig_vals=np.nan_to_num(bw.values(chrom, 
                            (start + summit) - output_width//2,
                            (start + summit) + output_width//2))
        vals.append(bigwig_vals)
    return (np.sum(np.array(vals),axis=1), one_hot.dna_to_one_hot(seqs))

def load_model_wrapper(model_h5):
    # read .h5 model
    custom_objects={"tf": tf, "multinomial_nll":losses.multinomial_nll}    
    get_custom_objects().update(custom_objects)    
    model=load_model(model_h5)
    print("got the model")
    model.summary()
    return model


