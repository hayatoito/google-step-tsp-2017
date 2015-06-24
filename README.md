Google 2015 STEP Class 5 - Travelling Salesman Problem Challenges
====

Hayato Ito (hayato@google.com)

1. Problem Statement
----

In this assignment, you will design an algorithm to solve a fundamental problem faced by every travelling salesperson, called *Travelling Salesman Problem* (TSP).
I’ll explain TSP using a whiteboard in the onsite class, June 26.
TSP is very famous problem. See http://en.wikipedia.org/wiki/Travelling_salesman_problem. You should understand the problem without any difficulties.

Quoted from [Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem):

> The travelling salesman problem (TSP) asks the following question: Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?

2. Assignment
----

The assignment is hosted on GitHub, https://github.com/hayatoito/google-2015-step-tsp.
You can download the assignment by `git clone`:

    git clone https://github.com/hayatoito/google-2015-step-tsp

I recommend you to [fork](https://help.github.com/articles/fork-a-repo/) this repository to your own git repository before cloning it. You will be asked to publish your own git repository later.
Note that this document doesn’t explain “what is git?’ nor “how to use GitHub?”. It’s your responsibility to master the usage of git and GitHub. Some of the sample scripts included in the repository are written in Python 3, rather than Python 2. It’s also your responsibility to install Python 3 into your laptop if you want to run the scripts, though which is not mandatory.

There are 7 challenges of TSP in the assignment, from N = 5 to N = 2048:

| Challenge    | N (= the number of cities) | Input file  | Output (Solution) file |
| ------------ | -------------------------: | ----------- | ---------------------- |
| Challenge 0  |                          5 | input_0.csv | solution_yours_0.csv   |
| Challenge 1  |                          8 | input_1.csv | solution_yours_1.csv   |
| Challenge 2  |                         16 | input_2.csv | solution_yours_2.csv   |
| Challenge 3  |                         64 | input_3.csv | solution_yours_3.csv   |
| Challenge 4  |                        128 | input_4.csv | solution_yours_4.csv   |
| Challenge 5  |                        512 | input_5.csv | solution_yours_5.csv   |
| Challenge 6  |                       2048 | input_6.csv | solution_yours_6.csv   |

See *3. Data Format Specification* section to know the format of input and solution files.

### Your tasks

* Solve each TSP by designing and implementing an algorithm.
* Overwrite each solution file, `solution_yours_{0-6}.csv`, with your solution.
* Enter the *path length* of your solution in the [scoreboard], for each challenge. Needless to say, shorter path length is better.
* Publish your git repository, which should include your code and solutions.

[scoreboard]: https://docs.google.com/spreadsheets/d/1knGHexwjlFJkRhhpuVtBjQAiI7TaTapysBPMPe0KO3A/edit?usp=sharing

### Visualizer

The demo page of the visualizer is: http://hayatoito.github.io/google-2015-step-tsp/visualizer/.

The assignment includes a helper Web page, `visualizer/index.html`, which visualizes your solutions. You need to run a HTTP server on your local machine to access the visualizer. Any HTTP server is okay. If you are not sure how to run a web server, use the following command to run the HTTP server included in the assignment. Make sure that you are in the top directory of the assignment before running the command.

    ./nocache_server.py # For Python 3
    ./nocache_server.py2.py # If you don’t want to install Python3

Then, open a browser and navigate to the [http://localhost:8000/visualizer/](http://localhost:8000/visualizer/). Note that visualizer was only tested by Google Chrome.
Using the visualizer is up-to you. You don’t have to use the visualizer to finish the assignment. The visualizer is provided for the purpose of helping you understand the problem.

3. Data Format Specification
----

### Input Format

The input consists of `N + 1` lines. The first line is always `x,y`. It is followed by `N` lines, each line represents an i-th city’s location, point `xi,yi` where `xi`, `yi` is a floating point number.

    dx,y
    x_0,y_0
    x_1,y_1
    …
    x_N-1,y_N-1

### Output Format

Output has `N + 1` lines. The first line should be “index”. It is followed by `N` lines, each line is the index of city, which represents the visitation order.

    index
    v_0
    v_1
    v_2
    …
    v_N-1

### Example (Challenge 0, N = 5)

Input Example:

    x,y
    214.98279057984195,762.6903632435094
    1222.0393903625825,229.56212316547953
    792.6961393471055,404.5419583098643
    1042.5487563564207,709.8510160219619
    150.17533883877582,25.512728869805677

Output (Solution) Example:

    index
    0
    2
    3
    1
    4

These formats are requirements for the visualizer, which can take only properly formatted CSV files as input.

4. Schedule
----

### June 26 (Fri), 2015, 5:00 PM JST

The Class 5 starts. You must bring your laptop.

This class is a kick-off class for the assignment and will be basically 3 hours hackathon. You are expected to understand the problem and solve a challenge with a small N. You can also try a challenge with a large N if you can move fast in the class.

### June 29 (Mon), 2015, 6:00 PM JST

(Optional) Office hours. I'll be there. Please follow TA's instructions to join the office hours.

### July 2 (Thu), 2015, 11:59 PM JST

The deadline for submission.

Until the deadline, you are expected to improve your algorithm and enter the score in the [scoreboard] manually for each challenge. You can update the score as many times as needed. I highly recommend you to update your score whenever you can find a shorter path. Remember that other students, as well as me, are interested in your progress. Don’t update the score after the deadline.

You can also enter the visualizer URL so that other students can see how a salesperson is visiting each city in your solution.

After the deadline, you can publish your code and solutions. Input the location of your git repository in the [scoreboard].
You might want to avoid to input the repository location before the deadline because other students don't want to see your code accidentally before the deadline.

### July 3 (Fri), 2015, 5:00 PM JST

The Class 6 starts. You must bring your laptop.

We have one-hour wrap-up time. Be ready to explain your code and algorithm. You will also be encouraged to take a look at code written by other students and understand *their* approaches. Please keep your code *clean* so that other students can read your code and understand your approach without any difficulties. Writing readable code is one of the most important skills as a Software Engineer. I recommend you to update README.md file to explain the content of your git repository.

5. What’s included in the assignment
----

To help you understand the problem, there are some sample scripts / resources in the assignment, including, but not limited to:

* `solver_random.py` - Sample stupid solver. You never lose to this stupid one.
* `solution_random_{0-6}.csv` - Sample solutions by solver_random.py.
* `solver_greedy.py` - Sample solver using the greedy algorithm. You should beat this definitely.
* `solution_greedy_{0-6}.csv` - Sample solutions by solver_greedy.py.
* `solution_sa_{0-6}.csv` - Yet another sample solutions. I expect all of you will beat this one too. The solver itself isn’t included intentionally.
* `solution_yours_{0-6}.csv` - You should overwrite these files with your solution.
* `solution_verifier.py` - Try to validate your solution and print the path length.
* `input_generator.py` - Python script which was used to create input files, `input_{0-6}.csv`
* `visualizer/` - The directory for visualizer.

6. Discussions / Collaboration Rules
----

I highly encourage you to exchange an idea between students. If you have any question, or any idea, please use [GitHub Issues] in the repository. You can create a new issue there to ask a question or share your idea. It's very important to share your question among all students so that everyone can get benefts from the discussion there. Other students may have the same question. Please feel free to answer a question from other students. I'll join the discussion as much as possible.

You might want to [watch](https://help.github.com/articles/watching-repositories/) the repository so that you get notification for any new issues that are created there.

[GitHub Issues]: https://github.com/hayatoito/google-2015-step-tsp/issues

Please refrain from the followings:

* Posting the actual code, including pseudo-code, before the deadline.
* Using code which is not your own.

### Group

It's okay to work as a group if you prefer. The number of members in one group should be less than 5. You can exchange anything between the members in the same group. You can't belong to more than one group at the same time. Please use one GitHub repository per a group. You should mention who are the members in `README.md` file. If you are looking for a member, please file an issue to [GitHub Issues] to recruite members.

You could know the location of code in other groups, accidentally, before the deadline. For example, you can guess the location of the git repository of other groups via visualizer's URL in the [scoreboard]. However, please refrain from taking a look at the code and re-use it. I trust all of you.

7. Feedback from me
----

I promise to review your code and give you code comments as much as possible, if all of the following conditions are satisfied:

*   Your code is hosted on GitHub. I'll use GitHub's code review system. Don't forget to enter your repository's URL in the [scoreboard].
*   Your code is written in one of the followings:
    *   C++, Python, Scala, Java, C, JavaScript, Go, Haskell, Scheme and Emacs Lisp.

        I can't promise to review your code if the code is written in other programming languages.

Please feel free to [mention](https://github.com/blog/821) @hayatoito at GitHub, anytime, even before the deadline. I'll get notification if you mention @hayatoito. I'll do the best effort to give a comment to your code in progress.

I won't comment much about your approach itself before the deadline. I only comment about the quality of your code, in terms of readability and efficiency, and give you an advice about how to improve it.


8. FAQ
----

This FAQ includes the questions and the answers in the last year, 2014. Some Q/A might be obsolete for this year.
Please use [GitHub Issues] for a new question.

> I found a typo in this document.

Please feel free to send a [pull request](https://help.github.com/articles/using-pull-requests/) or file an issue at [GitHub Issues] to improve this document.

> Can I use any programming language?

Yes. It’s one of the most important skills to choose an appropriate programming language case by case.

> Do I have to use the same code for every challenges?

No.

> Is there any limitation of machine resources I can use? Can I use multiple machines? Can I run my algorithm 24 hours?

No limitation at all. You can use any machine resources you have.

> It seems that this document and the scoreboard are publicly viewable. Is this intentional?

Yes. I am a big fan of the transparency. If you have any concerns, please let me know that. I’ll honor your preference. Don’t enter any confidential information.

> Could you give me some hints for a challenge with a large N? I have no ideas how to attack those challenges.

I might add some hints or some useful links to external resources later. Stay tuned. Remember that “Google” is your helpful resource.

> Is there any prize for the winner?

[Input what you want]

> Visualizer doesn’t work well on firefox (or any other browsers if you like)

I appreciate if you could send a pull request which fixes the issue. You can consider this as an optional assignment. Your contribution is highly welcome.

2015: This is fixed.

> スコアボード、一人で何行も使っていい？アルゴリズムを変えたので。

OKです。できるだけ、連続した行を使用してください。（シートには、「行を挿入」できます）

> 自分の出した答えが正しく計算されているか自信がない.. Scoreboard に書いていいものかどうか...。

solution_yours_{n}.csv を自分で更新してから、Visualizer や solution_verifier.py を使用すれば、path length を計算してくれます。ただし、Visualizer は、invalid な solutions でも受け入れてしまいます。

> Web上で見かけた、数式は使っていい？

OK です。

> 来週のプレゼンテーションにむけて、スライドをつくったほうがよいですか？

全員分のプレゼンテーションタイムの時間はとれない気がするので、スライドの準備等は特に必要はないです。それよりは、誰が読んでも理解できるような綺麗なコードを書くことに力を注ぎましょう。あるいは、README.md ファイルにきちんと説明を書いておくほうが、「今」っぽいです。

> Visualizer で 自分のsolution (yours) を表示させるとき: Chrome は以前に読み込んだファイル  [solution_yours_{n}.csv] をキャッシュするので、solution_yours_{n}.csv を修正しても反映されません

「python -m SimpleHTTPServer」の代わりにno-cache-servr.pyを使っていたら毎回現在のsolution_yours_{n}.csvを読み込んでくれるはずです。
※ただし以前SimpleHTTPServerを使っていたら、まだcacheに入っている可能性があるので、以下の対策を使って、一回cacheを無効にして更新してみてください。
http://stackoverflow.com/questions/5690269/disabling-chrome-cache-for-website-development

>  I have implemented the algorithms:
>  * all permutations (which only solves until challenge 1)
>  * Greedy
>  * Random
>  * SA
>  * Genetic algorithm
>  However, I cannot seem to beat the scores for challenges over 3 by hayato-sa. I cannot seem to find any bug in my SA or GA solution, but is there anyway we can see the cooling rate, starting temperature, and ending temperature that you used to get the scores on the scoreboard?

Hidden.

9. Acknowledgements
----

This assignment is heavily inspired by [Discrete Optimization Course on Coursera](https://www.coursera.org/course/optimization).
