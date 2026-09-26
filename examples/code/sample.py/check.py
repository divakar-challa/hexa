import contextlib
import io
import tabnanny

report = io.StringIO()
with contextlib.redirect_stdout(report):
    tabnanny.check("sample.py")
print(report.getvalue().strip() or "indentation is consistent")
