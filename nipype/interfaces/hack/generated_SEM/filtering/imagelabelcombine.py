# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import (CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec,
                    File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath)
import os


class ImageLabelCombineInputSpec(CommandLineInputSpec):
    InputLabelMap_A = File(argstr="%s", desc="Label map image", position=-3, exists=True)
    InputLabelMap_B = File(argstr="%s", desc="Label map image", position=-2, exists=True)
    OutputLabelMap = traits.Either(traits.Bool, File(), argstr="%s", desc="Resulting Label map image", position=-1, hash_files=False)
    first_overwrites = traits.Bool(argstr="--first_overwrites ", desc="Use first or second label when both are present")


class ImageLabelCombineOutputSpec(TraitedSpec):
    OutputLabelMap = File(desc="Resulting Label map image", position=-1, exists=True)


class ImageLabelCombine(SEMLikeCommandLine):
    """title: Image Label Combine

category: Filtering

description: Combine two label maps into one

version: 0.1.0

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/ImageLabelCombine

contributor: Alex Yarmarkovich (SPL, BWH)

"""

    input_spec = ImageLabelCombineInputSpec
    output_spec = ImageLabelCombineOutputSpec
    _cmd = " ImageLabelCombine "
    _outputs_filenames = {'OutputLabelMap':'OutputLabelMap.nii'}
    _redirect_x = False