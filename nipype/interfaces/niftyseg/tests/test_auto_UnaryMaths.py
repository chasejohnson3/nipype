# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..maths import UnaryMaths


def test_UnaryMaths_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=2,),
        operation=dict(argstr="-%s", mandatory=True, position=4,),
        out_file=dict(
            argstr="%s",
            extensions=None,
            name_source=["in_file"],
            name_template="%s",
            position=-2,
        ),
        output_datatype=dict(argstr="-odt %s", position=-3,),
    )
    inputs = UnaryMaths.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_UnaryMaths_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = UnaryMaths.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
