# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..maths import SpatialFilter


def test_SpatialFilter_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=2,),
        internal_datatype=dict(argstr="-dt %s", position=1,),
        kernel_file=dict(
            argstr="%s", extensions=None, position=5, xor=["kernel_size"],
        ),
        kernel_shape=dict(argstr="-kernel %s", position=4,),
        kernel_size=dict(argstr="%.4f", position=5, xor=["kernel_file"],),
        nan2zeros=dict(argstr="-nan", position=3,),
        operation=dict(argstr="-f%s", mandatory=True, position=6,),
        out_file=dict(
            argstr="%s", extensions=None, genfile=True, hash_files=False, position=-2,
        ),
        output_datatype=dict(argstr="-odt %s", position=-1,),
        output_type=dict(),
    )
    inputs = SpatialFilter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SpatialFilter_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = SpatialFilter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
