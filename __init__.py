#!/usr/bin/python3

from renderlib import *
from easing import *

# URL to Schedule-XML
scheduleUrl = 'https://datenspuren.de/2017/fahrplan/schedule.xml'

def introFrames(args):
    ## flimmern und in Teilen einfügen
    frames = 12
    for i in range(0, frames):
        yield(
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
        yield(
           ('sprayG2', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.2, 0.9, frames)),
        )
    frames = 30
    for i in range(0, frames):
        yield(
           ('sprayG2', 'style', 'opacity', 0),
           ('sprayG4', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.2, 0.9, frames)),
        )
    frames = 30
    for i in range(0, frames):
        yield(
           ('sprayG4', 'style', 'opacity', 0),
           ('sprayG1', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.2, 0.9, frames)),
        )
    frames = 10
    for i in range(0, frames):
        yield(
           ('sprayG2', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.6, 1, frames)),
           ('sprayG4', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.6, 1, frames)),
        )
    frames = 10
    for i in range(0, frames):
        yield(
           ('sprayG2', 'style', 'opacity', 1),
           ('sprayG4', 'style', 'opacity', 1),
           ('sprayG1', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.6, 1, frames)),
           ('sprayG3', 'style', 'opacity', "%.4f" % easeInOutBounce(i, 0.6, 1, frames)),
        )
    #show whole image for 2 seconds
    frames = 2*fps
    for i in range(0, frames):
        yield(
           ('sprayG2', 'style', 'opacity', 1),
           ('sprayG4', 'style', 'opacity', 1),
           ('sprayG1', 'style', 'opacity', 1),
           ('sprayG3', 'style', 'opacity', 1),
        )
    #fade in title, subtitle, persons and id
    frames = 2*fps
    for i in range(0, frames):
        yield(
            ('title', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
            ('subtitle', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
            ('persons', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
            ('id', 'style', 'opacity', easeInQuad(i, 0, 1, frames)),
        )


def backgroundFrames(parameters):
    # 40 Sekunden

        frames = 20*fps
        for i in range(0, frames):
            xshift = (i+1) * 300/frames
            yshift = ((i+1) * (150/frames))
            yield(
                ('logo', 'attr', 'transform', 'translate(%.4f, %.4f)' % (xshift, yshift)),
            )

        frames = 20*fps
        for i in range(0, frames):
            xshift = 300 - ((i+1) * (300/frames))
            yshift = 150 - ((i+1) * (150/frames))
            yield(
              ('logo', 'attr', 'transform', 'translate(%.4f, %.4f)' % (xshift, yshift)),
            )

def outroFrames(args):
#fadein outro graphics
    frames = 3*fps
    for i in range(0, frames):
        yield(
            ('logo', 'style', 'opacity', easeInQuad(i, 0.01, 1, frames)),
            ('logotext', 'style', 'opacity', easeInQuad(i, 0.01, 1, frames)),
            ('c3voclogo', 'style', 'opacity', easeInQuad(i, 0.01, 1, frames)),
            ('c3voctext', 'style', 'opacity', easeInQuad(i, 0.01, 1, frames)),
            ('bysalogo', 'style', 'opacity', easeInQuad(i, 0.01, 1, frames)),
            ('bysatext', 'style', 'opacity', easeInQuad(i, 0.01, 1, frames)),
        )
    frames = 3*fps
    for i in range(0, frames):
        yield(
            ('pillgroup', 'style', 'opacity', 1),
            ('logotext', 'style', 'opacity', 1),
            ('c3voclogo', 'style', 'opacity', 1),
            ('c3voctext', 'style', 'opacity', 1),
            ('bysalogo', 'style', 'opacity', 1),
            ('bysatext', 'style', 'opacity', 1),
        )

def pauseFrames(args):
#fade heartgroups
        frames = int(0.5*fps)
        for i in range(0, frames):
                yield (
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                )
        for i in range(0, frames):
                yield (
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                )
        for i in range(0, frames):
                yield (
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                )
        for i in range(0, frames):
                yield (
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                )
        for i in range(0, frames):
                yield (
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                )
        for i in range(0, frames):
                yield (
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                )
        for i in range(0, frames):
                yield (
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                )
        for i in range(0, frames):
                yield (
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                )
        for i in range(0, frames):
                yield (
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 0.25, 0.75, frames)),
                )
        for i in range(0, frames):
                yield (
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                        ('logo', 'style', 'opacity', easeInQuad(i, 1, -0.75, frames)),
                )

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

    '''
    render('outro.svg',
        '../outro.ts',
        outroFrames
    )

    render(
        'background.svg',
        '../background.ts',
        backgroundFrames
    )

    render('pause.svg',
        '../pause.ts',
        pauseFrames
    )
    '''


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
