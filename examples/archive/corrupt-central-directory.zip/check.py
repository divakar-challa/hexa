import zipfile

try:
    with zipfile.ZipFile("corrupt-central-directory.zip") as z:
        bad = z.testzip()   # reads every entry and checks its CRC
        print(f"corrupt entry: {bad}" if bad else "ok")
except zipfile.BadZipFile as e:
    print("rejected:", e)
