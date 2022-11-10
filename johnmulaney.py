from email import message
from http import server
from sys import prefix
from discord.ext import commands
from discord.utils import get
import time, random, discord

A = ["And maybe you have a baby!",
"AH HAHAHA! I TAKE YOUR MILK-",
"AH HAHAHA! MY TITLE OF ALPHA-",
"AND MY MOM SAID 'YES'!",
"AND NOW WE HAVE NO ROOM FOR THE 'Y'",
"And then you go to write birthday, and you totally forget the lesson you just learned with happy.",
"AND ONE DAY YOUR BABY GOES 'UGHHH MY HEAD'-",
"AND YOU GO 'HEY I GOT SOMETHING FOR YA LITTLE GUY!'",
"'AWHHH, SHE'S UGLY-'", #urmom
"Anal contusions"]

B = ["BECAUSE IT'S THE ONE THING YOU CAN'T REPLACE",
"Because we're delta airlines, and life is a fucking nightmare~",
"BLOCKLETTERS AND CURSIVE LOOK GOOD TOGETHER??",
"BIG ASS B-",
"BECAUSE I KNOW YOU'LL BE DISAPPOINTED WHEN YOU OPEN UP THE DUFFLE BAG AND YOU REALISE IT'S NOT COCAINE AND IT'S LIKE POWDERED BABY ASPIRIN OR WHATEVER THEY DO-",
"BUT AT LEAST YOU HAVE BABY ASPIRIN??",
"But I figured noooo, I wouldn't do that.",
"But I was never sure.",
"BREAD IS GOD- IS BREADDD!"]

C = ["COCKSUCKER",
"Could be a nursery🥺"]

D = ["Duffle bag of fake cocaine.",
"Delta airlines.",
"DISH NOW!",
"Did I do that?"]

E = ["Eat ass, suck a dick and sell drugs💃🫦🫣🤩"]

F = ["FOLLOWED BY A BIG-ASS A- ",
"FOR SOMEONE TO TELL ME TO GO READ JANE AUSTEN- AND THEN I DIDN'T!"]

G = ["'GOD CAN'T HEAR YOU!'",
"GO AHEAD AND LAUGH, HIS NAME IS REDICULOUS!",
"GIVE US SOME MONEY!!"]

H = ["HOW ARE YOU BETTER THAN A NAZI??",
"HAHAHAHAHAHA! HAHAHAHAHA!",
"HAVE YOU EVER SEEN A GHOST??",
"HEY CAN I WALK YA HOME? HEY CAN I WALK YA HOME? HEY CAN I WALK YA HOME-"]

I = ["I WAS OVER ON THE BENCH!",
"I am a teenager asleep in bed.",
"I PAID A HUNDRED AND TWENTY THOUSAND DOLLARS-",
"I AM HOMELESS",
"I AM GAY",
"I HAVE AIDS",
"I'M NEW IN TOWN!",
"I'M SORRYYY!",
"'I think there's a carnival barker in the bathroom? Someone's trying to drum up the business for a carnival-'",
"I am very small… and I have no money… so you can imagine the kind of stress that I am under.",
"I'm so horny and angry all the time.. So, eggs."]

J = ["JOHN MULANEY BULL QUESTIONMARK??",
"JJ BITTENBINDER "]

K = ["KICK UPWARD AT 'EM!"]

L = ["LOOK AT THAT HIGH WAISTED MAN! HE'S GOT FEMININE HIPS!",
"Like we're space aliens in a play about humans that they wrote but they didn't work that hard on.",
"LIKE IT WAS INTRUIGING"]

M = ["MY FATHER ONCE LIFTED ME UP IN CHURCH!",
"MMMM DINNER! MMMM GOOD DINNER! MMMM WE'RE EATING DINNER!",
"MY FAMILY WATCHING AS I SWEAT VODKA AND EXSTACY!"]

N = ["NOOOOO~",
"NO, I TAKE IT BACK"]

O = ["OH! OH GOD! OH NO-",
"Oh but the past is the past!",
"OTHER THAN IF YOU BOUGHT LIKE A DUFFLE BAG OF FAKE COCAINE",
"OOOOOOH-",
"OKAYYYY-"]

P = ["PWAAHHH PWAH WHATS NEW PUSSYCAT",
"PEPPAAAAAA!",
"PSSHH! YOU'RE NOT GONNA FAINT!"]

Q = ["QUACK QUACK-",
"Question mark?"]

R = ["REAL SKINNY P-",
"READING BOOKS THAT I DIDN'T READ!",
"Relax."]

S = ["SCATTER!",
"So I'll go and book a ticket on some garbage airline",
"SORT OF LIKE A MOTORCYCLE SIDECAR SITUATION",
"SO WE'LL DO A SORT-OF CURLED UP NOODLE Y",
"STROLLING ACROSS THE STAGE!",
"SOMEONE'S IN HEEEREE! SOMEONE'S IN HEREE!",
"'Somebody took a shit on my dad's computer…'",
"SHUT UP, YOU'RE ALL GONNA DIE-",
"STREET SMARTS!"]

T = ["THROW THEM OFF THEIR RHYTHM!",
"The newspaper hit me in the face-",
"THEN WE'LL PUT THE SECOND P BELOW THE FIRST P",
"THE SUN IN MY EYES!",
"TO RECEIVE A 4 YEAR DEGREE IN A LANGUAGE I ALREADY SPOKE!",
"THAT IS THE WORST USE OF A HUNDRED AND TWENTY THOUSAND DOLLARS I CAN POSSIBLY FATHOM!",
"THAT'S A BETTER USE OF THE MONEY",
"TOO OLD TO BE A DUCKLING",
"THE INSIDE PART??",
"TELL HIM WE'RE HERE!",
"THE PASSWORDS HAVE PASSED, YOU'VE CORRECTLY GUESSED- BUT NOW IT'S TIME FOR THE ROBOT TEST!!"]

U = ["'UGHHH MY HEAD'",
"'UUUUGH', you know, life?"]

V = ["Very silly person"]

W = ["We've all made a happy birthday sign.",
"WHICH IS THE BEST ANSWER!",
"WITH A HIGH HUMP- WITH A HIGH HUMP!",
"WHYYYYY?? WHY DO YOU DO THIS???",
"Why buy the cow, question mark?",
"WE WANT A GIFT! BUT ONLY IF IT'S MONEY!!",
"WE WERE LIKE DOGS WITHOUT HORSES- WE WERE RUNNING WILD!"]

X = ["Xanax"]

Y = ["YOU'RE A LITTLE FAT GIRL AREN'T YOU??",
"YOU'RE NOT EATING DINNER, COCKSUCKER!"]

Z = ["Zoo-guy is like 'ohh, he must be in the inside part-'"]

prefix = "john"

intents = discord.Intents.default()
intents.members = True

bot = discord.Client(intents=discord.Intents.all())

token = "MTA0MDE3ODMxNTEwMjc4MTQ4MA.GwLVa8.r-kg8vSI36bfTuBzJhync-BPDiiFBC0VtHmHdM"


@bot.event
async def on_ready():
    print("{0.user} is online!".format(bot))

@bot.event
async def on_message(message):

    if message.content.lower() == prefix + " a":
        await message.channel.send(random.choice(A))
    if message.content.lower() == prefix + " b":
        await message.channel.send(random.choice(B))
    if message.content.lower() == prefix + " c":
        await message.channel.send(random.choice(C))
    if message.content.lower() == prefix + " d":
        await message.channel.send(random.choice(D))
    if message.content.lower() == prefix + " e":
        await message.channel.send(random.choice(E))
    if message.content.lower() == prefix + " f":
        await message.channel.send(random.choice(F))
    if message.content.lower() == prefix + " g":
        await message.channel.send(random.choice(G))
    if message.content.lower() == prefix + " h":
        await message.channel.send(random.choice(H))
    if message.content.lower() == prefix + " i":
        await message.channel.send(random.choice(I))
    if message.content.lower() == prefix + " j":
        await message.channel.send(random.choice(J))
    if message.content.lower() == prefix + " k":
        await message.channel.send(random.choice(K))
    if message.content.lower() == prefix + " l":
        await message.channel.send(random.choice(L))
    if message.content.lower() == prefix + " m":
        await message.channel.send(random.choice(M))
    if message.content.lower() == prefix + " n":
        await message.channel.send(random.choice(N))
    if message.content.lower() == prefix + " o":
        await message.channel.send(random.choice(O))
    if message.content.lower() == prefix + " p":
        await message.channel.send(random.choice(P))
    if message.content.lower() == prefix + " q":
        await message.channel.send(random.choice(Q))
    if message.content.lower() == prefix + " r":
        await message.channel.send(random.choice(R))
    if message.content.lower() == prefix + " s":
        await message.channel.send(random.choice(S))
    if message.content.lower() == prefix + " t":
        await message.channel.send(random.choice(T))
    if message.content.lower() == prefix + " u":
        await message.channel.send(random.choice(U))
    if message.content.lower() == prefix + " v":
        await message.channel.send(random.choice(V))
    if message.content.lower() == prefix + " w":
        await message.channel.send(random.choice(W))
    if message.content.lower() == prefix + " x":
        await message.channel.send(random.choice(X))
    if message.content.lower() == prefix + " y":
        await message.channel.send(random.choice(Y))
    if message.content.lower() == prefix + " z":
        await message.channel.send(random.choice(Z))

    elif message.content.lower() == prefix + " random":
        n = random.randint(1,26)
        if n == 1:
            await message.channel.send(random.choice(A))
        elif n == 2:
            await message.channel.send(random.choice(B))
        elif n == 3:
            await message.channel.send(random.choice(C))
        elif n == 4:
            await message.channel.send(random.choice(D))
        elif n == 5:
            await message.channel.send(random.choice(E))
        elif n == 6:
            await message.channel.send(random.choice(F))
        elif n == 7:
            await message.channel.send(random.choice(G))
        elif n == 8:
            await message.channel.send(random.choice(H))
        elif n == 9:
            await message.channel.send(random.choice(I))
        elif n == 10:
            await message.channel.send(random.choice(J))
        elif n == 11:
            await message.channel.send(random.choice(K))
        elif n == 12:
            await message.channel.send(random.choice(L))
        elif n == 13:
            await message.channel.send(random.choice(M))
        elif n == 14:
            await message.channel.send(random.choice(N))
        elif n == 15:
            await message.channel.send(random.choice(O))
        elif n == 16:
            await message.channel.send(random.choice(P))
        elif n == 17:
            await message.channel.send(random.choice(Q))
        elif n == 18:
            await message.channel.send(random.choice(R))
        elif n == 19:
            await message.channel.send(random.choice(S))
        elif n == 20:
            await message.channel.send(random.choice(T))
        elif n == 21:
            await message.channel.send(random.choice(U))
        elif n == 22:
            await message.channel.send(random.choice(V))
        elif n == 23:
            await message.channel.send(random.choice(W))
        elif n == 24:
            await message.channel.send(random.choice(X))
        elif n == 25:
            await message.channel.send(random.choice(Y))
        elif n == 26:
            await message.channel.send(random.choice(Z))

bot.run(token)