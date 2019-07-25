import urllib2
import numpy as np

def calc_cs(hv, element, orbital):
	"""
	hv is the photon energy
	element is a string specifying an element. Use the acronym.
	orbital is a string specifying principal quantum number
	and the angular quantum number (s, p, d, f) or t or '' for total
	"""
	target = "https://vuo.elettra.eu/services/elements/data/"

	if orbital == 't':
		orbital = ''
	
	filename = element + orbital + '.txt'
	
	target = target + filename
	
	data = urllib2.urlopen(target)
	x = np.genfromtxt(data, delimiter='\t')
	return np.interp(hv, x[:, 0], x[:, 3])

