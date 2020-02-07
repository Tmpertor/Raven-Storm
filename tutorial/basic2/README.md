# <center>Raven-Storm</center>

In this part we will learn about performing with adjustment.

Adjust threads:
- You can see threads as the main part of the strength.
- It is the amount of jobs to use which execute your command.
- ```set threads {200}```
- It can depend on the strength of the computer.

Adjust sleep:
- This will define the time between each start of a new thread.
- ```auto step {0.5}```

Adjust the method:
- By entering ```method```you wille be able to change from UDP flood to TCP flood.

Adjust the text repeatition:
- This command will repeat the message string, that is send to the target.
- ```set r {2}```
- Text: r:1 = byte ; r:2 = bytebyte

Adjust size:
- The message equals the size.
- ```set mb {5}```
- Each request would be 5 MB.

Adjust request time:
- Each threads send after 0 seconds the next request, you can change this though.
- ```set sleep {0.5}```

(Threads x Requests per second)
