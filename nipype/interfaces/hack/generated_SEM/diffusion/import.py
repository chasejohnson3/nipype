# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import (CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec,
                    File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath)
import os


class DWIConvertInputSpec(CommandLineInputSpec):
    conversionMode = traits.Enum("DicomToNrrd", "DicomToFSL", "NrrdToFSL", "FSLToNrrd", argstr="--conversionMode %s", desc="Determine which conversion to perform. DicomToNrrd (default): Convert DICOM series to NRRD DicomToFSL: Convert DICOM series to NIfTI File + gradient/bvalue text files NrrdToFSL: Convert DWI NRRD file to NIfTI File + gradient/bvalue text files FSLToNrrd: Convert NIfTI File + gradient/bvalue text files to NRRD file.")
    inputVolume = File(argstr="--inputVolume %s", desc="Input DWI volume -- not used for DicomToNrrd mode.", exists=True)
    outputVolume = traits.Either(traits.Bool, File(), argstr="--outputVolume %s", desc="Output filename (.nhdr or .nrrd)", hash_files=False)
    inputDicomDirectory = Directory(argstr="--inputDicomDirectory %s", desc="Directory holding Dicom series", exists=True)
    fslNIFTIFile = File(argstr="--fslNIFTIFile %s", desc="4D NIfTI file containing gradient volumes", exists=True)
    inputBValues = File(argstr="--inputBValues %s", desc="The B Values are stored in FSL .bval text file format", exists=True)
    inputBVectors = File(argstr="--inputBVectors %s", desc="The Gradient Vectors are stored in FSL .bvec text file format", exists=True)
    outputNiftiFile = traits.Either(traits.Bool, File(), argstr="--outputNiftiFile %s", desc="Nifti output filename (for Slicer GUI use).", hash_files=False)
    outputBValues = traits.Either(traits.Bool, File(), argstr="--outputBValues %s", desc="The B Values are stored in FSL .bval text file format (defaults to <outputVolume>.bval)", hash_files=False)
    outputBVectors = traits.Either(traits.Bool, File(), argstr="--outputBVectors %s", desc="The Gradient Vectors are stored in FSL .bvec text file format (defaults to <outputVolume>.bvec)", hash_files=False)
    writeProtocolGradientsFile = traits.Bool(argstr="--writeProtocolGradientsFile ", desc="Write the protocol gradients to a file suffixed by \'.txt\' as they were specified in the procol by multiplying each diffusion gradient direction by the measurement frame.  This file is for debugging purposes only, the format is not fixed, and will likely change as debugging of new dicom formats is necessary.")
    useIdentityMeaseurementFrame = traits.Bool(argstr="--useIdentityMeaseurementFrame ", desc="Adjust all the gradients so that the measurement frame is an identity matrix.")
    useBMatrixGradientDirections = traits.Bool(argstr="--useBMatrixGradientDirections ", desc="Fill the nhdr header with the gradient directions and bvalues computed out of the BMatrix. Only changes behavior for Siemens data.  In some cases the standard public gradients are not properly computed.  The gradients can emperically computed from the private BMatrix fields.  In some cases the private BMatrix is consistent with the public grandients, but not in all cases, when it exists BMatrix is usually most robust.")
    outputDirectory = traits.Either(traits.Bool, Directory(), argstr="--outputDirectory %s", desc="Directory holding the output NRRD file", hash_files=False)
    smallGradientThreshold = traits.Float(argstr="--smallGradientThreshold %f", desc="If a gradient magnitude is greater than 0 and less than smallGradientThreshold, then DWIConvert will display an error message and quit, unless the useBMatrixGradientDirections option is set.")
    transposeInputBVectors = traits.Bool(argstr="--transposeInputBVectors ", desc="FSL input BVectors are expected to be encoded in the input file as one vector per line. If it is not the case, use this option to transpose the file as it is read")
    allowLossyConversion = traits.Bool(argstr="--allowLossyConversion ", desc="The only supported output type is 'short'. Conversion from images of a different type may cause data loss due to rounding or truncation. Use with caution!\'")
    gradientVectorFile = traits.Either(traits.Bool, File(), argstr="--gradientVectorFile %s", desc="DEPRECATED:  Use --inputBVector --inputBValue files Text file giving gradient vectors", hash_files=False)
    fMRI = traits.Bool(argstr="--fMRI ", desc="DEPRECATED:  No support or testing.  Output a NRRD file, but without gradients")


class DWIConvertOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output filename (.nhdr or .nrrd)", exists=True)
    outputNiftiFile = File(desc="Nifti output filename (for Slicer GUI use).", exists=True)
    outputBValues = File(desc="The B Values are stored in FSL .bval text file format (defaults to <outputVolume>.bval)", exists=True)
    outputBVectors = File(desc="The Gradient Vectors are stored in FSL .bvec text file format (defaults to <outputVolume>.bvec)", exists=True)
    outputDirectory = Directory(desc="Directory holding the output NRRD file", exists=True)
    gradientVectorFile = File(desc="DEPRECATED:  Use --inputBVector --inputBValue files Text file giving gradient vectors", exists=True)


class DWIConvert(SEMLikeCommandLine):
    """title: Diffusion-weighted DICOM Import (DWIConvert)

category: Diffusion.Import and Export

description: Converts diffusion weighted MR images in DICOM series into NRRD format for analysis in Slicer. This program has been tested on only a limited subset of DTI DICOM formats available from Siemens, GE, and Philips scanners. Work in progress to support DICOM multi-frame data. The program parses DICOM header to extract necessary information about measurement frame, diffusion weighting directions, b-values, etc, and write out a NRRD image. For non-diffusion weighted DICOM images, it loads in an entire DICOM series and writes out a single dicom volume in a .nhdr/.raw pair.

version: 5.2.0

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.5/Modules/DWIConverter

license: Apache License Version 2.0

contributor: Hans Johnson (UIowa), Vince Magnotta (UIowa) Joy Matsui (UIowa), Kent Williams (UIowa), Mark Scully (Uiowa), Xiaodong Tao (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.  Additional support for DTI data produced on Philips scanners was contributed by Vincent Magnotta and Hans Johnson at the University of Iowa.

"""

    input_spec = DWIConvertInputSpec
    output_spec = DWIConvertOutputSpec
    _cmd = " DWIConvert "
    _outputs_filenames = {'outputVolume':'outputVolume.nii','outputNiftiFile':'outputNiftiFile.nii','outputBValues':'outputBValues.bval','outputBVectors':'outputBVectors.bvec','outputDirectory':'outputDirectory','gradientVectorFile':'gradientVectorFile'}
    _redirect_x = False
