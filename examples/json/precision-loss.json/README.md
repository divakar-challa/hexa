# precision-loss.json

Integers and decimals that exceed IEEE-754 double precision: 64-bit IDs, high-precision decimals, and values at MAX_SAFE_INTEGER boundaries.

Page: https://hexaqa.com/file/structured-data/precision-loss-json

```bash
curl -fsSL -o "precision-loss.json" "https://files.hexaqa.com/json/precision-loss.json"
```

SHA-256: `7075086fd6d6809ccd379203d3d4f803c22d4c44593b109f0032b1a8b9ba2e08`

## Node.js

JSON.parse turns every number into a double, so integers above 2^53 change silently. In recent Node versions the reviver also receives the original source text, which lets you keep them exact as BigInt.

```bash
node check.js
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
oneAbove: 9007199254740993n
snowflakeId: 1234567890123456789n
```

## Python

Python integers are exact at any size, so only decimals can lose precision. parse_float=Decimal keeps them as written.

```bash
python check.py
```

Output when run against this file (Python 3.14.4, Node 24.15.0):

```
oneAbove: 9007199254740993
highPrecisionDecimal: 0.1234567890123456789
```
