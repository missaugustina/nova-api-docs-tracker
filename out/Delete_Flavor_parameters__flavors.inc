Verify all parameters for Delete Flavor in flavors.inc

Source Code: ../tests/test_files/flavors.inc

1. Are all parameters that exist in the resource listed?
[]

2. Are all parameters referencing the right lookup value in parameters.yaml?
name, id are common issues, will need $foo_name and $foo_id created

3. Add microversion parameters at the end of the table in order of introduction
min_ver: 2.10 is a valid parameter key
