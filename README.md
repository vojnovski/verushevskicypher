Verushevski Cypher encoder/decoder
==================================

A python module allowing encoding and decoding with the infamous Verushevski cypher.

Usage
-----

    python verushevskicypher.py encode zdravo plenumci

or

    python verushevskicypher.py decode 18_22_44_24_12_0_50_12_39_3_22_0_18_44_24_5_33_3_5_51_51
    
#### Mapfile ####
    
There is also an optional argument **--mapfile** which specifies a JSON file that contains the cypher:
    
    python verushevskicypher.py --mapfile="C:/verushevski.json" encode zdravo
    
By default, mapfile is set to *"encode_map.json"* inside this repo. The file should be a JSON object with keys "a", "b", "c", ... and values "7", "4", "20" (the substitutions).

Comments
--------

Some letters (plus all uppercase, and all non-ascii) are missing, feel free to contribute.
