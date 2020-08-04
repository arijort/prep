# Algorithms Preparation

## Algorithm Learning:

[MIT course](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/index.htm)

[Stanford Course, Coursera](https://www.coursera.org/specializations/algorithms)

Both courses are very well structured. If you learn well from videos definitely dig into these.


## Data Structure and Algorithms

Make sure to be very familiar with these concepts and be able to discuss them, when to use them, and how to discuss time and space complexity of solutions that use them.

1. Work with strings and arrays
2. Know how to work with multiple pointers through strings/arrays
3. Work with Hash Tables
4. How to manage trees, in particular binary search trees. Be prepared to discuss BSTs are useful.
5. Solve the matching parenthesis problem
6. Know how to reverse a linked list. It sounds easy but there are many issues to trip over.
7. Understand the basics of sorting. Know bubblesort, insertionsort, quicksort, mergesort, counting sort. Know the time complexities and when it's appropriate to use each.
8. Understand recursion. Know when to use it and what problems it might introduce, i.e. memory usage when the call stack grows without bound.
9. Know Depth-first search (DFS).  Can be done with recursion or with a stack.
10. Know Breadth-first search (BFS). Can be done with recursion or with a queue.
   Note for DFS and BFS: Recognize when it's the appropriate choice. Useful for tree and graph problems.  Note some problems might not look like a BFS/DFS problem but can be transformed into one to enable a solution.
11. Get comfortable with creating a custom data structure e.g. an array of prefix sums, suffix tree, pairs/tuples. Be prepared to explained why and how you use this data structure.

- Leetcode http://leetcode.com/

There are a large number of problems and a very active community for discussions around specific problems and interviews at the tech companies.

Start with easy problems then move to medium when comfortable. 

Premium service adds enhanced searching and filtering of problems.

- [Hackerrank](http://hackerrank.com/)

Free service has many problems and some structured areas focused on certain areas, e.g. specific languages.

- [CodeChef](https://www.codechef.com/)

Free service for practicing coding algorithmic problems. Very supportive community.

- [CodeForces](https://codeforces.com/)

Wide set of coding problems targeted at competitive programming circles. Start with the easier problems and move up.

- [InterviewCake](https://www.interviewcake.com/)

The service is structured as a full course of the algorithms and data structures you need for the interview. The pay service provides additional structure to the learning and practice sessions

- [Pramp](https://www.pramp.com/)

Free Service allowing interview practice in a timed setting. You are paired up with another participant and alternate 45 minutes interview sesssions. I strongly recommend this service for getting used to the timing of the interview and communication with your interview partner.

- [AlgoExpert](https://www.algoexpert.io/product)

This is a pay service with structured learning and practice sessions. The head of this service is very active on youtube: https://www.youtube.com/channel/UCaO6VoaYJv4kS-TQO_M-N_g

- [Interviewing.io](https://interviewing.io/)

This is a pay service for practice with interview problems but I never investigated it.



## System Design

Donne Martin system design primer:

https://github.com/donnemartin/system-design-primer

Use the flash cards if that learning style works for you.

Ensure familiarity with these import concepts:

### CAP theorem
### How to reason about the choice betweeen SQL and noSQL databases
### When and how to use load-balancers
### Caches
### How to separate read traffic

- Anatomy of a System Design Interview https://hackernoon.com/anatomy-of-a-system-design-interview-4cb57d75a53f

Nicely structured article on how to prep for this interview.

Note that these interviews are highly formulaic and your industry experience is very valuable as long as you fit it into this structure.

Overall, communication ability is a key trait to show. Go broad at first and communicate possibilities on where to dive in.

Related links: 
  1. https://hackernoon.com/top-10-system-design-interview-questions-for-software-engineers-8561290f0444
  2. https://hackernoon.com/how-not-to-design-netflix-in-your-45-minute-system-design-interview-64953391a054

  3. Grokking the System Design Interview https://www.educative.io/courses/grokking-the-system-design-interview


For pay service run by the author of the article above.

- Google guidance on the system design interview

https://www.youtube.com/watch?v=Gg318hR5JY0

Important points inculde the following:

Communication: Key on your ability to communicate through the process of solving the given problem.

Under-specified: the problem statement is deliberately under-specified which means you have to ask questions to fill out the overall solution you propose. This is of course a big part of the communication you will be doing.

Scale: At each step, try to estimate where the solution would break as you scale up and what steps you take to scale further. Your scaled solution will likely look very different from an initial proposed solution.

Distributed: remember you are designing a distributed system. Make sure to consider and articulate APIs for how components interact, and where bottlenecks will appear.

Tradeoffs: be prepared to discuss tradeoffs between e.g. latency and throughput. Or between scale and simplicity.

Quantitative: be prepared to make quantitative statements about the proposal including

## Other links for Learning

[Big O cheatsheet](https://www.bigocheatsheet.com/)

[Numbers every programmer should know](https://gist.github.com/jboner/2841832) There are many instances of this. Google for others.

[First person account of how to prepare for the tech interview](https://www.quora.com/How-should-I-prepare-for-a-production-engineer-interview-at-Facebook)

[Quora account of interviewing guidance](https://www.quora.com/I-was-recently-interviewed-at-Google-and-got-rejected-on-the-last-interview-even-though-I-solved-the-problem-right-Why/answer/Sief-Khafagi)

[High Scalability](http://highscalability.com/) for blogs and articles

http://highscalability.com/google-architecture
http://highscalability.com/blog/category/facebook
