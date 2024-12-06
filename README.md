# PopPUNK_tools
Guidance and tools to use for building and visualizing PopPUNK databases
Remember - Each statistic is a guiding tool! Remember to check that your clustering patterns make sense. 

# Prep your data
Go to [poppunk_data_prep](https://github.com/DOH-HNH0303/PopPUNK_tools/tree/dev/poppunk_data_prep). Get outta here!


# Easy db builds (for ideal data)
Hahaha you wish it was this easy (and sometimes it is!)

Use the (almost) one-stop-shop [poppunk_easy_run.py](https://github.com/bacpop/PopPUNK/blob/master/scripts/poppunk_easy_run.py) provided to you by PopPUNK. Often, when using this script, its makes sense to use the [suggested k-mer length](https://poppunk.bacpop.org/sketching.html#choosing-the-right-k-mer-lengths) based on the organism type.
```
poppunk_easy_run.py --r-files <refseq>_input.txt  --analysis-args "--threads 8 --min-k 13 --max-k 29  --k-step 3" --output Corynebacterium_diphtheriae --viz --viz-args "'--microreact'"
```
This will create and refine a db using dbscan and creat a Microreact visual

# Not so easy db builds (for more troublesome data)

# Example builds

# General Troubleshooting
Most scripts are created with the assumption that the prefix of a created database are the same prefix used in the files contained within the database. If renaming a database, make sure to edit the prefix od the database files to contain the new matching prefix.


