def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count
file = open("newfile.txt", "w")
file.write("""the world is looking for girls and women who can code to
solve their problems.coding is advantageous to learn and its fun,
programmers love to code day and night.sleeping with a problem can actually
solve it.happy coding!""" )
fie.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()

for char in
"abcdefghijklmnopqrstuvwxyz":
     perc = 100 * count_char(text,char) / len(text)
     print("{0} - {1}%".format(char,round(perc,2)))