#### Dotplot script

A dotplot displays similarities between 2 sequences. This is useful in biology, for example when comparing DNA or RNA. One sequence goes along the horizontal axis and the other along the vertical:


![Dotplot](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Zinc-finger-dot-plot.png/310px-Zinc-finger-dot-plot.png)  
From [https://en.wikipedia.org/wiki/Dot_plot_(bioinformatics)](https://en.wikipedia.org/wiki/Dot_plot_(bioinformatics))


![Simple dotplot](https://images.books24x7.com/bookimages/id_4302/fig180_02.jpg)  
From [https://www.globalspec.com/reference/65983/203279/the-dotplot](https://www.globalspec.com/reference/65983/203279/the-dotplot)


Cells in the matrix are highlighted when the corresponding X and Y values are identical. Therefore the diagonal lines in the diagram represent a region which is the same for both sequences. For more information visit [https://en.wikipedia.org/wiki/Dot_plot_(bioinformatics)](https://en.wikipedia.org/wiki/Dot_plot_(bioinformatics))


The dotplot script requires 2 FASTA files and uses the first sequence from each to produce a dotplot and print it to the screen. Options are:
* **--complement, -c**  
  Finds DNA/RNA complements instead of matches
* **--filter, -f**  
  Displays isolated matches in lower case
* **--palindrome, -p**  
  Displays isolated matches in the other direction in lower case, showing palindromic sequences
* **--ascii, -a**  
  Dots represent isolated matches and slashes represent matches in a sequence to form a line, must be used with --filter or --palindrome
* **--help, -h**  
  Displays a help message


## Advanced features

* The script throws an error an exits if there aren't 2 files specified, or if the files are not in correct FASTA format  
  Each file must exist and can't be empty or have any empty lines, must start with an ID (beginning with '>') and the sequence must be in upper case.
* There is also an error if just --ascii is specified without --filter or --palindrome  
* I used a TDD approach when writing the functions in the script  
* I used mocking in my tests instead of opening files
