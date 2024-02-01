import re

input_file = "inputs/quiz_practice_posix2.tex"
output_file = "clean_quiz2.txt"

with open(input_file) as f_in, open(output_file, "w") as f_out:

    in_listing = False
    prev_listing = False
    
    for line in f_in:
    
        if line.startswith(r"\begin{lstlisting}"):
            in_listing = True
            prev_listing = True
            
        elif line.startswith(r"\end{lstlisting}"):
            in_listing = False
            prev_listing = True
            
        elif in_listing:
            code = re.sub(r"%.*", "", line).strip()
            code = re.sub(r"^(?!\w)\$", "", code)
            
            if code:
                print(code, file=f_out)
                
        if prev_listing and not in_listing:
            print("", file=f_out)
            prev_listing = False