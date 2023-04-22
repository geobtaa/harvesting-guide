## Purpose: This script will read a batch of IIIF JSONs, flatten them, and write them to a CSV.

!!! Warning

	This will lump all the subsections into single fields and the user will still need to split them.

## Step 1

Download all of the JSONs to a local folder using WGET or a browser plugin. If you gather a list of the JSONs into a csv called "filename.csv", this syntax will work:  wget -i filename.csv