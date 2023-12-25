A versatile solution

In 2023, the image of Santa Claus getting into a small sleigh to deliver
presents is a bit outdated. The sled now looks more like a Boeing 737. The
elves are working hard day and night to load it. Perhaps too hard, because many
presents always get lost during loading. Fortunately, Santa Claus has an idea
to prevent disappointed children: He wants to wrap the presents in balloons, so
that they are protected by a layer of air. He has given you the task of finding
out exactly how full the balloons need to be to properly protect the packages.

You are sitting in a dimly lit room at a rickety desk. You have been waiting
for a while for the head elf, with whom you have an appointment, so that she can
tell you how the packing and loading work. Or well, you had an appointment with
her, because she is already more than 10 minutes late. You're just wondering if
she'll show up when the door bangs open and an elf walks in at high speed and
throws a stack of paper down on the table. "Hey... sorry, emergency... packing
machine in hall 15 broken..." the elf pants, looking at you with a sweaty
face. You give her a few seconds to catch her breath and try to be sympathetic.
"Annoying! But glad you're here! What are these-". You don't get a chance to
finish your question. "Sorry, I have to go again," the elf says as she walks out
the door.

You sigh and wonder if this was indeed the head elf.

Instructions

You look at the pile of paper on the desk in front of you. There appears to be
a polygon on each sheet. You take a closer look at the top sheet of paper. There
is a series of coordinates:

(0, 4), (3, -2), (-1, -2), (-2, 0)

Below is a diagram:

         (0,4)
           o
          / \
         /   \
        /     \
(-2,0) o   +   \
        \       \
         o———————o
      (-1,-2)  (3,-2)


You know from previous years that the packages in the sleigh are two-
dimensional, and you immediately recognize this diagram as the outline of a
package. The coordinates are therefore the vertices of a parcel. In the middle,
at the coordinates (0, 0), there is a cross. You assume that the center of the
balloon will be attached to the gift here.

If we draw a circle of radius 4 around the center, we see that all vertices
are in or on the circle. The point at (0, 4) is on the edge of the circle. That
means if we were to make the circle smaller, this point would fall outside the
circle. In this case, the smallest balloon that contains all the points has
radius 4.

Your input consists of a number of lines. Each line describes a package. A line
contains the coordinates (x, y) of the vertices of the parcel. The coordinates
are separated by commas. For each parcel, you need to calculate the radius of
the smallest balloon so that each vertex fits into the balloon when the balloon
is centered on the cross at (0, 0).Download the list of packages

For each package in the list, find the radius of the smallest balloon with
center (0, 0) so that the package fits entirely inside the balloon. Your answer
to part 1 is the sum of these numbers, rounded down to a whole number.

Enter your answer below.


Part 2

So, solved! That was faster than expected, Santa told you that he thought it
would keep you busy for a day. You explained to the elves at the packing machine
what the intention was, and decided to spend the rest of the day playing on your
phone. Your game of Candy Crush is rudely interrupted when the door swings open
for the second time today. The elf you suspect is the head elf remains standing
in the doorway this time. She doesn't look happy.

"What are you doing?" says the elf. You just started level 47, but keep that
to yourself for now. “These balloons are way too inflated.” The elf finally
leaves a silence, in which you could give a response, if you had one. The elf
apparently thinks you are a bit sad, or perhaps she realizes that she is being
very offensive, because she takes a slightly milder tone. “Well, look at it
again.” she says as she places a stack of paper on the table. "I hope you can
find a better solution." she says before walking away.

You sigh and let what just happened sink in for a moment. You put your phone in
your pocket and reluctantly look at the stack.

Instructions

You recognize the top sheet and conclude that this is the same diagram as before.

         (0,4)
           o
          / \
         /   \
        /     \
(-2,0) o       \
        \       \
         o———————o
      (-1,-2)  (3,-2)

A circle has been drawn with a pen over this diagram, the center of which is not
on the cross. At the center of the circle are the coordinates (1, 0.75), and the
radius √11.5625 = 3.400367... is noted.

So your assumption that the balloon must have a center (0, 0) was incorrect.
The balloon can have any center. This makes it a lot harder to find the smallest
balloon that will fit all the points. For the first example, the radius of the
smallest balloon is √11.5625 = 3.400367...

The next sheet of paper contains the following coordinates:

(-1, 0), (1, 4), (1, -4)

The diagram of this package looks like this:

           (1,4)
            o
           /|
          / |
         /  |
(-1, 0) o   |
         \  |
          \ |
           \|
            o
         (1,-4)

In this case, the smallest circle containing all vertices turns out to have
center (1, 0) and radius 4. The points (1, 4) and (1, -4) lie on the edge of the
circle and the point (-1, 0) lies inside the circle.

For each package in the list: find the radius of the smallest balloon so that
the package fits completely inside the balloon. This time you need to choose the
center of the balloon so that the radius is minimum. Take the sum of the radii
of the balloons and round down to a whole number. This number is your answer to
part 2.

The list of packages is the same as for part 1, but if you want you can download
it again.
