# Levenshtein Distance

In information theory, linguistics, and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. It is named after the Soviet mathematician Vladimir Levenshtein, who considered this distance in 1965.

# Algorithm

I chose to use a recursive implementation : 

    | Function levenshtein(a,b) is
        |if a.size() == 0 then
            |return b.size()
        |end
        |if b.size() == 0 then
            |return a.size()
        |end

        |indicator <-- a[0] != b[0] ? 1 : 0;
        
        |return Minimum(
            levenshtein(a.substr(1),b) + 1,                     //Deletion
            levenshtein(b.substr(1),a) + 1,                     //Insertion
            levenshtein(a.substr(1), b.substr(1)) + indicator   //Substitution
        );
    |end