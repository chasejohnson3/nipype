# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import (CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec,
                    File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath)
import os


class BRAINSDWICleanupInputSpec(CommandLineInputSpec):
    inputVolume = File(argstr="--inputVolume %s", desc="Required: input image is a 4D NRRD image.", exists=True)
    outputVolume = traits.Either(traits.Bool, File(), argstr="--outputVolume %s", desc="given a list of ", hash_files=False)
    badGradients = InputMultiPath(traits.Int, argstr="--badGradients %s", sep=",")


class BRAINSDWICleanupOutputSpec(TraitedSpec):
    outputVolume = File(desc="given a list of ", exists=True)


class BRAINSDWICleanup(SEMLikeCommandLine):
    """title: BRAINSDWICleanup

category: Diffusion.Utilities

description: Remove bad gradients/volumes from DWI NRRD file.

version: 5.2.0

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: This tool was developed by Kent Williams.

"""

    input_spec = BRAINSDWICleanupInputSpec
    output_spec = BRAINSDWICleanupOutputSpec
    _cmd = " BRAINSDWICleanup "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
    _redirect_x = False


class ResampleDTIVolumeInputSpec(CommandLineInputSpec):
    inputVolume = File(argstr="%s", desc="Input volume to be resampled", position=-2, exists=True)
    outputVolume = traits.Either(traits.Bool, File(), argstr="%s", desc="Resampled Volume", position=-1, hash_files=False)
    Reference = File(argstr="--Reference %s", desc="Reference Volume (spacing,size,orientation,origin)", exists=True)
    transformationFile = File(argstr="--transformationFile %s", exists=True)
    defField = File(argstr="--defField %s", desc="File containing the deformation field (3D vector image containing vectors with 3 components)", exists=True)
    hfieldtype = traits.Enum("displacement", "h-Field", argstr="--hfieldtype %s", desc="Set if the deformation field is an -Field")
    interpolation = traits.Enum("linear", "nn", "ws", "bs", argstr="--interpolation %s", desc="Sampling algorithm (linear , nn (nearest neighborhoor), ws (WindowedSinc), bs (BSpline) )")
    noMeasurementFrame = traits.Bool(argstr="--noMeasurementFrame ", desc="Do not use the measurement frame that is in the input image to transform the tensors. Uses the image orientation instead")
    correction = traits.Enum("zero", "none", "abs", "nearest", argstr="--correction %s", desc="Correct the tensors if computed tensor is not semi-definite positive")
    transform_tensor_method = traits.Enum("PPD", "FS", argstr="--transform_tensor_method %s", desc="Chooses between 2 methods to transform the tensors: Finite Strain (FS), faster but less accurate, or Preservation of the Principal Direction (PPD)")
    transform_order = traits.Enum("input-to-output", "output-to-input", argstr="--transform_order %s", desc="Select in what order the transforms are read")
    notbulk = traits.Bool(argstr="--notbulk ", desc="The transform following the BSpline transform is not set as a bulk transform for the BSpline transform")
    spaceChange = traits.Bool(argstr="--spaceChange ", desc="Space Orientation between transform and image is different (RAS/LPS) (warning: if the transform is a Transform Node in Slicer3, do not select)")
    rotation_point = traits.List(argstr="--rotation_point %s", desc="Center of rotation (only for rigid and affine transforms)")
    centered_transform = traits.Bool(argstr="--centered_transform ", desc="Set the center of the transformation to the center of the input image (only for rigid and affine transforms)")
    image_center = traits.Enum("input", "output", argstr="--image_center %s", desc="Image to use to center the transform (used only if \'Centered Transform\' is selected)")
    Inverse_ITK_Transformation = traits.Bool(argstr="--Inverse_ITK_Transformation ", desc="Inverse the transformation before applying it from output image to input image (only for rigid and affine transforms)")
    spacing = InputMultiPath(traits.Float, argstr="--spacing %s", desc="Spacing along each dimension (0 means use input spacing)", sep=",")
    size = InputMultiPath(traits.Float, argstr="--size %s", desc="Size along each dimension (0 means use input size)", sep=",")
    origin = traits.List(argstr="--origin %s", desc="Origin of the output Image")
    direction_matrix = InputMultiPath(traits.Float, argstr="--direction_matrix %s", desc="9 parameters of the direction matrix by rows (ijk to LPS if LPS transform, ijk to RAS if RAS transform)", sep=",")
    number_of_thread = traits.Int(argstr="--number_of_thread %d", desc="Number of thread used to compute the output image")
    default_pixel_value = traits.Float(argstr="--default_pixel_value %f", desc="Default pixel value for samples falling outside of the input region")
    window_function = traits.Enum("h", "c", "w", "l", "b", argstr="--window_function %s", desc="Window Function \nh = Hamming \nc = Cosine \nw = Welch \nl = Lanczos \nb = Blackman")
    spline_order = traits.Int(argstr="--spline_order %d", desc="Spline Order (Spline order may be from 0 to 5)")
    transform_matrix = InputMultiPath(traits.Float, argstr="--transform_matrix %s", desc="12 parameters of the transform matrix by rows ( --last 3 being translation-- )", sep=",")
    transform = traits.Enum("rt", "a", argstr="--transform %s", desc="Transform algorithm\nrt = Rigid Transform\na = Affine Transform")


class ResampleDTIVolumeOutputSpec(TraitedSpec):
    outputVolume = File(desc="Resampled Volume", position=-1, exists=True)


class ResampleDTIVolume(SEMLikeCommandLine):
    """title: Resample DTI Volume

category: Diffusion.Utilities

description: Resampling an image is a very important task in image analysis. It is especially important in the frame of image registration. This module implements DT image resampling through the use of itk Transforms. The resampling is controlled by the Output Spacing. "Resampling" is performed in space coordinates, not pixel/grid coordinates. It is quite important to ensure that image spacing is properly set on the images involved. The interpolator is required since the mapping from one space to the other will often require evaluation of the intensity of the image at non-grid positions.

version: 1.0.2

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/ResampleDTI

contributor: Francois Budin (UNC)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149. Information on the National Centers for Biomedical Computing can be obtained from http://nihroadmap.nih.gov/bioinformatics

"""

    input_spec = ResampleDTIVolumeInputSpec
    output_spec = ResampleDTIVolumeOutputSpec
    _cmd = " ResampleDTIVolume "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
    _redirect_x = False
