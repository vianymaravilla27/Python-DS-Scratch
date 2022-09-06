#egrep.py 
import sys,re

#sys.argv is the list of command line arguments
#sys.argv[0] is the name of the program itself
#sys.argv[1]
regex = sys.argv[1]
print("this is", regex)
#for every line passed into the script

for line in sys.stdin:
    # if it matches the regex, write it to stdout
    if re.search(regex,line):
        sys.stdout.write(line)
# cat somefile.txt | python egrep.py "[0-9]" | python  line_count.py