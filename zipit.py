import zipfile

# name of the final zipfile
zip_file=zipfile.ZipFile('Packages.bz2',"w")
# Name of the file who gonna be ziped
zip_file.write('Packages', compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()