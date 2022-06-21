# to make sure there's no unintentional one-to-many or many-to-many from merging tables.
# uses validating merges .merge(validate=) you just need to change the validate argument

albums.merge(tracks, on='aid', validate='one_to_many')

# for verifying concatenations, uses .concat(verify_integrity=False) which is the default value
# this method only check index values and not columns.

pd.concat([inv_feb, inv_mar], verify_integrity=True) # will show an error for overlapping data
pd.concat([inv_feb, inv_mar], verify_integrity=False) # will show the table with overlapping index


