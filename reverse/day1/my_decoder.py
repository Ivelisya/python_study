import base64 as base

encoded_str = "h/zydy7HG8M7ZNzC02iIeLMw7mvShzidvUixjW+V+7GolPGfMVFdCsB0FX/MxbY1hAfBc67t4rRC4VzTxMPdd0eyALvSIkeBTFD/Svlou7wtw/pql8eMaBgodh1SiP+ueFY0RFzHLPqIpBcl10lBTNK721DpS8Dqlg418xLmfLhrjb/9NnBHlDLhiWaX85sFp8Zp9AuycOSBhfSYPoFXKkXJhLoWwKBz9TVeXw0b4PCk4/wYSzWXNJPm0Mx/TGpG+Nr22g4AXLcEwwUw44nnbFwSzpmZaTjB1nzyEKzT+58="
decoded_bytes = base.b64decode(encoded_str)
try:
    decoded_str = decoded_bytes.decode('utf-8')
    print("Decoded string:", decoded_str)
except UnicodeDecodeError:
    print("The decoded bytes do not represent a UTF-8 string.")