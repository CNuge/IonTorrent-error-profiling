# IonTorrent-error-profiling
Code for the analysis of the error profile of IonTorrent sequencing data

## TODO:

- in python turn the phred scores into a list of numerics

- Figure out how to dereplicate reads... 

- For neural network architecture, figure out how to incorportate multiple input layers...
	- may need to move away from the seq2seq model and find something that can accomidate more varied inputs. Do some research but it may also be possible to just add an additional column next to the one hot encoding on the input layer for the encoder and then have the decoder still only predict an output sequence *TEST THIS WITH THE TOY DATA*


## Data avaliable

## IonTorrent error information