# NANOPACK
Easily install all my Oxford Nanopore processing and analysis scripts at the same time.

## Installation
`pip install nanopack`
## Updating
`pip install nanopack --upgrade`


## Scripts
**[NanoPlot][1]**: creating many relevant plots derived from reads (fastq), alignments (bam) and albacore summary files. Examples can be found in [the gallery on my blog][2].

**[NanoComp][10]**: comparing multiple runs on read length and quality based on reads (fastq), alignments (bam) or albacore summary files.

**[NanoStat][4]**: Quickly create a statistical summary from reads, an alignment or a summary file.

**[NanoFilt][3]**: Streaming script for filtering a fastq file based on a minimum length and minimum quality cut-off. Also trimming nucleotides from either read ends is an option.

**[NanoLyse][5]**: Streaming script for filtering a fastq file to remove reads mapping to the lambda phage genome (control DNA used in nanopore sequencing). Uses [minimap2/mappy][9].


## Modules
**[nanoget][6]**: Functions for extracting features from reads, alignments and albacore summary data, parallelized.  

**[nanomath][7]**: Functions for mathematical processing and calculating statistics.  

**[nanoplotter][8]**: Appropriate plotting functions, building on the [seaborn][11] module.



  [1]: https://github.com/wdecoster/NanoPlot
  [2]: https://gigabaseorgigabyte.wordpress.com/2017/06/01/example-gallery-of-nanoplot/
  [3]: https://github.com/wdecoster/nanofilt
  [4]: https://github.com/wdecoster/nanostat
  [5]: https://github.com/wdecoster/nanolyse
  [6]: https://github.com/wdecoster/nanoget
  [7]: https://github.com/wdecoster/nanomath
  [8]: https://github.com/wdecoster/nanoplotter
  [9]: https://github.com/lh3/minimap2
  [10]: https://github.com/wdecoster/nanocomp
  [11]: https://seaborn.pydata.org/
