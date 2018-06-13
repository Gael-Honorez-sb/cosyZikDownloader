from cx_Freeze import setup, Executable

base = None    

executables = [Executable("cosyZikDownloader.py", base=base)]

packages = ["idna", "discord", "sys", "asyncio", "re", "youtube_dl"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "cosyZikDownloader",
    options = options,
    version = "1",
    description = 'Choppe la zik trop cosy',
    executables = executables
)