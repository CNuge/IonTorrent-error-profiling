import numpy as np

def process_fastq_record(lines=None):
	""" 
	Take the four lines of a fastq record and create a dictonary for the record
	"""
	ks = ['name', 'sequence', 'optional', 'quality']
	return {k: v for k, v in zip(ks, lines)}


def read_fastq(filename):
	""" 
	This function takes a fastq filename and will read in the records in the file,
	constructing a dictonary for each record with the keys: 'name', 'sequence', 'optional', 'quality'.
		
	A list containing the dictonaries for all of the records will be returned.		
	"""
	records = []
	n = 4
	with open(filename, 'r') as file:
		lines = []
		for line in file:
			lines.append(line.rstrip())
			if len(lines) == n:
				record = process_fastq_record(lines)
				records.append(record)
				lines = []

	return records


#turn phred scores into list of numerics
#add a 'quality_nums' key to the dict that stores a list of the values.


def dereplicate(records):
	"""dereplicate reads and keep a copy of only one each
		keep a list of all the numeric phred scores associated with each read
	"""
	obvs_seqs = set()
	seq_qualities = {}

	for rec in records:
		seq = rec['sequence']
		if seq not in obvs_seqs:
			seq_qualities[seq] = [rec['quality_nums']]

	outseq = []
	#for each unique sequence, 
		#return a dict with:
		# single string of the read
		# a read count (len(v))
		# the avg of the qual score for each base, get this using a numpy array
		#

	#return a dict 