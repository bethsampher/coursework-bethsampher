#### Testing

Most functions in the script are tested in test_dotplot.py. I tested the command line manually:


**Error if 2 files aren't specified:**  
./dotplot.py  
usage: dotplot.py [-h] [-c] [-f] [-a] [-p] file_a file_b  
dotplot.py: error: the following arguments are required: file_a, file_b


**Error if files can't be read:**  
./dotplot.py nofile nofile  
usage: dotplot.py [-h] [-c] [-f] [-a] [-p] file_a file_b  
dotplot.py: error: argument file_a: can't open 'nofile': [Errno 2] No such file or directory: 'nofile'


**Exits with error if not correct FASTA format:**  
./dotplot.py not_fasta.txt not_fasta.txt  
Error: invalid FASTA file


**Error if --ascii specified alone:**  
./dotplot.py dorothyhodgkin_fasta.txt dorothycrowfoothodgkin_fasta.txt -a  
usage: dotplot.py [-h] [-c] [-f] [-a] [-p] file_a file_b  
dotplot.py: error: --ascii requires --filter or --palindrome


**Help message:**  
./dotplot.py -h  
usage: dotplot.py [-h] [-c] [-f] [-a] [-p] file_a file_b  

Prints dotplot based on matches in sequences from 2 FASTA files. Abnormal exit
if files not in correct format  

positional arguments:  
  file_a            first FASTA file  
  file_b            second FASTA file  

optional arguments:  
  -h, --help        show this help message and exit  
  -c, --complement  instead of matches, finds DNA/RNA complements in sequences  
  -f, --filter      converts fowards lone matches to lowercase  
  -a, --ascii       converts lone matches to dots and joined matches to  
                    slashes, must be used with --filter or --palindrome  
  -p, --palindrome  converts backwards lone matches to lowercase  


Examples of dotplots printing correctly are shown in README_sample_outputs.txt
