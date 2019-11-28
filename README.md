#### Dotplot script

A dotplot displays similarities between 2 sequences. This is useful in biology, for example when comparing DNA or RNA. One sequence goes along the horizontal axis and the other along the vertical:


![Dotplot](https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FDot_plot_(bioinformatics)&psig=AOvVaw0Wdi0qmTV9WjY6f19YUJ-p&ust=1574959444749000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLCp3d7riuYCFQAAAAAdAAAAABAp)


![Simple dotplot](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.globalspec.com%2Freference%2F65983%2F203279%2Fthe-dotplot&psig=AOvVaw0Wdi0qmTV9WjY6f19YUJ-p&ust=1574959444749000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLCp3d7riuYCFQAAAAAdAAAAABA3)


Cells in the matrix are highlighted when the corresponding X and Y values are identical. Therefore the diagonal lines in the diagram represent a region which is the same for both sequences. For more information visit [https://en.wikipedia.org/wiki/Dot_plot_(bioinformatics)](https://en.wikipedia.org/wiki/Dot_plot_(bioinformatics))


The dotplot script takes 2 FASTA files and uses the first sequence from each to produce a dotplot and print it to the screen. Options are:
* **-filter**  
  Displays isolated matches in lower case
* **-ascii**  
  Dots represent isolated matches and backslashes represent matches in a sequence to form a line
* **-palindrome**  
  Highlights palindromic sequences
* **-h**  
  Help

