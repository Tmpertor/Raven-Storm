# <center>Raven-Storm</center>

In this part, we will learn about performing with adjustment.

## Adjust threads:
- You can see threads as the main part of the strength.
- It is the number of jobs to use which execute your command.
- ```set threads {200}```
- It can depend on the strength of the computer.


## Adjust the message:
- This is the message that will be sent to the target.
- You can change it using:
- ```set message {test}```


## Adjust sleep:
- This will define the time between each start of a new thread.
- ```auto step {0.5}```


## Adjust the method:
- By entering ```method```you will be able to change from UDP flood to TCP flood.


## Adjust the text repetition:
- This command will repeat the message string, that is sent to the target.
- ```set r {2}```
- Text: r:1 = byte ; r:2 = bytebyte


## Adjust size:
- The message equals size.
- ```set MB {5}```
- Each request would be 5 MB.


## Adjust request time:
- Each thread sends after 0 seconds the next request, you can change this though.
- ```set sleep {0.5}```


(Threads x = Requests per second)
