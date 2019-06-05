# IonTorrent-error-profiling
Code for the analysis of the error profile of IonTorrent sequencing data

## TODO:

- in python turn the phred scores into a list of numerics

- Figure out how to dereplicate reads... 

- For neural network architecture, figure out how to incorportate multiple input layers...
	- may need to move away from the seq2seq model and find something that can accomidate more varied inputs. Do some research but it may also be possible to just add an additional column next to the one hot encoding on the input layer for the encoder and then have the decoder still only predict an output sequence *TEST THIS WITH THE TOY DATA*
		- maybe bind the avg quality column to the encoder input after one hot encoding, so the input would have the one-hot character columns as well as the PHRED adjacent to it.
		- I think this will work based on the fact that the input and output of a word based seq2seq network don't have to share the same feature space... the additional column on the encoder shouldn't be tied to the feature space of the decoder.
		- Have a look at the code though... would we want to add the PHRED to the decoder inputs, or must this share the same feature space as the decoder outputs. Regardless I've not seen quality info on seq2seq networks explored in the literature, so this could be a novel ml contribution in addition to the applied biology side of things.
		- Double possibly: add a column with the # of contributing reads count to the data processing.

## Data avaliable

## IonTorrent error information