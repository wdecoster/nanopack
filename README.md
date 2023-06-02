# NANOPACK

Overview of my long read processing and analysis tools.

## Tools

**[NanoPlot][1]**: creating many relevant plots derived from reads (fastq), alignments (bam) and albacore summary files. Examples can be found in [the gallery on my blog][2]. NanoPack is also available as a **[web service](http://nanoplot.bioinf.be)**.

**[NanoComp][10]**: comparing multiple runs on read length and quality based on reads (fastq), alignments (bam) or albacore summary files.

**[NanoQC][14]**: Generating plots to investigate nucleotide composition and quality distribution at the end of reads.

**[Cramino][12]**: Rust replacement for NanoStat - much quicker summary creation of BAM or CRAM files.

**[chopper][16]**: A rust implementation combining NanoLyse and NanoFilt into one faster tool for filtering, trimming, and removing contaminants

**[phasius][15]**: Rust tool to create a graphical representation of the read phasing performance (from BAM/CRAM files)

**[kyber][17]**: Rust tool for a minimalistic and standarized impression of a BAM/CRAM file, optionally comparing 2 or 3 datasets.

## Deprecated (replaced by quicker alternatives)

[NanoStat][4]: Create a statistical summary from reads, an alignment or a summary file.

[NanoFilt][3]: Streaming script for filtering a fastq file based on a minimum length, minimum quality cut-off, minimum and maximum average GC. Also trimming nucleotides from either read ends is an option.

[NanoLyse][5]: Streaming script for filtering a fastq file to remove reads mapping to the lambda phage genome (control DNA used in nanopore sequencing). Uses [minimap2/mappy][9].

## Modules

**[nanoget][6]**: Functions for extracting features from reads, alignments and albacore summary data, parallelized.  

**[nanomath][7]**: Functions for mathematical processing and calculating statistics.  

## Test data

**[nanotest][13]** provides small test datasets in fastq, bam and summary format (not included when installing NanoPack)  

## Installation 

The python scripts are written and tested for Python >= 3.6. With `pip install nanopack` all python tools can be installed simultaneously, but using a conda environment is encouraged. For the rust tools binaries can be downloaded from the releases on the respective GitHub repositories, as well as installation through conda.

  [1]: https://github.com/wdecoster/NanoPlot
  [2]: https://gigabaseorgigabyte.wordpress.com/2017/06/01/example-gallery-of-nanoplot/
  [3]: https://github.com/wdecoster/nanofilt
  [4]: https://github.com/wdecoster/nanostat
  [5]: https://github.com/wdecoster/nanolyse
  [6]: https://github.com/wdecoster/nanoget
  [7]: https://github.com/wdecoster/nanomath
  [9]: https://github.com/lh3/minimap2
  [10]: https://github.com/wdecoster/nanocomp
  [12]: https://github.com/wdecoster/cramino
  [13]: https://github.com/wdecoster/nanotest
  [14]: https://github.com/wdecoster/nanoQC
  [15]: https://github.com/wdecoster/phasius
  [16]: https://github.com/wdecoster/chopper
  [17]: https://github.com/wdecoster/kyber

## CITATION

  If you use this tool, please consider citing our [publication](https://academic.oup.com/bioinformatics/article/39/5/btad311/7160911).
