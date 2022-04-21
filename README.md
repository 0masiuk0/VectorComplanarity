# VectorComplanarity
n-dimantional vector complanarity, appriximate matrix rank

The theory is that if you stack vectors as matrix (vectors as rows or columns) and find matrix rank, then if rank is 1, vectors are collinear (same direction or opposite direction). If rank is 2 then vectors are complanar. Any vector can be represented as linear combination of any other two non-collinear vectors. They are in the same plane, so to speak.

That's theory. In practice as soon as you start do funny things, that will use full depth of float type (normalization, trigonometry), float precision will screw your rank detection. Sometimes some determinant inside there will be 10e-26, not zero, and you get higher matrix rank than it deserves. NumPi and MathNet for Python and C# have measures to deal with this, but in my tests it fails sometimes. I did this matrix tests for thousands of random vectors A and B and random coefs n and m for [A, B, (n*A+m*B)] matrices ranks and they are above 2 sometimes.
So here is some functions I came up with through trial and error that test for complanarity with arbitary precision.

You can quicly turn this into appriximate matrix rank determination. Matrix rank equals number of non-zero components in s array.

In 3d you do not need any of this. Test for triple product to be equal to zero. a*(b x c) == 0.
