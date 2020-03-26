# NANOPACK
Easily install all my long read processing and analysis scripts simultaneously.

## Installation
`pip install nanopack`
## Updating
`pip install nanopack --upgrade`

These scripts are written and tested for Python3, and may not work on Python2.

## Content
### Scripts
**[NanoPlot][1]**: creating many relevant plots derived from reads (fastq), alignments (bam) and albacore summary files. Examples can be found in [the gallery on my blog][2]. NanoPack is also available with a graphical user interface in **[NanoGUI][12]** or as a **[web service](http://nanoplot.bioinf.be)**.

**[NanoComp][10]**: comparing multiple runs on read length and quality based on reads (fastq), alignments (bam) or albacore summary files.

**[NanoQC][14]**: Generating plots to investigate nucleotide composition and quality distribution at the end of reads.

**[NanoStat][4]**: Quickly create a statistical summary from reads, an alignment or a summary file.

**[NanoFilt][3]**: Streaming script for filtering a fastq file based on a minimum length, minimum quality cut-off, minimum and maximum average GC. Also trimming nucleotides from either read ends is an option.

**[NanoLyse][5]**: Streaming script for filtering a fastq file to remove reads mapping to the lambda phage genome (control DNA used in nanopore sequencing). Uses [minimap2/mappy][9].


### Modules
**[nanoget][6]**: Functions for extracting features from reads, alignments and albacore summary data, parallelized.  

**[nanomath][7]**: Functions for mathematical processing and calculating statistics.  

### Test data
**[nanotest][13]** provides small test datasets in fastq, bam and summary format (not included when installing NanoPack)  


  [1]: https://github.com/wdecoster/NanoPlot
  [2]: https://gigabaseorgigabyte.wordpress.com/2017/06/01/example-gallery-of-nanoplot/
  [3]: https://github.com/wdecoster/nanofilt
  [4]: https://github.com/wdecoster/nanostat
  [5]: https://github.com/wdecoster/nanolyse
  [6]: https://github.com/wdecoster/nanoget
  [7]: https://github.com/wdecoster/nanomath
  [9]: https://github.com/lh3/minimap2
  [10]: https://github.com/wdecoster/nanocomp
  [11]: https://seaborn.pydata.org/
  [12]: https://github.com/wdecoster/nanogui
  [13]: https://github.com/wdecoster/nanotest
  [14]: https://github.com/wdecoster/nanoQC

  ## CITATION
  If you use this tool, please consider citing our [publication](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/bty149/4934939).
