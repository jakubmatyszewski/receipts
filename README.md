# Receipts pipeline:

0) Download recent images from iCloud
 - set up a crone
	
1) Does the image contain receipt or not? ok
2) Localise fragments that contain text
 - normalize image
   - detect rotation
   - image threshholding
3) Segmentation of text
4) Text classification

5) Upload to spreadsheet