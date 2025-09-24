Using standard command line tools (e.g., head, more, grep) and csvtool, explore the clean_dialog.csv. Use the command line tools to answer the following questions:

1. How big is the dataset?

Using "wc -l [filename]", we can find the dataset is 36860 lines long, minus the header which means the dataset contains 36859 pieces of data.

2. What’s the structure of the data? (i.e., what are the fields and what are values in them)

Use "head -n 2 clean_dialog.csv" to see fields and values. The fields are in order: "title", "writer", "pony", "dialog". The values are episode title, writer, the current character speaking, and their dialog (everything is a string).

3. How many episodes does it cover?

Use csvtool and it's features (col, uniq), piping them together.
Use csvtool col 1 clean_dialog.csv | uniq | wc -l. It covers 198 episodes.

4. During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis.

Some lines of dialog only contain stage directions/non-dialogue which is different than the rest of the data in the field (spoken dialogue).

Task 4:
Use csvtool col 3 clean_dialog.csv | grep -c "Character Name" for each main character to find out the number of times they speak. We found out the total of lines in part 1.
