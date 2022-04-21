using System;
using System.Collections.Generic;
using System.Linq;
using MathNet.Numerics.LinearAlgebra;

class CompanarityTest
{
    protected const int PRECISION = 5;
    
    public static bool IsComplanar(params Vector7[] vectors)
    {
        List<double[]> vectorCmps = (from cmp in vectors select cmp.Components).ToList();
        var vectorMatrix = CreateMatrix.DenseOfArray(Auxiliaries.CreateRectangularArray<double>(vectorCmps));
        var svd = vectorMatrix.Svd();
        return svd.S.Count(p => Math.Round(p, PRECISION) == 0.0) <= 2;
    }
}
