# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import (CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec,
                    File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath)
import os


class PerformMetricTestInputSpec(CommandLineInputSpec):
    inputBSplineTransform = File(argstr="--inputBSplineTransform %s", desc=",         Input transform that is use to warp moving image before metric comparison.,       ", exists=True)
    inputFixedImage = File(argstr="--inputFixedImage %s", exists=True)
    inputMovingImage = File(argstr="--inputMovingImage %s", exists=True)
    metricType = traits.Enum("MMI", "MSE", argstr="--metricType %s", desc="Comparison metric type")
    numberOfSamples = traits.Int(argstr="--numberOfSamples %d", desc="The number of voxels sampled for metric evaluation.")
    numberOfHistogramBins = traits.Int(argstr="--numberOfHistogramBins %d", desc="The number of historgram bins when MMI (Mattes) is metric type.")


class PerformMetricTestOutputSpec(TraitedSpec):
    pass


class PerformMetricTest(SEMLikeCommandLine):
    """title: Metric Test

category: Registration

description: Compare Mattes/MSQ metric value for two input images and a possible input BSpline transform.

version: 5.2.0

documentation-url: A utility to compare metric value between two input images.

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Ali Ghayoor

"""

    input_spec = PerformMetricTestInputSpec
    output_spec = PerformMetricTestOutputSpec
    _cmd = " PerformMetricTest "
    _outputs_filenames = {}
    _redirect_x = False