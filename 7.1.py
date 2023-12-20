from astropy.io import fits

# Open a FITS file
hdulist = fits.open(r'C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\data\data\lab 7\M51\b.fits')
hdulist = fits.open(r'C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\data\data\lab 7\M51\b.fits')
hdulist = fits.open(r'C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\data\data\lab 7\M51\b.fits')

# Access the data in the primary HDU (Header Data Unit)
data = hdulist[0].data
hdulist.close()  # Close the FITS file

import matplotlib.pyplot as plt
plt.imshow(data, cmap='Blues')
plt.show()
plt.imshow(data, cmap='Reds')
plt.show()
plt.imshow(data, cmap='Greens')
plt.show()
header = hdulist[0].header
