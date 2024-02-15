# Dead-Ants

---

[Lista de reproduccion de youtube Dead Ants](https://www.youtube.com/playlist?list=PLxFn4mrvRfPWotozt4CrEjQ70KfkdD1Jh)

---

This program is designed to identify a text string in which, by already established rules, it is determined if the ant is alive. If you want to obtain more information, visit the docs folder and open the file called “IDS347L Dead Ants Scenarios”.
The program has a pre-established sequence of positions of the ants which are saved in a text string in a variable called **“string”**, if you want to change the sequence you only have to modify the variable **“string”**.

## Steps to run the program (Dead Ants):
1. install the library called colorama with the following command (~~~pip install colorama~~~)
2. Modify the **“string”** variable in case you want to try a different sequence than the one
which is predetermined.
3. If you do not have python installed, visit the official website
[download Python](https://www.python.org/downloads/) and download the latest stable version in the
download section
4. Install python if you do not have it installed.
5. restart your computer
6. open the command console and type ~~~“python”~~~ or ~~~“python3”~~~ and the file path
main.py, it should look like this ~~~python ./main.py~~~ or similar.
7. If you do not know how to write the file path, I recommend opening the terminal,
write python and drag the main.py file into the terminal window.

---

### Challenge:
An orderly trail of ants is marching across the park picnic area. It looks something like this:
..ant..ant.ant...ant.ant..ant.ant....ant..ant.ant.ant...ant..
But suddenly there is a rumour that a dropped chicken sandwich has been spotted on the ground ahead. The ants surge forward! Oh No, it's an ant stampede!!
Some of the slower ants are trampled, and their poor little ant bodies are broken up into scattered bits.
The resulting carnage looks like this:
...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t Can you find how many ants have died?

### general scenarios:
1. We must understand that if we have n points[. , ... , ..] is an indication that there is a space between the ants.
2. When you find the word “ant” it means that an ant is in that space.
3. Since we already know that “ant” is an ant, we could take as a parameter that “an” is the body of the ant and it could be divided only into “a” or “n” and then
it would be followed by a period or some letter.
4. So since we have already identified that “an” is the body, we could take as a
parameter that “t” is the head of the ant and in any case that “t” is not accompanied by the body, that is, “an” then The ant is dead.

### dead ant scenarios:
1. the head “t” is next to a point
2. “t”meets“a”
3. “t” is found next to another “t”

### live ant scenarios:
1. The word “ant” is complete and there are periods in front or behind it.
2. The word “ant” is complete and together with other letters in front of or behind
it, such as “aant”, “anant”, “tant”, “anta”, antan” or “antt”
3. In some cases you could find live ants without separation between them, so it
would look like this: "antant"