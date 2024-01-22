code = """
:D :) :)  :D :) :D  :D :) :P  :S :P  :D :P :P  :D :) :D  :D :D :(  :D :D :D  :/ :)  :D :D
:/  :D :) :D  :D :) :{  :( :)  :D :) :)  :D :) =)  :D :D =)  :D :D =/  ;) :/  :D :D :)  ;) ;)  
:D :) :D  ;) =)  :D :D =/  :D :D :D  ;) =)  :D :D :P  :D :D :/  :D :) ;)  :D :D :P  :( :(  :S 
:P  :D :) ;)  :D :D :P  :D :) :S  :( :(  :S :P  :D :) :P  :D :D :/  :D :) :D  :D :) :{  ;) =)  
:D :) :{  :D :) :D  :D :) :P  :D :D =/  :( :D  =) :{  :D :)  :S :P  :S :P  :S :P  :S :P  :D :D 
:(  :D :) :D  :D :D =/  :D :D :/  :D :D :(  :D :D :)  :S :P  :D :) :)  :D :) =)  :D :D =)  :D 
:D =/  ;) :/  :D :D :)  ;) ;)  :D :) :D  ;) =)  :D :D =/  :D :D :D  ;) =)  :D :D :P  :D :D :/  
:D :) ;)  :D :D :P  :S :P  =/ :)  =/ :D  :S :P  :D :) ;)  :D :D :P  :D :) :S  :S :P  :( :P  :S 
:P  :D :) :P  :D :D :/  :D :) :D  :D :) :{  ;) =)  :D :) :{  :D :) :D  :D :) :P  :D :D =/  :D :)
"""

# Mapping from characters to integers
char_to_int = {':(': 4, ':/': 7, ':D': 1, '=/': 6, ':P': 2, '=)': 5, ';)': 9, ':)': 0, ':{': 8, ':S': 3}

# Decode and print the output for the given inputs
for input_value in [50, 25, 2]:
    decoded_output = "".join(map(chr, [int(str(char_to_int[i]) * input_value) for i in code.split()]))
    print(decoded_output)
