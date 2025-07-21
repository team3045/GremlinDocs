Section 3: Using Templates to Program
=====================================

Intro to templates
------------------

Templates are a set of operations that already have their settings filled in. This makes the programming much simpler, as you just have to adapt the template to your parts. Although the template massively standardizes the programming process, there are still various skills you’ll need to succeed to be able to CAM your parts.

Basics of Fusion 360 CAD
If you have no experience with Fusion 360, or any CAD program in general, I very highly recommend that you at least familiarize yourself with the basics of the software. There are various differences between Fusion and Onshape, so I recommend spending at least a few hours CADing on fusion. Being familiar with fusion 360 will allow you to better navigate the program, make slight adjustments to parts without having to re-import them, better understand the file structure, and reduce overall frustration.

Here is a tutorial on Fusion 360 CAD.
https://www.youtube.com/watch?v=7lKpzGtoQX0

Importing Parts from Onshape
We have to export our parts to fusion 360 in order to use the CAM software. All parts that are programmed from a template will fall into two categories: sheet and tube. 

Take a look at this assembly:
https://cad.onshape.com/documents/6006bfe527a332986f6698c5/w/2451c39deadd9ca943cb7670/e/729b7e6010078ee459fa5090?renderMode=0&uiState=6868beeee96e971640f45b21


This assembly (our first experimental climber from 2025), contains both sheet metal and tube parts. One way to move this assembly over to fusion 360 is to export the whole thing. Right click on the bottom tab and export. Remember to always export the file as a .STEP. 
Caution: I would not recommend doing this for large assemblies, such as the entire robot. This will cause Fusion 360 to be really laggy, instead use the following method.


The other way to export is by selecting only what you need. In this case, I only selected the ¼ aluminum parts. Right click anywhere and export the selected parts.

Next we want to import the parts. Go to Fusion 360. Do ctrl + o and click open from my computer. Select the file you exported.


The parts should appear like this:


Using the Arrange Feature
-------------------------


One of the main reasons we use Fusion 360 to CAM is the arrange feature. This feature allows you to arrange parts on a flat sheet in a somewhat optimized way. Switch from the design to the Manufacture workspace.


Create a Manufacturing Model. This essentially creates a faux design work space inside of the manufacturing workspace. Since we import our parts, it actually doesn’t matter whether we do this or not, but it's best practice to make your arrangement in the manufacturing model.



Edit the Manufacturing Model. Your toolbar should now look like the design work space.


Create a sketch on an arbitrary plane. Make a rectangle anywhere. It doesn’t matter if it is unconstrained, only the size of the rectangle matters. In this case, the rectangle represents the size of the sheet metal that we are going to use. Since our metal comes in a standard 24 by 36 size, that’s what we should dimension our rectangle to be.

Finish the sketch but stay in the manufacturing model. Go to Modify and find the arrange feature.




This is the feature pop up. Objects are the parts that are to be arranged, while the Envelopes is the surface/boundary of the arrangement. Switch the envelopes tab. Select the sketch we just created as the envelope.



Here are the spacing settings I use for a 4mm endmill.

Switch back to the objects Tab. Begin selecting the parts you want to arrange. Remember to select the faces you want pointing up. You should see the sketch you made begin to populate with parts.


Reminder: Be sure that sketch is on the bottom of the part. We zero off the wasteboard, so we want the bounding sketch to reflect that.

Once the arrangement is done, exit the manufacturing model.

Importing Templates
On the top left corner of the screen, you should see the hub which you are part of. Ask a mentor to be added to this hub. 


Once you’re in the hub, find the directory
Machining > 2024 Offseason > Templates

Double click Tubing Template



You should see a sample part and set of operations.This file also serves as a guide for what each operation is intended to do.


To store these operations as a template, left click the first operation, it should highlight it blue. Then, without clicking off, hold shift and left click and the last operation. This will select all operations between them. Right click, at the bottom of the pop up, you should see an option to “Store as Template”.


Save the template locally, and name the template. Since we may occasionally update the template, add the date of the last revision (which should be in the set up name), so we can keep track of the version of the template.

Check that you have the template, open a new document with ctrl + n, switch to the manufacturing workspace, create a new set up (just click OK and ignore any warnings).

Right click the set up, you should see an option to “Create From Template”, with the templates you have. If your templates don’t appear here, click Select Template and they should appear here.

Repeat the process for the sheet template.

CAM the sheet using a template
------------------------------

Create a new set up. Go to Model, and select the arrangement by going under the manufacturing Models like so and clicking on it. This will select all parts in that arrangement.

Under the Work Coordinate System, use “Selected Point” and click the bottom left corner of the sketch we made for the arrangement.



Next go to the stock page. Make sure that it is in relative stock mode and be sure to select “No additional stock”.



Click OK.

Right click on the set up we just created and select our Sheet Template.

The setup will become populated with several operations, all with error messages.



Use these templates to select the appropriate geometry, and delete any operations that are not used. A step by step for this portion would be time consuming, and I believe that it is better to understand each operation rather than using rote memorization. Please refer to the template sample to see how each.

ALWAYS REMEMBER TO SCREW PARTS DOWN BEFORE P2
Job Order
Operation
Purpose
Notes/Comments
P1
Oversized Bore
Roughs out holes that are bigger than 2x the diameter of the endmill
This is the operation same as the through pockets, but must be before Through Bore.
Through Bore
Cuts and finishes all holes that go completely through the material including those selected in Oversized Bored


Counter Bore
Finishes bores that don't break through, typically in a counterbore. 
Use a blind pocket if the offset from the inner hole and counter bore is greater than the diameter of the end mill.
Slots
Cuts and finishes slots
Is the same as Counter Cut Out.
TM
10-32 Thread mill
Cuts 10-32 threads
Switch to thread mill, post as its own job
P2
Through Pockets
Roughs pockets that go completely through the material


Through Pocket Finish
Finishes the Through Pockets.
Is simply a 2d contour operation; derive this operation to save time tediously reselecting geometry for large jobs
Blind Pocket
Roughs pockets that don’t completely break through


Blind Pocket Finish
Finishes the Blind Pockets.


Counter Cut Out
Cuts the part out of the sheet




In just a few minutes we have completely CAM’d this sheet of metal. Very nice!



