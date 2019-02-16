When writing programs, it's important to make smart programming choices so that code runs most efficiently. Computers seem to take no time evaluating programs, but when scaling programs to deal with massive amounts of data, writing efficient code becomes the difference between success and failure. In computer science, we define how efficient a program is by its runtime.

We can't just time the program, however, because different computers run at different speeds. My dusty old PC does not run as fast as your brand new laptop. Programming is also done in many different languages, how do we account for that in the runtime? We need a general way to define a program’s runtime across these variable factors. We do this with Asymptotic Notation.

With asymptotic notation, we calculate a program’s runtime by looking at how many instructions the computer has to perform based on the size of the program’s input. For example, if I were calculating the maximum element in a collection, I would need to examine each element in the collection. That examining step is the same regardless of the language used, or the CPU that's performing the calculation. In asymptotic notation, we define the size of the input as N. I may be looking through a collection of 10 elements, or 100 elements, but we only need to know how many steps are performed relative to the input so N is used in place of a specific number. If there is a second input, we may define the size of that input as M.

There are varieties of asymptotic notation that focus on different concerns. Some will communicate the best case scenario for a program. For example, if we were searching for a value within a collection, the best case would be if we found that element in the first place we looked. Another type will focus on the worst case scenario, such as if we searched for a value, looked in the entire dataset and did not find it. Typically programmers will focus on the worst case scenario so there is an upper bound of runtime to communicate. It's a way of saying "things may get this bad, or slow, but they won't get worse!"

In this next module, we will learn more about asymptotic notation, how to properly analyze the runtime of a program through asymptotic notation, and how to take into consideration the runtime of different data structures and algorithms when creating programs. Learning these skills will change the way you think when you design programs and it will prepare you for the software engineering world where creating efficient programs is an essential skill.

Let’s dive into the world of asymptotic notation!

Cheetahs. Ferraris. Life. All are fast, but how do you know which one is the fastest? You can measure a cheetah’s and a Ferrari’s speed with a speedometer. You can measure life with years and months.

But what about computer programs? In fact, you can time a computer program, but different computers run at different speeds. For example, a program that takes 12 nanoseconds on one computer could take 45 milliseconds on another. Therefore, we need a more general way to gauge a program’s runtime. We do this with Asymptotic Notation.

Instead of timing a program, through asymptotic notation, we can calculate a program’s runtime by looking at how many instructions the computer has to perform based on the size of the program’s input: N.

For instance, a program that has input of size N may tell the computer to run 5N2+3N+2 instructions. (We will get into how we get this kind of expression in future exercises.) Nevertheless, this is a still a fairly messy and large expression. For asymptotic notation, we drop all of our constants (the numbers) because as N becomes extremely large, the constants will make minute differences. After changing our constants, we have N2+N. If we take each of these terms in the expression and graph them, we see that the N2 term grows faster than the N term.

For example, when N is 1000:

the N2 term is 1,000,000
the N term is 1,000
As you can see, the N2 term is much more significant than the N term. When N is larger than 1000, the difference becomes even more significant. Because the difference is so enormous, we don’t even need to consider the N term when calculating the runtime. Thus, for this program, we would describe the runtime in terms of N2. There are three different ways we could describe the runtime of this program: big Theta or Θ(N2), big O or O(N2), big Omega or Ω(N2). The difference between the three and when to use which one will be detailed in the next exercises.


Common Runtimes
Before we delve into the multiple runtime cases, let’s see the different common runtimes a program could have. Below is a list of common runtimes that run from fastest to slowest.

Θ(1). This is constant runtime. This is the runtime when a program will always do the same thing regardless of the input. For instance, a program that only prints “hello, world” runs in Θ(1) because the program will always just print “hello, world”.
Θ(log N). This is logarithmic runtime. You will see this runtime in search algorithms.
Θ(N). This is linear runtime. You will often see this when you have to iterate through an entire dataset.
Θ(N*logN). You will see this runtime in sorting algorithms.
Θ(N2). This is an example of a polynomial runtime. You will see this runtime when you have to search through a two-dimensional dataset (like a matrix) or nested loops.
Θ(2N). This is exponential runtime. You will often see this runtime in recursive algorithms (Don’t worry if you don’t know what that is yet!).
Θ(N!). This is factorial runtime. You will often see this runtime when you have to generate all of the different permutations of something. For instance, a program that generates all the different ways to order the letters “abcd” would run in this runtime.


****************************************************************************************************************************************
Big Omega (Ω) and Big O (O)
Sometimes, a program may have a different runtime for the best case and worst case. For instance, a program could have a best case runtime of Θ(1) and a worst case of Θ(N). We use a different notation when this is the case. We use big Omega or Ω to describe the best case and big O or O to describe the worst case. Take a look at the following pseudocode that returns True if 12 is in the list and False otherwise:

Function with input that is a list of size N:
    For each value in the list:
        If value is equal to 12:
            Return True
    Return False
    
 
 How many times will the loop iterate? Let’s take a list of size 1000. If the first value in the list was 12, then the loop would only iterate once. However, if 12 wasn’t in the list at all, the loop would iterate 1000 times. If the input was a list of size N, the loop could iterate anywhere from 1 to N times depending on where 12 is in the list (or if it’s in the list at all). Thus, in the best case, it has a constant runtime and in the worst case it has a linear runtime.
 
There are many ways we could describe the runtime of this program:
This program has a best case runtime of Θ(1).
This program has a worst case runtime of Θ(N).
This program has a runtime of Ω(1).
This program has a runtime O(N).
You may be tempted to say the following:

However, this is not true because the program does not have a linear runtime in every case, only the worst case.

In fact, when describing runtime, people typically discuss the worst case because you should always prepare for the worst case scenario! Often times, in technical interviews, they will only ask you for the big O of a program.

Great! Now you know the different types of asymptotic notation and when to use which one! Now, let's delve into more complex program runtimes!

This program has a runtime of Θ(N).
    
    
    
    
