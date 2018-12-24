# picat
Raspberry Pi based Cat Toy. 

I decided to make a cat toy based on the Raspberry Pi. The concept works, but the mechanical prototype I made was not durable enough to withstand the cat's enjoyment of the toy. My fabrication skills are lacking, as are my tools, materials, patience, etc.

The toy uses an HC-SR04 ultrasonic distance sensor to determine when the cat approaches. When the cat is sensed, a gimbal that is powered by two servo motors starts waving a cat toy suspended on a string. The two servos on the gimbal vary the tilt and rotation of the gimbal platform. The platform has a stick about 12 inches in length affixed to it. A stuffed bird cat toy is tied to the end of the stick. When the cat walks away, the sensor 'notices' and the gimbal stops jerking the toy around. If the cat returns, playtime resumes.

Python code that controls this contraption is hereby checked in. 
