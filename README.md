Google 2016 STEP Class 6 - Travelling Salesman Problem Challenges
====

[![Join the chat at https://gitter.im/hayatoito/google-step-tsp](https://badges.gitter.im/hayatoito/google-step-tsp.svg)](https://gitter.im/hayatoito/google-step-tsp?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[Hayato Ito](https://github.com/hayatoito) (hayato@google.com)

1. Problem Statement
----

In this assignment, you will design an algorithm to solve a fundamental problem
faced by every travelling salesperson, called *Travelling Salesman Problem*
(TSP).  I’ll explain TSP using a whiteboard in the onsite class, July 1.  TSP
is very famous problem. See
http://en.wikipedia.org/wiki/Travelling_salesman_problem. You should understand
the problem without any difficulties.

Quoted from [Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem):

> The travelling salesman problem (TSP) asks the following question: Given a
> list of cities and the distances between each pair of cities, what is the
> shortest possible route that visits each city exactly once and returns to the
> origin city?

2. Assignment
----

The assignment is hosted on GitHub,
https://github.com/hayatoito/google-step-tsp.  You can download the assignment
by `git clone`:

    git clone https://github.com/hayatoito/google-step-tsp

I recommend you to [fork](https://help.github.com/articles/fork-a-repo/) this
repository to your own git repository before cloning it. You will be asked to
publish your own git repository later.  Note that this document does not explain
“what is git?’ nor “how to use GitHub?”. It is your responsibility to master the
usage of git and GitHub. Some of the sample scripts included in the repository
are written in Python 3, rather than Python 2. It’s also your responsibility to
install Python 3 into your laptop if you want to run the scripts, though which
is not mandatory.

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

See *3. Data Format Specification* section to know the format of input and
solution files.

### Your tasks

* Solve each TSP by designing and implementing an algorithm.
* Overwrite each solution file, `solution_yours_{0-6}.csv`, with your solution.
* Enter the *path length* of your solution in the [scoreboard], for each challenge. Needless to say, shorter path length is better.
* Publish your git repository, which should include your code and solutions.

[scoreboard]: https://docs.google.com/spreadsheets/d/1BkPU8cEkwvlZatVsxw62GKYxhWREcZywruL4AfasxQg/edit?usp=sharing

### An optional task (Speed challenge)

What matters in this optional task is your program's *speed* (execution time). The path length does not matter as long as it meets the condition.
Your task is:

* Given `input_6.csv`, write a program which outputs a path shorter than `47,000`

Input your program's execution time in the [scoreboard]. Faster (smaller) is better.

You can measure the execution time by `time` command.

```shellsession
$ time yourprogram input_6.csv solution_yours_6.csv
2.96s user 0.07s system 97% cpu 3.116 total
```

In this case, your score is `3.116` (s).

### Visualizer

The demo page of the visualizer is:
http://hayatoito.github.io/google-step-tsp/visualizer/.

The assignment includes a helper Web page, `visualizer/index.html`, which
visualizes your solutions. You need to run a HTTP server on your local machine
to access the visualizer. Any HTTP server is okay. If you are not sure how to
run a web server, use the following command to run the HTTP server included in
the assignment. Make sure that you are in the top directory of the assignment
before running the command.

``` shellsession
./nocache_server.py # For Python 3
./nocache_server.py2.py # If you don’t want to install Python3
```

Then, open a browser and navigate to the
[http://localhost:8000/visualizer/](http://localhost:8000/visualizer/). Note
that visualizer was only tested by Google Chrome.  Using the visualizer is
up-to you. You don’t have to use the visualizer to finish the assignment. The
visualizer is provided for the purpose of helping you understand the problem.

3. Data Format Specification
----

### Input Format

The input consists of `N + 1` lines. The first line is always `x,y`. It is followed by `N` lines, each line represents an i-th city’s location, point `xi,yi` where `xi`, `yi` is a floating point number.

```
x,y
x_0,y_0
x_1,y_1
…
x_N-1,y_N-1
```

### Output Format

Output has `N + 1` lines. The first line should be “index”. It is followed by `N` lines, each line is the index of city, which represents the visitation order.

```
index
v_0
v_1
v_2
…
v_N-1
```

### Example (Challenge 0, N = 5)

Input Example:

```
x,y
214.98279057984195,762.6903632435094
1222.0393903625825,229.56212316547953
792.6961393471055,404.5419583098643
1042.5487563564207,709.8510160219619
150.17533883877582,25.512728869805677
```

Output (Solution) Example:

```
index
0
2
3
1
4
```

These formats are requirements for the visualizer, which can take only properly formatted CSV files as input.

4. Schedule
----

### 2016-07-01 (Fri) 5:00pm (JST)

The class starts. You must bring your laptop.

This class is a kick-off class for the assignment, and will be basically 3 hours
hackathon. You are expected to understand the problem and solve a challenge
with a small N. You can also try a challenge with a large N if you can move
fast in the class.

### From: 2016-07-01 (Fri) 8:00pm - To: 2016-07-08 (Fri) 5:00pm

The deadline of the final submission is the next Friday.

Until the deadline, you are expected to improve your algorithm and enter the
score in the [scoreboard] manually for each challenge. You can update the score
as many times as needed. I highly recommend you to update your score whenever
you can find a shorter path. If you get the best score in the
scoreboard, please announce it at [GitHub Issues] so that other
participants can know that your score is the next target.

You can enter your git repository's location in the [scoreboard] once it is ready. Publish your git repository as soon as possible.
Other participants want to see your code even if your code is work in progress.

You can also enter the visualizer URL so that other students can see how your
salesperson is visiting each city in your solution.

We have two phases before the final submission deadline:

####  The first phase: (- until 2016-07-05 (Tue) 11:59pm)

- You can see (or use) code written in other students freely in this phase.
  Please try to upload your code within the first phase as much as possible so that other students can see your code.
- I will save a snapshot of the [scoreboard] at the end of the first phase to decide the winner(s) of the first phase.

#### The second phase: (From: 2016-07-06 (Wed) 8:00am - To: 2016-07-08 (Fri) 5:00pm)

- In this phase, you are not allowed to see code written by other groups. Please do not try to see code written in other groups in this phase.
- It is okay to use code written in other groups if it is written in the first phase. You do not have to throw it away.
- It is okay to ask any question freely even in this phase.

### 2016-07-05 (Tue) 5:00pm

(Optional) I will hold office hours on next Tuesday at Google Tokyo office 44F. I will be available until 9:00pm. You can leave anytime.

How to attend office hours: I will announce it later at [GitHub Issues].

### 2016-07-08 (Fri) 5:00pm

The next class starts.

We have one-hour wrap-up time in this week's
class. You must bring your laptop. Be ready to explain your code and algorithm.

The top rankers in the scoreboard are expected to explain their approaches and code to other students.
Please be prepare to run your program in the class.

You will also be encouraged to take a look at code written by other students and
understand *their* approaches after the class. Please keep your code *clean* so that other
students can read your code and understand your approach without any
difficulties. Writing readable code is one of the most important skills as a
Software Engineer. I recommend you to update README.md file to explain the
content of your git repository.

5. What’s included in the assignment
----

To help you understand the problem, there are some sample scripts / resources
in the assignment, including, but not limited to:

- `solver_random.py` - Sample stupid solver. You never lose to this stupid one.
- `solution_random_{0-6}.csv` - Sample solutions by solver_random.py.
- `solver_greedy.py` - Sample solver using the greedy algorithm. You should beat this definitely.
- `solution_greedy_{0-6}.csv` - Sample solutions by solver_greedy.py.
- `solution_sa_{0-6}.csv` - Yet another sample solutions. I expect all of you will beat this one too. The solver itself is not included intentionally.
- `solution_yours_{0-6}.csv` - You should overwrite these files with your solution.
- `solution_verifier.py` - Try to validate your solution and print the path length.
- `input_generator.py` - Python script which was used to create input files, `input_{0-6}.csv`
- `visualizer/` - The directory for visualizer.

6. Discussions / Collaboration Rules / Code of Conduct
----

### Discussion

I highly encourage you to exchange an idea between students. If you have any
question, or any idea, please share it at [GitHub Issues] or [Chat Room] in the repository.
It is very important to share your question among all students so that everyone can get
benefit from the discussion there. Other students may have the same
question. Please feel free to answer a question from other students. I will join
the discussion as much as possible.

You might want to
[watch the repository](https://help.github.com/articles/watching-repositories/)
so that you get a notification when new question is posted.

[GitHub Issues]: https://github.com/hayatoito/google-step-tsp/issues
[Chat room]: https://gitter.im/hayatoito/google-step-tsp

### Group

It is okay to work as a group if you prefer. The number of members in one group
should be less than 5. You can exchange anything between the members in the
same group. You can not belong to more than one group at the same time. Please
use one GitHub repository per a group. You should mention who are the members
in `README.md` file. If you are looking for a member, please file an issue to
[GitHub Issues] to recruit members.

### Code of Conduct

Until the final deadline, please refrain from getting an assistance from a person other than the STEP students or me.

In the second phase, please do not try to see code which is written by other groups.
It is okay to share anything, anytime, in the same group.

Use your best judgment when using third party libraries in your code. It is okay to use built-in libraries provided by programming languages.

Please see also [code of conduct](https://online.berklee.edu/about/code-of-conduct), if you are interested in, as a general code of conduct, as a reference.

7. Feedback from me
----

I will make my best effort to answer your questions via:

-   [Chat room] for this class.

-   [GitHub Issues] for this class.

-   Office hours: I will be available.

I will review your code and give you a comment as much as possible, if all of the following conditions are satisfied:

-   Your code is hosted on GitHub. I will use GitHub's code review system. Do not forget to enter your repository's URL in the [scoreboard].

-   Your code is written in one of the followings: C++, Rust, Scala, Python3, Python2, Java, C, JavaScript, Haskell, OCaml, and Emacs Lisp.
    I can not promise to review your code if the code is written in other programming languages. I will do code review with Google Standard.

Please feel free to [mention](https://github.com/blog/821) @hayatoito at
GitHub, anytime if you need my help. I will get notified if you mention
@hayatoito. I will make my best effort to give a comment on your code.

I will not comment much about your approach itself. I will comment mainly about the quality of your code, in terms of readability and efficiency,
and give you an advice about how to improve it.

You can also comment on other student's code at GitHub. Please get familiar with Git and GitHub, and use them effectively as a collaboration tool.
In the first phase, you are encouraged to help other students so that all students can enjoy the assignment.

8. FAQ
----

This FAQ includes the questions and the answers in the last year, 2015, as is. Some Q/A might be obsolete for this year.
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

> Is there any prize for the winner?

[Input what you want]

> Visualizer does not work well on firefox (or any other browsers if you like)

I appreciate if you could send a pull request which fixes the issue. You can consider this as an optional assignment. Your contribution is highly welcome.

2015: This is fixed.

9. Acknowledgments
----

This assignment is heavily inspired by [Discrete Optimization Course on Coursera](https://www.coursera.org/course/optimization).
