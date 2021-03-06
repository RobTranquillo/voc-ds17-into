#!/usr/bin/python3
from renderlib import *
from easing import *
import svg.path
import random
from itertools import permutations

# URL to Schedule-XML
scheduleUrl = 'https://datenspuren.de/2017/fahrplan/schedule.xml'
colors = ['#9e00a0', '#ffe72d', '#ff8600', '#0bc401', '#d40010', '#0049da']
## the colors are stolen from the Easterhack17 intro, in honor of there color flicker preset

def flashImage(frame, rate):
    if(frame % rate == 0):
        return 0

def rndColors():
  return colors[random.randint(0, 5)]

def colorSprayG(g,color):
    objCnt = {1: 32, 2:48, 3:28, 4: 23} #group counts
    framesContent = []
    for i in range(1, objCnt[g]+1):
          if color is 'rnd':
            framesContent += [('sprayG%s_%s'%(g,i),  'style', 'fill', rndColors() )]
          else:
            framesContent += [('sprayG%s_%s'%(g,i),  'style', 'fill', color )]
    return framesContent



def introFrames(args):
    ## flimmern und in Teilen einfügen
    frames = 12
    for i in range(0, frames):
        yield (
           ('sprayG1', 'style', 'opacity', 0),
           ('sprayG2', 'style', 'opacity', 0),
           ('sprayG3', 'style', 'opacity', 0),
           ('sprayG4', 'style', 'opacity', 0),
           ('datenspurende', 'style', 'opacity', 0),
           ('blossKeineDS', 'style', 'opacity', 0),
           ('title', 'style', 'opacity', 0),
           ('subtitle', 'style', 'opacity', 0),
           ('persons', 'style', 'opacity', 0),
           ('id', 'style', 'opacity', 0),
        )

    frames = 30
    for i in range(0, frames):
        scene = [('sprayG2', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.1, 1, frames))]
        scene += colorSprayG(2,"rnd")
        #print(scene)
        yield(scene)

    frames = 30
    for i in range(0, frames):
        scene = [
           ('sprayG2', 'style', 'opacity', 0),
           ('sprayG4', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.2, 0.9, frames)),
        ]
        scene += colorSprayG(4,"rnd")
        yield(scene)

    frames = 30
    for i in range(0, frames):
        scene = [
           ('sprayG4', 'style', 'opacity', 0),
           ('sprayG1', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.2, 0.1, frames)),
        ]
        scene += colorSprayG(1,"rnd")
        yield(scene)

    frames = 10
    for i in range(0, frames):
        scene = [
           ('sprayG1', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.6, 1, frames)),
           ('sprayG2', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.6, 1, frames)),
        ]
        scene += colorSprayG(2,"rnd")
        yield(scene)

    frames = 10
    for i in range(0, frames):
        scene = [
           ('sprayG1', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.6, 1, frames)),
           ('sprayG2', 'style', 'opacity', 1),
           ('sprayG3', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.6, 1, frames)),
           ('sprayG4', 'style', 'opacity', 1),
        ]
        scene += colorSprayG(1,"rnd")
        scene += colorSprayG(2,"rnd")
        scene += colorSprayG(3,"rnd")
        scene += colorSprayG(4,"rnd")
        yield(scene)

    #show whole image for 1 seconds
    frames = 1*fps
    for i in range(0, frames):
        yield(
                ('sprayG1', 'style', 'opacity', flashImage(i, 5)),
                ('sprayG2', 'style', 'opacity', 1),
                ('sprayG4', 'style', 'opacity', 1),
                ('sprayG3', 'style', 'opacity', 1),
        )

    #and one more
    frames = 1*fps
    for i in range(0, frames):
        scene = [
           ('sprayG1', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.2, 0.9, frames)),
           ('sprayG2', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.2, 0.9, frames)),
           ('sprayG3', 'style', 'opacity', flashImage(i, 5)),
           ('sprayG4', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.2, 0.9, frames)),
        ]
        yield( scene )

    frames = 1*fps
    for i in range(0, frames):
        scene = [
            ('sprayG2', 'style', 'opacity', 1),
            ('sprayG4', 'style', 'opacity', 1),
            ('sprayG1', 'style', 'opacity', 1),
            ('sprayG3', 'style', 'opacity', 1),
        ]
        scene += colorSprayG(1,"rnd")
        scene += colorSprayG(2,"rnd")
        scene += colorSprayG(3,"rnd")
        scene += colorSprayG(4,"rnd")
        yield( scene )

    #fade in title, subtitle, persons and id
    frames = 3*fps
    for i in range(0, frames):
        yield(
            ('title', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
            ('subtitle', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
            ('persons', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
            ('id', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
        )


def backgroundFrames(parameters):
        frames = 1*fps
        for i in range(0, frames):
            yield(
              ('logo', 'style', 'opacity', 1),
            )

def outroFrames(args):
  ## Just the spray
  frames = 3*fps
  for i in range(0, frames):
      scene = [
        ('datenspurende', 'style', 'opacity', 0),
        ('blossKeineDS', 'style', 'opacity', 0),
        ('c3voclogo', 'style', 'opacity', 0),
        ('c3voctext', 'style', 'opacity', 0),
        ('bysalogo', 'style', 'opacity', 0),
        ('bysatext', 'style', 'opacity', 0),
        ('sprayG1', 'style', 'opacity', 1),
        ('sprayG2', 'style', 'opacity', 1),
        ('sprayG3', 'style', 'opacity', 1),
        ('sprayG4', 'style', 'opacity', 1),
      ]
      scene += colorSprayG(1,"rnd")
      scene += colorSprayG(2,"rnd")
      scene += colorSprayG(3,"rnd")
      scene += colorSprayG(4,"rnd")
      yield(scene)

  ## headlines + white Spray
  frames = 1*fps
  for i in range(0, frames):
      scene = [
          ('datenspurende', 'style', 'opacity', easeInExpo(i, 0.05, 1, frames)),
          ('blossKeineDS',  'style', 'opacity', easeInExpo(i, 0.05, 1, frames)),
      ]
      scene += colorSprayG(1,"white")
      scene += colorSprayG(2,"white")
      scene += colorSprayG(3,"white")
      scene += colorSprayG(4,"white")
      yield(scene)

  ## headlines + logo + fadein C3Voc
  frames = 3*fps
  for i in range(0, frames):
      yield(
          ('datenspurende', 'style', 'opacity', 1),
          ('blossKeineDS', 'style', 'opacity', 1),
          ('c3voclogo', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
          ('c3voctext', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
          ('bysalogo', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
          ('bysatext', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
      )

  frames = 5*fps
  for i in range(0, frames):
      scene = [
          ('datenspurende', 'style', 'opacity', 1),
          ('blossKeineDS', 'style', 'opacity', 1),
          ('c3voclogo', 'style', 'opacity', 1),
          ('c3voctext', 'style', 'opacity', 1),
          ('bysalogo', 'style', 'opacity', 1),
          ('bysatext', 'style', 'opacity', 1),
      ]
      yield(scene)



def rndPart(group):
  groupCounts = {1: 32, 2:48, 3:28, 4: 23} #group counts
  return random.randint(1, groupCounts[group])

''' Pause version by Rob
def pauseFrames(args):
  #light color changes
  frames = int(0.5*fps)
  scene = []
  groups = [1,2,3,4]
  for cuts in range(0, 10):
    color = rndColors()
    for group in groups:
      for j in range(1,6):
        part = rndPart(group)
        for i in range(0, frames):
          yield([('sprayG%s_%s'%(group, part), 'style', 'fill', color )])

    color = 'white'
    for group in groups:
      for j in range(1,6):
        part = rndPart(group)
        for i in range(0, frames):
          yield( [('sprayG%s_%s'%(group, part), 'style', 'fill', color )])
'''

# Pause by K4lipso: https://github.com/k4lipso/voc-ds17-into/
def pauseFrames(args):
    frames = 12
    for i in range(0, frames):
        yield (
           ('sprayG1', 'style', 'opacity', 0),
           ('sprayG2', 'style', 'opacity', 0),
           ('sprayG3', 'style', 'opacity', 0),
           ('sprayG4', 'style', 'opacity', 0),
           ('datenspurende', 'style', 'opacity', 0),
           ('blossKeineDS', 'style', 'opacity', 0),
           ('title', 'style', 'opacity', 0),
           ('subtitle', 'style', 'opacity', 0),
           ('persons', 'style', 'opacity', 0),
           ('id', 'style', 'opacity', 0),
        )

    frames = 1*fps
    for i in range(0, frames):
        yield(
                ('sprayG1', 'style', 'opacity', 1),
                ('sprayG2', 'style', 'opacity', 1),
                ('sprayG4', 'style', 'opacity', 1),
                ('sprayG3', 'style', 'opacity', 1),
                ('datenspurende', 'style', 'opacity', 1),
        )

    objCnt = {1: 32, 2:48, 3:28, 4: 23}
    #extend loops to get a longer lasting version
    #one loop is about 19 seconds
    loops = 4
    for loop in range(0, loops):
        frames = 2*fps
        sprayX = random.randint(1,4)
        sprayY = random.randint(1,4)
        ratio = random.randint(5,10)
        scene1 = []
        scene1 += colorSprayG(1,"rnd")
        scene1 += colorSprayG(2,"rnd")
        scene1 += colorSprayG(3,"rnd")
        scene1 += colorSprayG(4,"rnd")
        yield(scene1)

        scene2 = []
        for i in range(0, frames):
            scene1 = []
            scene2 = []
            scene1 += [('sprayG%s'%(sprayX), 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.3, 1, frames))]
            scene2 += colorSprayG(sprayX,"rnd")
            yield(scene1)
            #yield scene2 multiple times to slow it a bit down
            for i in range(0, 8):
                yield(scene2)

def debug():
    render('intro.svg',
        '../intro.ts',
        introFrames,
        {
            '$id': 7776,
            '$title': 'Titel des Talks',
            '$subtitle': 'Subtitel des talks',
            '$personnames':  ['pers1','pers2','Frank Nord','Ho! Schi Ming']
        }
    )

    render('outro.svg',
        '../outro.ts',
        outroFrames
    )

    render('pause.svg',
        '../pause.ts',
        pauseFrames
    )

    render(
        'background.svg',
        '../background.ts',
        backgroundFrames
    )


def tasks(queue, args, idlist, skiplist):
    # iterate over all events extracted from the schedule xml-export
    for event in events(scheduleUrl):
        if event['room'] not in ('Goldberg Saal', 'Museumskino', 'Technisches Theater','Add-ons'):
            print("skipping room %s (%s [%s])" % (event['room'], event['title'], event['id']))
            continue
        if not (idlist==[]):
                if 000000 in idlist:
                        print("skipping id (%s [%s])" % (event['title'], event['id']))
                        continue
                if int(event['id']) not in idlist:
                        print("skipping id (%s [%s])" % (event['title'], event['id']))
                        continue

        # generate a task description and put them into the queue
        queue.put(Rendertask(
            infile = 'intro.svg',
            outfile = str(event['id'])+".ts",
            sequence = introFrames,
            parameters = {
                '$id': event['id'],
                '$title': event['title'],
                '$subtitle': event['subtitle'],
                '$persons': event['personnames']
            }
        ))

    # place a task for the outro into the queue
    if not "out" in skiplist:
        queue.put(Rendertask(
            infile = 'outro.svg',
            outfile = 'outro.ts',
            sequence = outroFrames
         ))

    # place the pause-sequence into the queue
    if not "pause" in skiplist:
        queue.put(Rendertask(
            infile = 'pause.svg',
            outfile = 'pause.ts',
            sequence = pauseFrames
        ))

    # place the background-sequence into the queue
    if not "bg" in skiplist:
        queue.put(Rendertask(
            infile = 'background.svg',
            outfile = 'background.ts',
            sequence = backgroundFrames
        ))
