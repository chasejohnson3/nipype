# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import (CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec,
                    File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath)
import os


class ACPCTransformInputSpec(CommandLineInputSpec):
    acpc = InputMultiPath(traits.List(traits.Float(), minlen=3, maxlen=3), argstr="--acpc %s...", desc="ACPC line, a list of two fiducial points, one at the anterior commissure and one at the posterior commissure.")
    midline = InputMultiPath(traits.List(traits.Float(), minlen=3, maxlen=3), argstr="--midline %s...", desc="The midline is a series of points (at least 3) defining the division between the hemispheres of the brain (the mid sagittal plane).")
    outputTransform = traits.Either(traits.Bool, File(), argstr="--outputTransform %s", desc="A transform filled in from the ACPC and Midline registration calculation.", hash_files=False)


class ACPCTransformOutputSpec(TraitedSpec):
    outputTransform = File(desc="A transform filled in from the ACPC and Midline registration calculation.", exists=True)


class ACPCTransform(SEMLikeCommandLine):
    """title: ACPC Transform

category: Registration.Specialized

description: <p>Calculate a transformation that aligns brain images to standard orientation based on anatomical landmarks.</p><p>The ACPC line extends between two points, one at the anterior commissure and one at the posterior commissure. The resulting transform will bring the line connecting the two points horizontal to the AP axis.</p><p>The midline is a series of points (at least 3) defining the division between the hemispheres of the brain (the mid sagittal plane). The resulting transform will result in the output volume having the mid sagittal plane lined up with the AS plane.</p><p>Use the Filtering module <b>Resample Scalar/Vector/DWI Volume</b> to apply the transformation to a volume.</p>

version: 1.0

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/ACPCTransform

license: slicer3

contributor: Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = ACPCTransformInputSpec
    output_spec = ACPCTransformOutputSpec
    _cmd = " ACPCTransform "
    _outputs_filenames = {'outputTransform':'outputTransform.txt'}
    _redirect_x = False


class BRAINSTransformFromFiducialsInputSpec(CommandLineInputSpec):
    fixedLandmarks = InputMultiPath(traits.List(traits.Float(), minlen=3, maxlen=3), argstr="--fixedLandmarks %s...", desc="Ordered list of landmarks in the fixed image")
    movingLandmarks = InputMultiPath(traits.List(traits.Float(), minlen=3, maxlen=3), argstr="--movingLandmarks %s...", desc="Ordered list of landmarks in the moving image")
    saveTransform = traits.Either(traits.Bool, File(), argstr="--saveTransform %s", desc="Save the transform that results from registration", hash_files=False)
    transformType = traits.Enum("Translation", "Rigid", "Similarity", argstr="--transformType %s", desc="Type of transform to produce")
    fixedLandmarksFile = File(argstr="--fixedLandmarksFile %s", desc="An fcsv formatted file with a list of landmark points.", exists=True)
    movingLandmarksFile = File(argstr="--movingLandmarksFile %s", desc="An fcsv formatted file with a list of landmark points.", exists=True)
    numberOfThreads = traits.Int(argstr="--numberOfThreads %d", desc="Explicitly specify the maximum number of threads to use.")


class BRAINSTransformFromFiducialsOutputSpec(TraitedSpec):
    saveTransform = File(desc="Save the transform that results from registration", exists=True)


class BRAINSTransformFromFiducials(SEMLikeCommandLine):
    """title: Fiducial Registration (BRAINS)

category: Registration.Specialized

description: Computes a rigid, similarity or affine transform from a matched list of fiducials

version: 5.2.0

documentation-url: http://www.slicer.org/slicerWiki/index.php/Modules:TransformFromFiducials-Documentation-3.6

contributor: Casey B Goodlett

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = BRAINSTransformFromFiducialsInputSpec
    output_spec = BRAINSTransformFromFiducialsOutputSpec
    _cmd = " BRAINSTransformFromFiducials "
    _outputs_filenames = {'saveTransform':'saveTransform.h5'}
    _redirect_x = False


class FiducialRegistrationInputSpec(CommandLineInputSpec):
    fixedLandmarks = InputMultiPath(traits.List(traits.Float(), minlen=3, maxlen=3), argstr="--fixedLandmarks %s...", desc="Ordered list of landmarks in the fixed image")
    movingLandmarks = InputMultiPath(traits.List(traits.Float(), minlen=3, maxlen=3), argstr="--movingLandmarks %s...", desc="Ordered list of landmarks in the moving image")
    saveTransform = traits.Either(traits.Bool, File(), argstr="--saveTransform %s", desc="Save the transform that results from registration", hash_files=False)
    transformType = traits.Enum("Translation", "Rigid", "Similarity", argstr="--transformType %s", desc="Type of transform to produce")
    rms = traits.Float(argstr="--rms %f", desc="Display RMS Error.")
    outputMessage = traits.Str(argstr="--outputMessage %s", desc="Provides more information on the output")


class FiducialRegistrationOutputSpec(TraitedSpec):
    saveTransform = File(desc="Save the transform that results from registration", exists=True)


class FiducialRegistration(SEMLikeCommandLine):
    """title: Fiducial Registration

category: Registration.Specialized

description: Computes a rigid, similarity or affine transform from a matched list of fiducials

version: 0.1.0.$Revision$

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/TransformFromFiducials

contributor: Casey B Goodlett (Kitware), Dominik Meier (SPL, BWH)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = FiducialRegistrationInputSpec
    output_spec = FiducialRegistrationOutputSpec
    _cmd = " FiducialRegistration "
    _outputs_filenames = {'saveTransform':'saveTransform.txt'}
    _redirect_x = False
