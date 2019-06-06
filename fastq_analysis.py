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
def numeric_qual(list_of_fqs):
	"""
	Take the string of Quality Phred scores and turn them into a list of numeric quality scores

	"""
	for read in list_of_fqs:
		read['num_quality'] = [ord(x) for x in list(read['quality'])]



def dereplicate(records):
	"""dereplicate reads and keep a copy of only one each
		keep a list of all the numeric phred scores associated with each read
	"""
	obvs_seqs = set()
	seq_qualities = {}

	for rec in records:
		seq = rec['sequence']
		if seq not in obvs_seqs:
			seq_qualities[seq] = [rec['num_quality']]
			obvs_seqs.add(seq)

		else:
			seq_qualities[seq].append(rec['num_quality'])

	avg_qual = {}

	for s in obvs_seqs:
		#make an array of the quality scores and then average the score for each position
		qual_dat = np.array(seq_qualities[s])
		avg_scores = qual_dat.mean(axis=0)
		avg_qual[s] = avg_scores

	return avg_qual


if __name__ == '__main__':
	

	example_input = '/home/cnuge/Documents/barcode_data/mBRAVE_raw_read_data/GMP-03299)CCDB-S5-0084)CBGMB-00030.fastq'

	data = read_fastq(example_input)
	len(data) #1 123 847 reads... lets see how long the dereplication algorithm I'm making takes
	#^not great it crashes when dereplicating

	#this modifies the dictonary in place
	numeric_qual(data)

	#this is using only the first 100 reads b/c of memory constraints on laptop... try full on server
	dereplicated_data = dereplicate(data[:100])

	len(dereplicated_data)
	v1=list(dereplicated_data.keys())[1]
	dereplicated_data[v1]

