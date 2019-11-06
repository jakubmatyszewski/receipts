# Receipts.py

Receipts.py is a tool that based on a photo of a receipt can read products listed on it, place where the purchase was made and export it to spreadsheet.

---------

# Receipts pipeline:

- [ ] Download recent images from iCloud
    1. set up a crone
    
- [x] Image recognition/receipt classifier
- [x] Localise fragments that contain text
    1. normalize image
        1. detect rotation
        1. image threshholding
- [ ] Segmentation of text
- [ ] Text classification

- [ ] Upload to spreadsheet
