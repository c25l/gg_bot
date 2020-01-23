# Gill and Gilbert but it’s AI-generated.
Let me explain what I’m trying here and why. It’s been evident for some time that computers can make text, but it’s a matter of alignment (in the dungeons and dragons sense). Generating extremely lawful text has been possible for decades. It’s boring. Generating chaotic text is much harder. Senselessly chaotic is easy, but getting it to feel human is hard. GPT-2 works. From countless scripts people have generated and bots on twitter (including [mine](https://twitter.com/utilitylimbgpt2)) it’s evident that GPT-2 is great for chaotic evil style text. Seriously, curating this bot involves three things, in increasing order of difficulty: not copying the source tweets too closely, not being just nonsense, and not being so incredibly dark or terrible that I cringe at posting it. I want to try to generate something chaotic good. 

Long story short, the subject needs to be essentially over, so I’m not stomping on anyone’s current work or getting too close to ethical lines, and also it needs to be extremely chaotic good. There was one clear choice: [Pat Gill](https://twitter.com/pizza_suplex) and [Brian David Gilbert](https://twitter.com/briamgilbert)’s former nightmare public access show [Gill and Gilbert](https://twitter.com/gillandgilbert).

## How it’s done.
### Get the goods
First we either have to train directly on the video, or we need to get text transcripts of the shows.  We do the latter with python through the [YouTube transcript api](https://pypi.org/project/youtube-transcript-api/). You’re welcome to follow along with the code and such or just ignore the code portions to discern my intent and then enjoy the results.

### Set up the environment.
Other people have explained how to do this well, and I encourage you to [find them](https://medium.com/@ngwaifoong92/beginners-guide-to-retrain-gpt-2-117m-to-generate-custom-text-content-8bb5363d8b7f) if this doesn’t work for you.

```
pip3 install tensorflow==1.15.0
pip3 install gpt-2-simple
pip install youtube_transcript_api
git clone https://github.com/c25l/gg_bot
cd gg_bot
python3 get.py #get the transcripts
python3 train.py #make that model.
```

So, if you’re making the model, and you have a gpu, and you installed the NIVIDA Cuda drivers, then maybe it’ll go fast and be nice for you. It’s a lot to ask. I’m running on a laptop here, and… it wants to do a “China syndrome” for the entire process which takes _hours_ but… worth it. Do people know what the verb “to China syndrome” even means anymore? I have no idea.

As it goes it’ll occasionally barf out some quotes for you. Good luck with them, have fun, mileage may vary.  These quotes are imagined transcripts of fictional shows, so you’ll have both voices talking back and forth just mashed together, but I find that the structure of conversation is actually pretty good and there’s some influence from each of them sometimes.

For those who are new to this whole thing, you’ll notice it’s printing a line there. The first number is the number of training iterations, the second is the amount of time that has elapsed, the third is the loss, the fourth is the average loss. We want the last two to go down within reason, but if we keep it running for too many iterations the model will memorize the input data and become less fun, really. Also worth noting, the number doesn’t go strictly down, it bounces around a little with a trend downwards, playing games with it to try to make it go only downwards leads only to frustration.

Here’s what happens when we prefix our sessions with “This is a segment called”
```
 now that we've talked about the
things we can do now I think it's time to
really really get into it because
this one comes from at Cubie boy
this is a segment called this is a
segment called we don't know what you
think about Vladivostok
okay so I went to Vladivostok
okay I was very excited to go to
Vladivostok because I thought it would be
exciting it would be a new chapter in
my life and I went to a tiny port in the
middle of nowhere and I saw a bunch of
people eating piping hot soup
and I was like oh that's very Russian
yeah I they said that all the time
that's like that's the thing about Russia
they say like when you're talking about
your love life and you don't know it's
because they don't talk shit and I'm like
well that's not a good way to settle a
debate
```

Sometimes segments organically in the machine conversation with no prompt, too.
```
so yes there's a thing called
segments so I think part of what makes a
good segment is it has to do
with these numbers that we ask for yeah so
in this one we're gonna do oh yeah hi
guys I think it's um it's okay I think
it's um it's okay this is a good one
for us because in this one we're not
gonna actually be able to put any text
but Gil and Gilbert into it so this is a
segment called it is a segment
called human emojis and then we put
our text into the box and then we
check it back at yeah we take care of it that
way Pat
```

They clearly discuss playing some fictional games that seem… fairly legit, really.
```
here's your challenge friend my turn
to play to find your gun it's been a while
since I've played this game well here's
your turn to find your gun and you have
eight points you can spend all of them
to upgrade your gun okay awesome
hmm whoa whoa wow oh man that was a
lot like my real okay but you did it
```

If you want to simulate replicant Pat and Brian to do a segment of your choosing, feel free to generate with that as a prefix, eg “This is a segment called piss constable the next generation”, which the lads seem to decline to do, very in-keeping with expectations.
```
this is a segment called piss constable the next generation
stream is gonna be me and Brian and then
Russell and then piss constable and I'll
be Russell and then you know what
you're gonna be Russell and piss constable
and that's a good its a good idea a
good idea yeah so do we want to do it
in the PC specifically so like we want to
yeah so we can we can run into trouble if
we decide to do it in the console specifically
we can depending on how far along
we are in the game what we decide to
go at this point in the game it's like
yeah we're we're at level three which is
what you get for killing a dog oh and
yeah we have to get a new dog and so
let's see how far we get as far as we
go without piss constable yeah I think
we already have enough of that so
yeah we're okay we're okay
so what's the the new dog here
oh it's a it's a big old beagle it's a
big old thing
```

